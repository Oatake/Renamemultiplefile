import os
import shutil #library for copy file command

path = "C:\\Users\\Oat\\Documents\\Project\\RenameFile\\Example\\"
outputpath = "C:\\Users\\Oat\\Documents\\Project\\RenameFile\\Output\\"

try :
    shutil.rmtree(outputpath)                               #remove non-empty directory
except OSError as e:
    print("Error cannot remove directory : %s : %s" % (outputpath, e.strerror))
# try :    
#     os.mkdir(outputpath)    
# except OSError as e:                                #create directory to be output file directory
#     print("Error cannot create directory : %s : %s" % (outputpath, e.strerror))


# shutil.rmtree(outputpath)   
os.mkdir(outputpath)                                #remove non-empty directory

print(f"Before Renaming: {os.listdir(path)}")
for i in os.listdir(path):
    print(i)
    shutil.copyfile(path+i, outputpath+i)               #copy file from example to output
    os.rename(outputpath+i, outputpath+i+'.txt')        #rename file by adding .txt
#print(f"After Renaming: {os.listdir(path)}")