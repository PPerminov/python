#!/usr/bin/python3

from tkinter import *
from time import *
from random import *



def window_deleted():
    print('Окно закрыто')
    root.quit() # явное указание на выход из программы




root=Tk()
root.title('Пример приложения')
root.geometry('500x400') # ширина=500, высота=400, x=300, y=200
root.protocol('WM_DELETE_WINDOW', window_deleted) # обработчик закрытия окна
root.resizable(True, True) # размер окна может быть изменён только по горизонтали

raw1=Toplevel()
raw1.transient(root)
raw1.title("Holy crap!!!!")
# raw1.withdraw()
raw1.protocol('WM_DELETE_WINDOW',window_deleted)
button1=Button(root,text='ok',width=25,height=5,bg='black',fg='red',font='arial 14')
button1.pack()
label1=Label(root,text='ok',width=100,height=5,bg='black',fg='red',font='arial 14')
label1.pack()
entry1=Entry(root,bd=12,show='*')
entry1.pack()
text1=Text(root,height=7,width=7,font='Arial 14',wrap=WORD)
text1.pack()
listbox1=Listbox(root,height=5,width=15,selectmode=EXTENDED)
listbox2=Listbox(root,height=5,width=15,selectmode=SINGLE)
list1=[u"Москва",u"Санкт-Петербург",u"Саратов",u"Омск"]
list2=[u"Канберра",u"Сидней",u"Мельбурн",u"Аделаида"]
for i in list1:
    listbox1.insert(END,i)
for i in list2:
    listbox2.insert(END,i)
listbox1.pack()
listbox2.pack()
root.mainloop()
