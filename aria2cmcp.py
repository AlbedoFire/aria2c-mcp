from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os
from aria2p import API,Client
# 初始化连接
aria2 = API(Client(port=16800))

mcp = FastMCP()

@mcp.tool()
async def add_download(url) -> str:
    download = aria2.add_uris([url])
    return f"下载任务添加成功，任务id为{download.gid}"
@mcp.tool()
async def get_download_progress(gid)->str:
    download = aria2.get_download(gid)
    return f"下载进度为{download.progress_string()}"
@mcp.tool()
async def get_download_list() -> list:
    # 获取所有下载任务（包括活动的和等待的）
    return [{
        'gid': d.gid,
        'name': d.name,
        'status': d.status,
        'progress': d.progress_string()
    } for d in aria2.get_downloads()]
@mcp.tool()
async def get_download_status(gid)->str:
    download = aria2.get_download(gid)
    return f"下载状态为{download.status}"
@mcp.tool()
async def pause_download(gid)->None:
    download = aria2.get_download(gid)
    download.pause()
    return f"下载任务{gid}暂停成功"

@mcp.resource("config://default")
async def get_default_config() -> str:
    return "enable-rpc=true\n"+"rpc-listen-all=true\n"\
                   +"rpc-listen-port=16800\n"+\
                   "rpc-allow-origin-all=true\n"+\
                   "dir=./Downloads"
@mcp.tool()
async def start_aria2c_rpc() -> None:
    from utils import start_aria2c_rpc
    start_aria2c_rpc() 

@mcp.tool()
async def stop_aria2c_rpc() -> None:
    from utils import stop_aria2c_rpc
    stop_aria2c_rpc()
@mcp.tool()
async def check_aria2c_rpc() -> bool:
    from utils import check_aria2c_rpc
    return check_aria2c_rpc()

if __name__ == "__main__":
    mcp.run(transport='stdio')
