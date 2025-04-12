import os
import platform
import subprocess
import requests
import zipfile
import tarfile
import shutil

def check_aria2c():
    """检查当前目录下是否存在 aria2c"""
    return os.path.exists("aria2c") or os.path.exists("aria2c.exe")

def download_aria2c():
    """根据系统类型下载 aria2c"""
    system = platform.system()
    if system == "Windows":
        url = "https://github.com/aria2/aria2/releases/download/release-1.36.0/aria2-1.36.0-win-64bit-build1.zip"
        filename = "aria2.zip"
    elif system == "Linux":
        url = "https://github.com/aria2/aria2/releases/download/release-1.36.0/aria2-1.36.0-linux-glibc228-x86_64.tar.bz2"
        filename = "aria2.tar.bz2"
    elif system == "Darwin":  # macOS
        url = "https://github.com/aria2/aria2/releases/download/release-1.36.0/aria2-1.36.0-osx-darwin.dmg"
        filename = "aria2.dmg"
    else:
        print("不支持的操作系统")
        return

    print(f"正在下载 aria2c 到当前目录...")
    response = requests.get(url, stream=True)
    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    if system == "Windows":
        with zipfile.ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall(".")
        os.rename("aria2-1.36.0-win-64bit-build1/aria2c.exe", "aria2c.exe")
        shutil.rmtree("aria2-1.36.0-win-64bit-build1")
    elif system == "Linux":
        with tarfile.open(filename, "r:bz2") as tar_ref:
            tar_ref.extractall(".")
        os.rename("aria2-1.36.0-linux-glibc228-x86_64/aria2c", "aria2c")
        shutil.rmtree("aria2-1.36.0-linux-glibc228-x86_64")
    elif system == "Darwin":
        print("macOS 下载完成后需要手动挂载 DMG 文件并安装")

    os.remove(filename)
    print("aria2c 下载完成")

def auto_download_aria2c():
    if check_aria2c():
        print("当前目录下已存在 aria2c，无需下载")
    else:
        download_aria2c()

if __name__ == "__main__":
    auto_download_aria2c()