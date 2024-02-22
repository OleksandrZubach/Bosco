import time
import tkinter
import random
import tkinter as tk
from tkinter import *

root = Tk()

def quite():
    root.quit()


def gra():
    gra = Tk()

    gra.geometry(f'410x450+{w}+{h}')
    gra.title('Гра')
    gra['bg'] = 'black'
    gra.resizable(width=False, height=False)
    gra.attributes('-topmost', True)
    frame = tk.Frame(gra, width=10, height=5, bg='lightblue')
    frame.pack(padx=10, pady=250)
    g = root.winfo_screenwidth()
    q = root.winfo_screenheight()
    print(g,q)


    def vash_vubir(choise):



        label_gra1 = Label(gra, text=f'Ваш вибір - {choise}', bg='black', fg='white', font=('Comic Sans MS',15), padx=10, justify=tk.LEFT)
        label_gra1.place(x=15, y=200)

        predmetu = ['папір    ', 'ножниці     ' , 'камінь    ']
        vubir_komputera = random.choice(predmetu)
        label_gra2 = Label(gra, text=f"Вибір комп'ютера - {vubir_komputera}", bg='black' , fg='white', font=('Comic Sans MS',15),padx=10,justify=tk.LEFT)
        label_gra2.place(x=15 , y = 250)


    gra_button = Button(gra, text='Камінь', bg='green', fg='white', padx=15, pady=10, bd=3, font=('Comic Sans MS', 15),relief='ridge', activebackground='yellow',activeforeground='blue' , command= lambda : vash_vubir('камінь     '))
    gra_button.place(x=20, y=350)

    gra_button1 = Button(gra, text='Ножниці', bg='green', fg='white', padx=16, pady=10, bd=3, font=('Comic Sans MS', 15),relief='ridge', activebackground='yellow',activeforeground='blue' , command= lambda : vash_vubir('ножниці   '))
    gra_button1.place(x=140, y=350)

    gra_button2 = Button(gra, text='Папір', bg='green', fg='white', padx=17, pady=10, bd=3, font=('Comic Sans MS', 15),relief='ridge' , activebackground='yellow',activeforeground='blue' , command= lambda : vash_vubir('папір     '))
    gra_button2.place(x=280, y=350)



w = root.winfo_screenwidth()//2-270
h = root.winfo_screenheight()//2-270
print(h,w)
root.geometry(f'400x450+{w}+{h}')

root.title('КНП')
root['bg']='forestgreen'

root.resizable(width=False , height=False)
root.attributes('-topmost',True)

frame_home = tk.Frame(root, width=300, height=400, bg='grey' , relief='ridge' , bd = 3)
frame_home.pack(padx=10, pady=15)


label1 = Label(root,text='КАМІНЬ - НОЖНИЦІ - ПАПІР', bg='yellow', fg='black', font=('Comic Sams MS',15) , pady=7,padx=15, relief='ridge' , bd=3 )
label1.place(x = 50, y = 15)

but1 = Button(root, text='Грати' , bg= 'yellow', fg='black', padx=55 , pady=10 , bd=3 , font=('Comic Sans MS',15), relief='ridge', activebackground='lime' ,command=gra)
but1.place(x = 110 , y = 100)

but2 = Button(root, text='Рахунок' , bg= 'yellow', fg='black', padx=45 , pady=10 , bd=3 , font=('Comic Sans MS',15), relief='ridge', activebackground='lime')
but2.place(x = 110 , y = 200)

but3 = Button(root, text='Вихід' , bg= 'yellow', fg='black', padx=55 , pady=10 , bd=3 , font=('Comic Sans MS',15), relief='ridge',activebackground='lime', command=quit)
but3.place(x = 110 , y = 300)


root.mainloop()
