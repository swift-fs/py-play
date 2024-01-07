from pathlib import Path


def main():
    # 当前工作目录
    cwd = Path.cwd()
    # 当前文件所在目录
    # cwd = Path(__file__).parent
    print(f"cwd:{cwd}")
    # 创建文件夹
    new_dir = cwd.joinpath("new_dir")
    if not new_dir.exists():
        new_dir.mkdir(mode=777, parents=True)

    print(f"new_dir:{new_dir}")
    # 重命名
    new_dir.rename("new_dir2")
    # 删除文件夹
    # new_dir.rmdir()
    # 遍历文件夹
    src_dir = Path(__file__).parent
    print(f"src_dir:{src_dir}")
    for item in src_dir.rglob("*"):
        if item.is_dir():
            print(f"dir:{item}")


if __name__ == "__main__":
    main()
