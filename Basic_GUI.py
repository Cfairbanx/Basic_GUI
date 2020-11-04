#
#Python Version         3.8.5
#
#Author                 Casey Fairbanks
#
#Purpose                Create a GUI that allows a user to enter text and have
#                       this text displayed in the browser.
#
#
#import needed modules
import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True,height=True)
        self.master.geometry('{}x{}'.format(500,200))
        self.master.title('Text Creator')
        self.master.config(bg='lightgray')

        self.varEnter_text = StringVar()

#label for text Box
        self.lblEnter_text = Label(self.master,text='Enter Text',font=('Helvetica',16), fg='black', bg='lightgray')
        self.lblEnter_text.grid(row=0,column=1, padx=(30,0), pady=(30,0))

#text box
        self.txtEnter_text = Entry(self.master,text=self.varEnter_text, font=('Helvetica', 16), fg='black', bg='white')
        self.txtEnter_text.grid(row=1,rowspan=2,column=0,columnspan=3, padx=(30,0),pady=(30,0))

#buttons
        self.btnCreate = Button(self.master, text='Create', width=10, height=1, command=self.create)
        self.btnCreate.grid(row=4, column=0,padx=(30,0), pady=(30,0), sticky=NE)

        self.btnClose = Button(self.master, text='Close', width=10, height=1, command=self.close)
        self.btnClose.grid(row=4, column=2, padx=(30,0), pady=(30,0), sticky=NE)

#Button Functionality
    def create(self):
        et = self.varEnter_text.get()
        f = open("myfile.html", "w")
        f.write("{}".format(et))
        url = "file:///C:/python_Projects/Basic_GUI/myfile.html"
        webbrowser.open(url,new=2,autoraise=True)


    def close(self):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

