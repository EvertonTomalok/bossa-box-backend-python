import asyncio
import json
from datetime import datetime

import nest_asyncio
from fastapi import FastAPI, Header, Path
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse, Response

from src.controllers.token import TokenController
from src.controllers.tools import ToolsController
from src.helpers.auth import check_jwt
from src.helpers.queue import SCRAPPING_LINK_TOPIC_KAFKA
from src.models.routes import Tool, User
from src.models.swagger_responses import (
    RESPONSE_RETURN_FIND_TOOL,
    RESPONSE_RETURN_POST_TOOL,
    RESPONSE_RETURN_TOKEN, RESPONSE_RETURN_PUT_TOOL,
)

nest_asyncio.apply()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = datetime.now()
    response = await call_next(request)
    process_time = datetime.now() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>Tools WebService</title>
        </head>
        <body>
            <h1>Tools WebService</h1>
        </body>
    </html>
    """


@app.get("/health", response_class=HTMLResponse)
async def health():
    return "<p>Ok</p>"


@app.get(
    "/tools",
    status_code=200,
    response_class=JSONResponse,
    responses=RESPONSE_RETURN_FIND_TOOL,
)
@check_jwt
async def get_tools(
    tag: str = "", skip: int = 0, limit: int = 10, token: str = Header("")
):
    return ToolsController.find_tools(tag, skip, limit)


@app.post(
    "/tools",
    status_code=201,
    response_class=JSONResponse,
    responses=RESPONSE_RETURN_POST_TOOL,
)
@check_jwt
async def tools_send(tool: Tool, token: str = Header("")):
    tool_object = ToolsController.add_tool(json.loads(tool.json()))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        await SCRAPPING_LINK_TOPIC_KAFKA.send(
            value={"link": tool_object["data"]["link"]}
        )
    )
    return tool_object


@app.delete(
    "/tools/{id}", status_code=204, response_class=HTMLResponse,
)
@check_jwt
async def tool_delete(
    id: str = Path(..., title="The ID of the item to delete"), token: str = Header(""),
):
    ToolsController.delete_tool(id=id)
    return ""


@app.put(
    "/tools/{id}",
    status_code=200,
    response_class=JSONResponse,
    responses=RESPONSE_RETURN_PUT_TOOL,
)
@check_jwt
async def tool_update(
    tool: Tool,
    id: str = Path(..., title="The ID of the item to delete"),
    token: str = Header(""),
):
    if new_tool := ToolsController.update_tool(id=id, tool=json.loads(tool.json())):
        return new_tool
    return Response(content="", status_code=204)


@app.post(
    "/token",
    status_code=201,
    response_class=JSONResponse,
    responses=RESPONSE_RETURN_TOKEN,
)
async def create_token(user: User):
    return TokenController.create_token(json.loads(user.json()))
