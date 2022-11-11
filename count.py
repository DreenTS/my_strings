import os


if __name__ == '__main__':
    files_amount = 0
    folders = os.listdir(path=".")
    for folder in folders:
        if os.path.isdir(folder) and '.' not in folder:
            files_amount += len(os.listdir(path=f"./{folder}"))
    print(f'{files_amount = }')