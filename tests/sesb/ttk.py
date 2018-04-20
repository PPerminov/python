from tkinter import *

def d1():
    root = Tk()

    w = Label(root, text="Hello, world!")
    w.pack()

    root.mainloop()


class App:

    def __init__(self, master):

        frame1 = Frame(master)
        frame2 = Frame(master)
        frame1.pack()
        frame2.pack()

        self.button = Button(
            frame1, text="QUIT", fg="red"
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame1, text="Hello", command=self.say_hi)
        self.hi_there1 = Button(frame2, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
        self.hi_there1.pack(side=RIGHT)

    def say_hi(self):
        print ("hi there, everyone!")

def d2():
    root = Tk()

    app = App(root)

    root.mainloop()
    root.destroy() # optional; see description below
    
d2().mainloop()