import os
import shutil #library for copy file command

path = "C:\\Users\\Oat\\Documents\\Project\\RenameFile\\Example\\"
outputpath = "C:\\Users\\Oat\\Documents\\Project\\RenameFile\\Output\\"

shutil.rmtree(outputpath)                               #remove non-empty directory
os.mkdir(outputpath)

print(f"Before Renaming: {os.listdir(path)}")
for i in os.listdir(path):
    print(i)
    shutil.copyfile(path+i, outputpath+i)               #copy file from example to output
    os.rename(outputpath+i, outputpath+i+'.txt')        #rename file by adding .txt
#print(f"After Renaming: {os.listdir(path)}")