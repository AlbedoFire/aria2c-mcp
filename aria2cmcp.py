# 导入基本mcp库
import mcp
from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP()

def start():
    mcp.run(transport='stdio')

if __name__ == "__main__":
    mcp.run(transport='stdio')