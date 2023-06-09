import os, shutil



def organize(file_list, path):
    for file in file_list:
        if os.path.isfile(f"{path}/{file}"):
            file_name, extension = os.path.splitext(file)
            extension = extension[1:]
            if os.path.exists(f'{path}/{extension}'):
                shutil.move(f'{path}/{file}', f'{path}/{extension}/{file}')
            else:
                os.makedirs(f'{path}/{extension}')
                shutil.move(f'{path}/{file}', f'{path}/{extension}/{file}')
