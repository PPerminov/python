from tkinter import *


class food:
    def __init__(self, name, price, includes=[], restrictions=None):
        self.name = name
        self.price = price
        # if not includes:
        self.includes = includes
        self.restrictions = restrictions

    def getFullPrice(self):
        positionOne = self.price
        for item in self.includes:
            positionOne += item.getFullPrice()
        return positionOne

    #@property
    def getIncludesNames(self):
        names = []
        for item in self.includes:
            names.append(item.name)  # getIncludesNames()
        return names

    #@property.set
    def setIncludes(self, whatIn):
        try:
            self.includes.append(whatIn)
        except:
            return False
        return True

    #@property.
    def delIncludes(self, trash):
        for item in self.includes:
            if item == trash:
                self.includes.remove(item)


class dinner:
    def __init__(self):
        self.water = food('water', 20)
        self.milk = food('milk', 10)
        self.milk_penka = food('milk_penka', 0, [milk])
        self.syrop = food('syrop', 5)
        self.sugar = food('sugar', 3)
        self.ham = food('ham', 15)
        self.cheese = food('cheese', 10)
        self.jam = food('jam', 7)
        self.bread = food('bread', 10)
        self.bun = food('bun', 15)
        self.crisps = food('crisps', 34)
        self.coockies = food('coockies', 29)
        self.espresso = food('espresso', 50)
        self.latte = food('latte', 0, [milk, espresso])
        self.cappuchino = food('cappuchino', 0, [espresso, milk, milk_penka])
        self.green_tea = food('green_tea', 25)
        self.black_tea = food('black_tea', 25)


# def GUIComposer():
#
#     def msg():
#         message = ch1.get()
#         label.config(text=message)
#     app = Tk()
#
#     rb = []
#     ch1 = IntVar()
#     rb.append(Radiobutton(app, text="bt1", variable=ch1, value=12, command=msg))
#     rb.append(Radiobutton(app, text="bt1", variable=ch1, value=13, command=msg))
#     rb.append(Radiobutton(app, text="bt1", variable=ch1, value=14, command=msg))
#     for item in rb:
#         item.pack(anchor='w')
#     label = Label(app)
#     label.pack()
#     return app
#
#
# def f1():
#     print(cappuchino.getIncludesNames())
#     cappuchino.setIncludes(latte)
#     print(cappuchino.getIncludesNames())
#     print(cappuchino.getFullPrice())
#     cappuchino.delIncludes(latte)
#     print(cappuchino.getIncludesNames())
#     print(cappuchino.getFullPrice())
#
#
# GUIComposer().mainloop()

class podnos
