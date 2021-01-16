import json
from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import HTMLResponse, JSONResponse

from src.controllers.tools import add_tool, find_tools

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Tool(BaseModel):
    title: str
    link: str
    description: str
    tags: List[str]


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


@app.get("/health")
async def health():
    return "Ok"


@app.get("/tools", status_code=201, response_class=JSONResponse)
async def get_tools(tag: str = "", skip: int = 0, limit: int = 10):
    return find_tools(tag, skip, limit)


@app.post("/tools", status_code=201, response_class=JSONResponse)
async def tools_send(tool: Tool):
    return add_tool(json.loads(tool.json()))
