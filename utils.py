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

# 创建默认配置文件
def create_default_config():
    if not os.path.exists("aria2.conf"):
        with open("aria2.conf", "w") as f:
            f.write('''enable-rpc=true
                        rpc-listen-all=true
                        rpc-listen-port=6800
                        dir=./Downloads''')
        print("创建默认配置文件成功")
    else:
        print("配置文件已存在")

# 启动aria2c的rpc
def start_aria2c_rpc(config_file="aria2.conf"):
    if platform.system() == "Windows":
        subprocess.Popen(["aria2c", "--conf-path=" + config_file])
    else:
        subprocess.Popen(["aria2c", "--conf-path=" + config_file, "--daemon=true"])
    print("aria2c started")

# 检查aria2c是否有进程
def check_aria2c_rpc():
    if platform.system() == "Windows":
        result = subprocess.run(["tasklist", "/FI", "IMENAME eq aria2c.exe"], capture_output=True, text=True)
        return "aria2c.exe" in result.stdout
    else:
        result = subprocess.run(["ps", "-ef"], capture_output=True, text=True)
        return "aria2c" in result.stdout


# 停止aria2c的rpc
def stop_aria2c_rpc():
    if platform.system() == "Windows":
        subprocess.Popen(["taskkill", "/F", "/IM", "aria2c.exe"])
    else:
        subprocess.Popen(["pkill", "aria2c"])
if __name__ == "__main__":
    auto_download_aria2c()