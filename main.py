import tkinter as tk
from config.config import *
from key.generator import *
from coder.read import *
from coder.write import *

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


def gotoFrame(newFrame):
    for frame in frame_List:
        frame.pack_forget()
    newFrame.pack()

#--- Main Frame ---
settingsButton = tk.Button(mainFrame,text="Settings",command=lambda: gotoFrame(settingsFrame))
settingsButton.pack()

#--- Settings Frame ---
backButton = tk.Button(settingsFrame,text="back",command=lambda: gotoFrame(mainFrame))
backButton.pack()

#--- read Frame ---
backButton = tk.Button(settingsFrame,text="back",command=lambda: gotoFrame(readFrame))
backButton.pack()

#--- write Frame ---
backButton = tk.Button(settingsFrame,text="back",command=lambda: gotoFrame(writeFrame))
backButton.pack()

ButtonList = [backButton,settingsButton]
ExtraList = []
mainFrame.pack()
root.mainloop()