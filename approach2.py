import os
import shutil


IMAGE = ('.jpg', '.png',)
AUDIO = ('.mp3',)
VIDEO = ('.mp4','.mov')
ZIP = ('.rar','.zip', '.tar', '.tar.gz')
DOC = ('.docx','.txt', '.doc', '.pdf')



def organize2(file_list, path):
    
    os.makedirs(f'{path}/IMAGEs')
    os.makedirs(f'{path}/AUDIOs')
    os.makedirs(f'{path}/VIDEOs')
    os.makedirs(f'{path}/ZIP')
    os.makedirs(f'{path}/DOCs')
    
    for file in file_list:
        if os.path.isfile(f"{path}/{file}"):
            if file.endswith(IMAGE):
                shutil.move(f"{path}/{file}", f"{path}/IMAGEs/{file}")
                
            if file.endswith(AUDIO):
                shutil.move(f"{path}/{file}", f"{path}/AUDIOs/{file}")
    
            if file.endswith(VIDEO):
                shutil.move(f"{path}/{file}", f"{path}/VIDEOs/{file}")
                
            if file.endswith(ZIP):
                shutil.move(f"{path}/{file}", f"{path}/ZIP/{file}")
            
            if file.endswith(DOC):
                shutil.move(f"{path}/{file}", f"{path}/DOCs/{file}")
