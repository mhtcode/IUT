import os
import shutil

srcpath = "E:\\learning\\Git.ir\\mosh docker\\104-Code with Mosh - The Ultimate Docker Course 2021-4-git.ir\\Code with Mosh - The Ultimate Docker Course 2021-5 Subtitle-git.ir"
destpath = "E:\\learning\\Git.ir\\mosh docker\\104-Code with Mosh - The Ultimate Docker Course 2021-4-git.ir"

listofdirinsrc = []

for file in os.listdir(srcpath):
    listofdirinsrc.append(file)

for path in listofdirinsrc:
    for file in os.listdir(srcpath+f'//{path}'):
        src = srcpath + f'//{path}' + f'//{file}'
        print(src)
        dest = destpath + f'//{path}'
        shutil.move(src, dest)
        print(file, "moved")
