from utils import *
from turtle import st


def main():
    print("Hello from aria2c-mcp!")
    print("check if have aria2c")
    if not check_aria2c():
        print("not found aria2c, download it")
        download_aria2c()
        if not check_aria2c():
            print("download failed")
            exit(1)
        print("download success")
    print("check success")
    create_default_config()

    if not check_aria2c_rpc():
        print("not found aria2c-rpc, start it")
        start_aria2c_rpc()
    else:
        print("found aria2c-rpc, stop it")
        stop_aria2c_rpc()
        start_aria2c_rpc()




if __name__ == "__main__":
    main()
