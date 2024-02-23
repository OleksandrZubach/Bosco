import tkinter.messagebox
from tkinter import messagebox
import random
import tkinter as tk
from tkinter import *

root = Tk()

# root.geometry('300x300')
# root['bg'] = 'black'
# root.resizable(width=False, height=False)
# root.attributes('-topmost', True)
# sprobu = 1



def zanovo():
    print('HELLO WORD')
    answer = tkinter.messagebox.askyesno(title='ХАХАХХХХАХАХХАХА', message='Хочеш зіграти знову чувак ??')
    if answer == True:
        pochatok_gru()
    else:
        root.quit()

def vgaday_chuslo():
    global but7
    global sprobu
    # sprobu += 1
    try:
        kilkist_sprob = 6
        chuslo_vgadayte = int(entry3.get())

        if chuslo_vgadayte == d :
            messagebox.showinfo(title='Кінець', message='Молодець чувак')
        if chuslo_vgadayte > d:
            messagebox.showinfo(title='Кінець', message='Менше чувак')
            root.title(sprobu)
            sprobu+=1

        if chuslo_vgadayte < d:
            messagebox.showinfo(title='Кінець', message='Більше чувае чувак')
            root.title(sprobu)
            sprobu += 1

        if sprobu == kilkist_sprob:
            messagebox.showinfo(title='Кінець', message='Чувак спроби закінчились')
            entry3['state'] = 'disabled'
            but5['state'] = 'disabled'
            but7 = Button(root, text="Почати заново", width=30, bg='green',fg="black", relief="ridge", bd=3, command=zanovo)
            but7.place(x=15, y=220)
    except(ValueError,UnboundLocalError,NameError):
        messagebox.showinfo(title='Ну чувак .......', message='Чувак дай уважніше')
        print('Ну блін чувак , дай уважніше')



def generyvatu():
    global sprobu
    global but5
    global entry3
    global d
    try:
        a = int(entry1.get())
        if a >= 0 :
            print('OK')
        else:
            messagebox.showerror(title='Кінець', message='Погано введено значення{g}')
    except(UnboundLocalError,ValueError,NameError):
        messagebox.showerror(title='Кінець', message='Погано введено значення{g}')


    try:
        b = int(entry2.get())
        if b <= 100 :
            print('OK')
        else:
            messagebox.showerror(title='Кінець', message='Погано введено значення {h}')
    except(UnboundLocalError,ValueError,NameError):
        messagebox.showerror(title='Кінець', message='Погано введено значення {h}')
        print('pogano')

    try:
        if a >=0 and b <= 100:
            # sprobu = 0
            c = [a,b]
            d=random.randint(a,b)
            root.title(d)
            entry2['state'] = 'disabled'
            entry1['state'] = 'disabled'
            but1['state'] = 'disabled'
            label100 = Label(root, text='Вгадай число', fg='black', bg='white', width=20, height=2)
            label100.place(x=10, y=140)

            entry3 = Entry(root,width=10, )
            entry3.place(x = 170,y = 150)

            but5 = Button(root, text='Спробувати',width=20 , fg="green", relief="ridge", bd=3 ,command=vgaday_chuslo)
            but5.place(x=50, y=180)



        else:
            print('pogano')
    except(UnboundLocalError, ValueError):
        messagebox.showerror(title='Кінець', message='Погано введено значення')
        print('pogano')


def pochatok_gru():
    global sprobu
    global entry1
    global entry2
    global but1
    global h
    global g

    # h = entry2.get()
    # g = entry1.get()

    root.geometry('300x300')
    root['bg'] = 'black'
    root.resizable(width=False, height=False)
    root.attributes('-topmost', True)
    sprobu = 1

    label1 = Label(root, text='Ліва межа',fg = 'black', width=10,height=2)
    label1.place(x = 10 , y = 10)

    label2 = Label(root, text='Права межа',fg = 'black', width=10,height=2)
    label2.place(x = 10 , y = 50)

    entry1 = Entry(root, width=10, )
    entry1.place(x = 100,y = 20)

    entry2 = Entry(root, width=10, )
    entry2.place(x = 100,y = 60)

    but1 = Button(root, text="Згенерувати", width=20 , fg="green", relief="ridge", bd=3 , command=generyvatu)
    but1.place(x = 50, y =100)


pochatok_gru()
root.mainloop()