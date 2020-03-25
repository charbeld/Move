#Move all png files into one folder called photos.
import shutil, os
from pathlib import Path

#input path of the folder you want to organize
main = os.getcwd()
pngs = [] #creates a list
sub = main + '\\Photos\\'

for i in os.listdir(main):
    if i.endswith('.png'):
        if os.path.exists(sub):
            pass
        else:
            os.mkdir(sub)

        shutil.move(main + '\\' + i , sub)
