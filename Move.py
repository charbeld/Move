
import shutil, os
from pathlib import Path

main = os.getcwd()
pngs = []
sub = main + '\\Photos\\'

for i in os.listdir(main):
    if i.endswith('.png') or i.endswith('.jpeg') or i.endswith('.gif') or i.endswith('.jpg'):
        if os.path.exists(sub):
            pass
        else:
            os.mkdir(sub)

        shutil.move(main + '\\' + i , sub)
