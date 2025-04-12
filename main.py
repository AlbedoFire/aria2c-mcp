def main():
    print("Hello from aria2c-mcp!")
    print("check if have aria2c")
    from utils import check_aria2c
    if not check_aria2c():
        print("not found aria2c, download it")
        from utils import download_aria2c
        download_aria2c()
        if not check_aria2c():
            print("download failed")
            exit(1)
        print("download success")
    print("check success")
    


if __name__ == "__main__":
    main()
