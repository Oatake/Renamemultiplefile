import os

path = "C:\\Users\\Oat\\Documents\\Project\\RenameFile\\Example\\"
outputpath = "C:\\Users\\Oat\\Documents\\Project\\RenameFile\\Output\\"

print("Hello world")
print(f"Before Renaming: {os.listdir(path)}")
for i in os.listdir(path):
    print(i)
    os.rename(path+i, path+i+'.txt')
#print(f"After Renaming: {os.listdir(path)}")

