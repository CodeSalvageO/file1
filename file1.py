from tkinter import *
from tkinter import messagebox
import math
import threading
import os
root = Tk()
canvas=(root, width=700, height=700 bg="green")
canvas.pack(expand=YES, fill=BOTH)
c = canvas.create_rectangle(root, 0, 0, 50, 50)
canvas.move(c, 50, 50)
def wow():
  canvas.move(c, 50, 0)
b = Button(root, text="Move Up", command=wow)
b.pack()
root.mainloop()
