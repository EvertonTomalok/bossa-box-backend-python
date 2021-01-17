import json
from datetime import datetime

from fastapi import FastAPI, Header, Path
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse

from src.controllers.token import TokenController
from src.controllers.tools import ToolsController
from src.helpers.auth import check_jwt
from src.models.routes import Tool, User
from src.models.swagger_responses import (
    RESPONSE_RETURN_FIND_TOOL,
    RESPONSE_RETURN_POST_TOOL,
    RESPONSE_RETURN_TOKEN,
)

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
    return ToolsController.add_tool(json.loads(tool.json()))


@app.delete(
    "/tools/{id}", status_code=204, response_class=HTMLResponse,
)
@check_jwt
async def tool_delete(
    id: str = Path(..., title="The ID of the item to delete"), token: str = Header(""),
):
    ToolsController.delete_tool(id=id)
    return ""


@app.post(
    "/token",
    status_code=201,
    response_class=JSONResponse,
    responses=RESPONSE_RETURN_TOKEN,
)
async def create_token(user: User):
    return TokenController.create_token(json.loads(user.json()))
