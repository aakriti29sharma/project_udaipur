from tkinter import *
import os
from PIL import ImageTk,Image
import tkinter as Tk
 

class App:
    def motions(self):
        import Motion_detect
    def emotions(self):
        import emotion   
    def close_window (self): 
     root.destroy()   
    def __init__(self, master):
        master.minsize(width=110, height=110)
        self.frame = Frame(master)
        self.b = Button(self.frame, text = 'Motion Module',bg="blue",width=10,height=5, command = self.motions)
        
        self.b.pack(side=LEFT)
        self.button = Button(self.frame, 
                         text="Exit Module", fg="red",
                         command=self.close_window)
        self.button.pack(side=RIGHT)
        self.c = Button(self.frame, text = 'Emotions',bg="yellow",width=10,height=5, command = self.emotions)
        self.c.pack(side=LEFT)

        self.frame.grid()
     



root = Tk.Tk()
background_image=Tk.PhotoImage(file="motion.gif")
background_label = Tk.Label(root, image=background_image)
background_label.place(x=10, y=0, relwidth=1, relheight=1)
root.wm_geometry("600x400+40+60")
root.title('Motion Detector')

app = App(root)
root.mainloop()
    
