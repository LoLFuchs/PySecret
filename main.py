import tkinter as tk
from config.config import *
from key.generator import *
from coder.read import *
from coder.write import *

global outputTextValue
outputTextValue = ""

global selectedType
selectedType = ""

root = tk.Tk()
root.title("PySecret")
root.resizable(False, False)
root.geometry('500x500')
root.eval("tk::PlaceWindow . center")


mainFrame = tk.Frame(root)
workFrame = tk.Frame(root)
settingsFrame = tk.Frame(root)

frame_List = [mainFrame,workFrame,settingsFrame]

def selectType(Type):       
    Text = inputText.get()
    Key = inputKey.get()

    if Type == write:

        outputTextValue = str(write(Text,Key))
    else:
        outputTextValue = str(read(Text,Key))
    
    outputText = tk.Label(workFrame,text=outputTextValue)
    outputLabel.pack()
    outputText.pack()

def gotoFrame(newFrame,*Type):
    for frame in frame_List:
        frame.pack_forget()

    newFrame.pack()

    if Type == "write":
        selectedType = "write"
    elif Type == "read":
        selectedType = "read"
        

def SaveSettings():
    gotoFrame(mainFrame)


#--- Main Frame ---


settingsButton = tk.Button(mainFrame, text="⚙️", command=lambda: gotoFrame(settingsFrame))
settingsButton.pack(pady=10, padx=10, anchor=tk.NE)

Welcome_label = tk.Label(mainFrame, text="PySecret", font=("arial", 25))
Welcome_label.pack(pady=10, padx=10, anchor=tk.NE)

readButton = tk.Button(mainFrame, text="read", command=lambda: gotoFrame(workFrame,"read"))
readButton.pack(pady=10)

writeButton = tk.Button(mainFrame, text="write", command=lambda: gotoFrame(workFrame,"write"))
writeButton.pack(pady=10)


#--- Settings Frame ---


backButton = tk.Button(settingsFrame,text="back",command=lambda: gotoFrame(mainFrame))
backButton.pack(pady=10)

StKeyText = tk.Label(settingsFrame,text="enter standart Key:")
StKeyText.pack(pady=10)

StandartKey = tk.Entry(settingsFrame)
StandartKey.pack()


submitSettingsButton = tk.Button(settingsFrame)


#--- work Frame ---
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

ButtonList = [backButton,settingsButton]
ExtraList = [Welcome_label]
mainFrame.pack()
root.mainloop()