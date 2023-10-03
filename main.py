import tkinter as tk
from config.config import *
from key.generator import *
from coder.read import *
from coder.write import *

global outputTextValue
outputTextValue = ""

root = tk.Tk()
root.title("PySecret")
root.resizable(False, False)
root.geometry('500x500')
root.eval("tk::PlaceWindow . center")


mainFrame = tk.Frame(root)
readFrame = tk.Frame(root)
writeFrame = tk.Frame(root)
settingsFrame = tk.Frame(root)

frame_List = [mainFrame,readFrame,writeFrame,settingsFrame]

def readText():
    rText = inputText.get()
    rKey = inputKey.get()

    outputLabel.pack()
    outputTextValue = str(read(rText,rKey))
    outputText = tk.Label(readFrame,text=outputTextValue)
    outputText.pack()

def writeText():
    wText = inputText.get()
    wKey = inputKey.get()

    outputLabel.pack()
    outputTextValue = str(write(wText,wKey))
    outputText = tk.Label(writeFrame,text=outputTextValue)
    outputText.pack()

def gotoFrame(newFrame):
    for frame in frame_List:
        frame.pack_forget()
    newFrame.pack()

def SaveSettings():
    gotoFrame(mainFrame)

#--- Main Frame ---
settingsButton = tk.Button(mainFrame, text="⚙️", command=lambda: gotoFrame(settingsFrame))
settingsButton.pack(pady=10, padx=10, anchor=tk.NE)

Welcome_label = tk.Label(mainFrame, text="PySecret", font=("arial", 25))
Welcome_label.pack(pady=10, padx=10, anchor=tk.NE)

readButton = tk.Button(mainFrame, text="read", command=lambda: gotoFrame(readFrame))
readButton.pack(pady=10)

writeButton = tk.Button(mainFrame, text="write", command=lambda: gotoFrame(writeFrame))
writeButton.pack(pady=10)

#--- Settings Frame ---
backButton = tk.Button(settingsFrame,text="back",command=lambda: gotoFrame(mainFrame))
backButton.pack(pady=10)

StKeyText = tk.Text(settingsFrame,text="enter standart Key:")
StKeyText.pack(pady=10)

StandartKey = tk.Entry(settingsFrame)
StandartKey.pack()


submitSettingsButton = tk.Button(settingsFrame)

#--- read Frame ---
backButton = tk.Button(readFrame,text="back",command=lambda: gotoFrame(mainFrame))
backButton.pack(pady=10)

InputTextText = tk.Label(readFrame,text="Enter Text:",font=("arial", 10))
InputTextText.pack(pady=10)

inputText = tk.Entry(readFrame)
inputText.pack(pady=5)


KeyText = tk.Label(readFrame,text="Enter Key:",font=("arial", 10))
KeyText.pack(pady=20)

inputKey = tk.Entry(readFrame)
inputKey.pack(pady=5)


submitButton = tk.Button(readFrame,text="submit",command=lambda: readText())
submitButton.pack(pady=5)

outputLabel = tk.Label(readFrame, text="Output" ,font=("arial", 20))
outputLabel.pack_forget()

outputText = tk.Label(readFrame,text=outputTextValue)
outputText.pack_forget()

#--- write Frame ---
backButton = tk.Button(writeFrame,text="back",command=lambda: gotoFrame(mainFrame))
backButton.pack(pady=10)

InputTextText = tk.Label(writeFrame,text="Enter Text:",font=("arial", 10))
InputTextText.pack(pady=10)

inputText = tk.Entry(writeFrame)
inputText.pack(pady=5)

submitButton = tk.Button(writeFrame,text="submit",command=lambda: writeText())
submitButton.pack(pady=5)

outputLabel = tk.Label(writeFrame, text="Output" ,font=("arial", 20))
outputLabel.pack_forget()

outputText = tk.Label(writeFrame,text=outputTextValue)
outputText.pack_forget()

ButtonList = [backButton,settingsButton]
ExtraList = [Welcome_label]
mainFrame.pack()
root.mainloop()