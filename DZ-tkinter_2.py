import time
import tkinter
import random
import tkinter as tk
from tkinter import *

root = Tk()

w = root.winfo_screenwidth()//2-270
h = root.winfo_screenheight()//2-270
print(h,w)
root.geometry(f'400x450+{w}+{h}')

root.title('КНП')
root['bg']='black'

root.resizable(width=False , height=False)
root.attributes('-topmost',True)

def gra():
    gra = Tk()

    gra.geometry(f'400x450+{w}+{h}')
    gra.title('Гра')
    gra['bg'] = 'black'
    gra.resizable(width=False, height=False)
    gra.attributes('-topmost', True)

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



    # gra.mainloop()



label1 = Label(root,text='КАМІНЬ - НОЖНИЦІ - ПАПІР', bg = 'black' , fg='white', font=('Comic Sams MS',15), relief='ridge',pady=5,padx=5 , bd=3  )
label1.place(x = 60, y = 15)

but1 = Button(root, text='ГРАТИ' , bg= 'black', fg='white', padx=15 , pady=10 , bd=3 , font=('Comic Sans MS',15), relief='ridge' ,command=gra)
but1.place(x = 150 , y = 100)

but2 = Button(root, text='Рахунок' , bg= 'black', fg='white', padx=10 , pady=10 , bd=3 , font=('Comic Sans MS',15), relief='ridge')
but2.place(x = 150 , y = 200)

but3 = Button(root, text='Вихід' , bg= 'black', fg='white', padx=20 , pady=10 , bd=3 , font=('Comic Sans MS',15), relief='ridge')
but3.place(x = 150 , y = 300)


root.mainloop()
