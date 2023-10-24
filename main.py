import tkinter as tk
import pyperclip
from tkinter import filedialog
from tkinter import messagebox
from config.config import *
from key.generator import *
from coder.read import *
from coder.write import *
from PIL import Image, ImageTk

global outputTextValue
outputTextValue = ""

global selectedType
selectedType = ""

Mode = "None"
switch_value = not get_default_mode()



root = tk.Tk()
root.title("PySecret")
root.resizable(False, False)
root.geometry('500x500')
root.eval("tk::PlaceWindow . center")

#set Icon
iconDir = os.getcwd() + r"\assets\Icon.png"
ico = Image.open(iconDir)
ico = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, ico)


light_open = Image.open("assets/light_mode.png")
light = ImageTk.PhotoImage(light_open)

dark_open = Image.open("assets/dark_mode.png")
dark = ImageTk.PhotoImage(dark_open)

mainFrame = tk.Frame(root)
workFrame = tk.Frame(root)
settingsFrame = tk.Frame(root)

frame_List = [mainFrame,workFrame,settingsFrame]

def selectType(Type):
    Text = str(inputText.get())

    if get_default_dir() != None and get_default_dir() != "":
        Key = get_default_dir()
    elif str(inputKey.get()) != "" and inputKey.get() != None:
        Key = str(inputKey.get())
    else: 
        messagebox.showerror(title="NO KEY", message="EMPTY KEY, PLEASE ENTER A KEY")
    
    if Text != "":
        if Type == "write":
            outputTextValue = str(write(Text,Key))
        elif Type == "read":
            outputTextValue = str(read(Text,Key))
        else: 
            messagebox.showerror(title="ERROR", message="ERROR")
            exit()    
        
        
        #outputText = tk.Label(workFrame,text=outputTextValue)
        
        if outputTextValue == "WRONG KEY":
            messagebox.showerror(title="WRONG KEY", message="the key, you took is not correct, please check it")
        else:
            outputText.config(text=outputTextValue)
            copyOutput.config(text="copy to clipboard")
            
            outputLabel.pack()
            outputText.pack(pady=10)
            copyOutput.pack(pady=10)
            
            if switch_value == False:
                outputText.config(bg="#26242f", fg="#ffffff")
            else:
                outputText.config(bg="white", fg="#000000")
    else:
        messagebox.showerror(title="NO TEXT", message="EMPTY TEXT, PLEASE ENTER A TEXT")
    
def clearDefKey():
    clear_default_dir()
    StandartKey.delete(0,tk.END)

def SaveSettings():
    update_default_mode(switch_value)
    update_default_dir(StandartKey.get())
    gotoFrame(mainFrame)

def toggle():
  
    global switch_value
    if switch_value == True :
        switch.config(image=light,bg="#26242f",
                      activebackground="#26242f")

        for frame in frame_List:
            frame.config(bg="#26242f")

        for button in ButtonList:
            button.config(bg="#26242f", fg="#ffffff", activebackground="#26242f", activeforeground="#ffffff")

        for extra in ExtraList:
            extra.config(bg="#26242f", fg="#ffffff")
        
        root.config(bg="#26242f")
        
        switch_value = False
  
    else:
        switch.config(image=dark,bg="white", 
                      activebackground="white")
          
        for frame in frame_List:
            frame.config(bg="white")

        for button in ButtonList:
            button.config(bg="white", fg="#000000", activebackground="white", activeforeground="#000000")

        for extra in ExtraList:
            extra.config(bg="white", fg="#000000")
        
        root.config(bg="white")

        switch_value = True

def insertKey(key):
    if get_default_dir() != None and get_default_dir() != "":
        StandartKey.insert(0,key)

def newDefKey():
    clearDefKey()
    insertKey(generate())
    
