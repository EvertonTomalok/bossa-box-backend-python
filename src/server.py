import json

from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse

from src.controllers.tools import ToolsController
from src.models.routes import Tool
from src.models.swagger_responses import (
    RESPONSE_RETURN_FIND_TOOL,
    RESPONSE_RETURN_POST_TOOL,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    status_code=201,
    response_class=JSONResponse,
    responses=RESPONSE_RETURN_FIND_TOOL,
)
async def get_tools(tag: str = "", skip: int = 0, limit: int = 10):
    return ToolsController.find_tools(tag, skip, limit)


@app.post(
    "/tools",
    status_code=201,
    response_class=JSONResponse,
    responses=RESPONSE_RETURN_POST_TOOL,
)
async def tools_send(tool: Tool):
    return ToolsController.add_tool(json.loads(tool.json()))


@app.delete(
    "/tools/{id}",
    status_code=204,
    response_class=HTMLResponse,
)
async def tool_delete(id: str = Path(..., title="The ID of the item to delete")):
    ToolsController.delete_tool(id=id)
    return ""
