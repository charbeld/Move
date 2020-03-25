
import shutil, os
from pathlib import Path

main = os.getcwd()
Folders = ['\\Photos','\\Movies','\\Documents','\\Compressed','\\Programs','\\Music']


for i in os.listdir(main):
    if i.endswith('.jpg') or i.endswith('.png') :
        if os.path.exists(main + Folders[0]):
            pass
        else:
            os.mkdir(main + Folders[0])

        shutil.move(main + '\\' + i , main + Folders[0])

for i in os.listdir(main):
    if i.endswith('.mp4'):
        if os.path.exists(main + Folders[1]):
            pass
        else:
            os.mkdir(main + Folders[1])

        shutil.move(main + '\\' + i , main + Folders[1])

for i in os.listdir(main):
    if i.endswith('.pdf'):
        if os.path.exists(main + Folders[2]):
            pass
        else:
            os.mkdir(main + Folders[2])

        shutil.move(main + '\\' + i , main + Folders[2])

for i in os.listdir(main):
    if i.endswith('.zip') or i.endswith('.rar'):
        if os.path.exists(main + Folders[3]):
            pass
        else:
            os.mkdir(main + Folders[3])

        shutil.move(main + '\\' + i , main + Folders[3])

for i in os.listdir(main):
    if i.endswith('.msi') or i.endswith('.exe'):
        if os.path.exists(main + Folders[4]):
            pass
        else:
            os.mkdir(main + Folders[4])

        shutil.move(main + '\\' + i , main + Folders[4])

for i in os.listdir(main):
    if i.endswith('.mp3') or i.endswith('.wma'):
        if os.path.exists(main + Folders[5]):
            pass
        else:
            os.mkdir(main + Folders[5])

        shutil.move(main + '\\' + i , main + Folders[5])
