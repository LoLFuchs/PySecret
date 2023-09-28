import tkinter as tk
import sys
from config.config import *

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


mainFrame.pack()
root.mainloop()