from os import close
from tkinter import *
from tkinter import filedialog,messagebox
import track

FotaGui = Tk()
FotaGui.geometry('600x600')

def file_path():
        
    global filepath
    filepath = StringVar()
    #Fetch the file path of the mp4 file browsed.
    if(filepath == ""):
        filepath = filedialog.askopenfilename(title = "select a file", filetypes = [("mp4 files", "*.mp4")])
    else:
        filepath = filedialog.askopenfilename( initialdir=filepath, title = "select a file", filetypes = [("mp4 files", "*.mp4")])
        filepathlabel.config(text=filepath)

#Morris Water Maze
def MWM():
        
    #Validation of entry fields, if left empty.
    if filepath == "":
        messagebox.showinfo('Info','Please select a video')
    else:
        exec("track")



Browsebutton = Button(FotaGui,width = 18,text= "Browse",command = file_path)
Browsebutton.pack()

MWMbutton = Button(FotaGui,width = 18,text="Morris Water Maze Test",command = MWM)
MWMbutton.pack()

filepathlabel = Label(FotaGui,text = "mp4 file path:",font = ('Times 10'))
filepathlabel.pack()

FotaGui.mainloop()