def gotoFrame(newFrame,Type="",inputKey=None):

    for frame in frame_List:
        frame.pack_forget()
    newFrame.pack()

    global selectedType

    if Type == "write":
        selectedType = "write"
    elif Type == "read":
        selectedType = "read"

    if newFrame == mainFrame:
        inputKey = tk.Entry(workFrame)
        inputKey.delete(0,tk.END)
        inputText.delete(0,tk.END)

        outputLabel.pack_forget()
        outputText.pack_forget()
        copyOutput.pack_forget()
    elif newFrame == workFrame:
        if get_default_dir() != None and get_default_dir() != "":
            KeyText.pack_forget()
            inputKey.pack_forget()
        else:
            submitButton.pack_forget()
            KeyText.pack(pady=20)
            inputKey.pack(pady=5)
            submitButton.pack(pady=5)

def copyToClipboard():
    print(outputText.cget("text"))
    pyperclip.copy(outputText.cget("text"))
    copyOutput.configure(text="✅")
    copyOutput.pack()

#               ---------- TKINTER ----------


#                   --- main frame ---


settingsButton = tk.Button(mainFrame, text="⚙️", command=lambda: gotoFrame(settingsFrame))

settingsButton.pack(pady=10, padx=10, anchor=tk.NE)

Welcome_label = tk.Label(mainFrame, text="PySecret", font=("arial", 25))
Welcome_label.pack(pady=10, padx=10, anchor=tk.NE)

img = Image.open(iconDir)
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)
picture = tk.Label(mainFrame, image=img)
picture.pack(pady=10)

readButton = tk.Button(mainFrame, text="read", command=lambda: gotoFrame(workFrame,"read",inputKey))
readButton.pack(pady=10)

writeButton = tk.Button(mainFrame, text="write", command=lambda: gotoFrame(workFrame,"write",inputKey))
writeButton.pack(pady=10)


#               --- settings frame ---


setbackButton = tk.Button(settingsFrame,text="back",command=lambda: gotoFrame(mainFrame))
setbackButton.grid(column=0,row=0,pady=10)

StKeyText = tk.Label(settingsFrame,text="enter standart Key:")
StKeyText.grid(column=0,row=1,pady=10)

StandartKey = tk.Entry(settingsFrame,text="test")
StandartKey.grid(column=0,row=2,ipadx=100)

delDefKey = tk.Button(settingsFrame,text="clear",command=lambda:clearDefKey())
delDefKey.grid(column=1,row=2)

reDefKey = tk.Button(settingsFrame,text="renew",command=lambda:newDefKey())
reDefKey.grid(column=2,row=2)

switch = tk.Button(settingsFrame, bd=0, bg="white",text="Light Mode", activebackground="white", command=toggle)
switch.grid(column=0,row=3,pady=100)

submitSettingsButton = tk.Button(settingsFrame,text="submit",command=lambda: SaveSettings())
submitSettingsButton.grid(column=0,row=4)

VersionLabel = tk.Label(settingsFrame, text="V.Beta")
VersionLabel.grid(column=0,row=5,pady=60)


#               --- work frame ---


backButton = tk.Button(workFrame,text="back",command=lambda: gotoFrame(mainFrame))
backButton.pack(pady=10)

InputTextText = tk.Label(workFrame,text="Enter Text:",font=("arial", 10))
InputTextText.pack(pady=10)

inputText = tk.Entry(workFrame)
inputText.pack(pady=5)

KeyText = tk.Label(workFrame,text="Enter Key:",font=("arial", 10))
KeyText.pack(pady=20)

inputKey = tk.Entry(workFrame)
inputKey.pack(pady=5)

submitButton = tk.Button(workFrame,text="submit",command=lambda: selectType(selectedType))
submitButton.pack(pady=5)

outputLabel = tk.Label(workFrame, text="Output" ,font=("arial", 20))
outputLabel.pack_forget()

outputText = tk.Label(workFrame,text=outputTextValue)
outputText.pack_forget()

copyOutput = tk.Button(workFrame,text="copy to clipboard",command=lambda: copyToClipboard())
copyOutput.pack_forget()

ButtonList = [setbackButton,backButton,settingsButton,readButton,writeButton,submitButton,delDefKey,submitSettingsButton,reDefKey,copyOutput]
ExtraList = [Welcome_label,StKeyText,StandartKey,InputTextText,inputText,KeyText,inputKey,outputLabel,outputText,picture,VersionLabel]


mainFrame.pack()
toggle()
insertKey(get_default_dir())
root.mainloop()