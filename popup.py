import tkinter as tk
from tkinter import messagebox
import time

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief= tk.FLAT,
            bd=1.5,
            highlightthickness=1,
            padx=8,
            pady=5,
            font=("Times New Roman", 12),
            foreground= "black",
            background= "green",
        )

        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)
        
    def on_hover(self, event):
        self.config(background= "lightblue", text="dialling....", font=("Arial", 10))
    def on_leave(self, event):
        self.config(background= "red", font=("Wingdings", 12), text= "THE TAIL OF HELL TAKES CRAWL")
    


def enter(event):
    ans= str(e1.get())
    if ans == "Call Declined!":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("But nobody came.")
    else:
        print("LOCKED")

root= tk.Tk()
root.geometry("500x200")


def msg():
    print("Call Declined!")
root.title("#1 RATED SALESMAN 1997")

custom_button= CustomButton(root, text= "Cl1Ck H3rE!!!", command=msg)
custom_button.pack(pady=15)


leave = tk.Button(root, text= "LEAVE?", command=root.destroy)
leave.pack(pady= 15)

tk.Label(root, text="Enter what you must:").pack()

e1= tk.Entry(root)

e1.bind("<Return>", enter)
e1.pack(pady= 15)


root.mainloop()
