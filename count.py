import os


if __name__ == '__main__':
    ok_files_amount = 0
    folders = os.listdir(path=".")
    for folder in folders:
        if os.path.isdir(folder) and '.' not in folder and folder != 'LOST':
            ok_files_amount += len(os.listdir(path=f"./{folder}"))
    lost_files_amount = 0
    folders = os.listdir(path="LOST")
    for folder in folders:
        if os.path.isdir(f"LOST/{folder}"):
            lost_files_amount += len(os.listdir(path=f"LOST/{folder}"))
    print(f'TOTAL = {ok_files_amount + lost_files_amount}')
    print(f'{ok_files_amount = }')
    print(f'{lost_files_amount = }')
