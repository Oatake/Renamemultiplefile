import os
import shutil  # library for copy file command
import tkinter
from tkinter import Frame, messagebox
from tkinter.constants import X,LEFT,TRUE,RIGHT

def CopyNRename(inputPath, outputPath):
    inputPath=inputPath+"\\"
    outputPath=outputPath+"\\"
    for i in os.listdir(inputPath):
        print(i)
        shutil.copyfile(inputPath+i, outputPath+i)              #copy file from example to output
        os.rename(outputPath+i, outputPath+i+'.txt')            #rename file by adding .txt

def Rename(inputPath, outputPath):
    inputPath=inputPath+"\\"
    outputPath=outputPath+"\\"
    for i in os.listdir(inputPath):
        os.rename(outputPath+i, outputPath+i+'.txt')            #rename file by adding .txt

def FuncButtonRename():
    inputPath = et1.get()
    outputPath = et2.get()
    if (inputPath==outputPath):
        try : 
            Rename(inputPath, outputPath)
            messagebox.showinfo("Rename Process", "Successful" )
            os.startfile(outputPath)
        except OSError as e:
            messagebox.showerror("Rename Process", e.strerror )
    else:
        try : 
            CopyNRename(inputPath, outputPath)
            messagebox.showinfo("Rename Process", "Successful" )
            os.startfile(outputPath)
        except OSError as e:
            messagebox.showerror("Rename Process", e.strerror )
    
# GUI section
GUI_Renamefile = tkinter.Tk()                           
GUI_Renamefile.title("Boyzilla")   
GUI_Renamefile.geometry("400x100+300+300")                  #dimension "widthxheight+x+y" x&y is grid when open gui

#Frame1
frame1=Frame(GUI_Renamefile)    
frame1.pack(fill=X)     

lbl1 = tkinter.Label(frame1,text="Input Path",width=10)     #Path of your input file
lbl1.pack(side=LEFT,padx=5,pady=5)

et1 = tkinter.Entry(frame1)
et1.pack(fill=X,expand=TRUE)

#Frame2 
frame2=Frame(GUI_Renamefile)    
frame2.pack(fill=X)     

lbl2 = tkinter.Label(frame2,text="Output Path",width=10)    #Where to store output file
lbl2.pack(side=LEFT,padx=5,pady=5)

et2 = tkinter.Entry(frame2)
et2.pack(fill=X,expand=TRUE)

#Frame3
frame3=Frame(GUI_Renamefile)    
frame3.pack(fill=X)     

B_Rename = tkinter.Button(frame3,text="Rename", command=FuncButtonRename)
B_Rename.pack(side=RIGHT, padx=5,pady=5)
GUI_Renamefile.mainloop()
