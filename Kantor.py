import tkinter.messagebox
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox

root =Tk()
root.geometry('600x400')
root.title('Кантор')
root.resizable(width=False,height=False)
root.attributes('-topmost', True)
root['bg']= 'dark cyan'

frrrame = Frame(root,width=500,height=300,background='CadetBlue2',relief='ridge',bd=2)
frrrame.place(x=50,y=50)


#-------------------------------------------------------------------------------------------------------------------------

value_1 = StringVar()
value_2 = StringVar()
# entry_value = IntVar()


def valuta(even):
    global value_1
    a = (combo.get())
    value_1=a
    print(value_1)

def valuta_2(even):
    global value_2
    a = (combo1.get())
    value_2 = a
    print(value_2)


def final_sum():
    try:
        if not value_1 or not value_2:
            messagebox.showinfo(title='Помилка', message='Будь ласка, виберіть валюту для конвертації')
            return

        if not combo.get() or not combo1.get():
            messagebox.showinfo(title='Помилка', message='Будь ласка, виберіть валюту для конвертації')
            return

        if not entry1.get():
            messagebox.showinfo(title='Помилка', message='Будь ласка, введіть суму для конвертації')
            return
    except:
        print('все добре')



    label_in_valuta = Label(frame_2, text=f'{value_1}           👉🏾 👉', bg='medium aquamarine', fg="black", width=20,font=('Comic Sans MS',18))
    label_in_valuta.place(x=5, y=3)

    lavel_in_valuta_2 = Label(frame_2, text=value_2, bg='medium aquamarine', fg="black", width=10, font=('Comic Sans MS',18))
    lavel_in_valuta_2.place(x=300, y=3)



    try:

        if value_1 == 'Dollar'and value_2 == 'Euro':
                b = float((entry1.get())) * 0.91
                print(b)
                lavel_in_valuta_pid_valuta2 = Label(frame_2, text=f'{b}',background='medium aquamarine', fg="black", width=10, font=('Comic Sans MS', 18))
                lavel_in_valuta_pid_valuta2.place(x=300, y=32)

        if value_1 == 'Euro'and value_2 == 'Dollar':
                c = float((entry1.get())) * 1.09
                print(c)
                lavel_in_valuta_pid_valuta2 = Label(frame_2, text=f'{c}',background='medium aquamarine', fg="black", width=10, font=('Comic Sans MS', 18))
                lavel_in_valuta_pid_valuta2.place(x=300, y=32)

        if value_1 == 'Euro'and value_2 == 'Zloty':
                e = float((entry1.get())) * 4.30
                print(e)
                lavel_in_valuta_pid_valuta2 = Label(frame_2, text=f'{e}',background='medium aquamarine', fg="black", width=10, font=('Comic Sans MS', 18))
                lavel_in_valuta_pid_valuta2.place(x=300, y=32)

        if value_1 == 'Euro'and value_2 == 'Gruvnya':
                o = float((entry1.get())) * 41.78
                print(o)
                lavel_in_valuta_pid_valuta2 = Label(frame_2, text=f'{o}',background='medium aquamarine', fg="black", width=10, font=('Comic Sans MS', 18))
                lavel_in_valuta_pid_valuta2.place(x=300, y=32)

        if value_1 == 'Dollar'and value_2 == 'Gruvnya':
                n = float((entry1.get())) * 38.18
                print(n)
                lavel_in_valuta_pid_valuta2 = Label(frame_2, text=f'{n}',background='medium aquamarine', fg="black", width=10, font=('Comic Sans MS', 18))
                lavel_in_valuta_pid_valuta2.place(x=300, y=32)

        if value_1 == 'Dollar'and value_2 == 'Zloty':
                g = float((entry1.get())) * 3.93
                print(g)
                lavel_in_valuta_pid_valuta2 = Label(frame_2, text=f'{g}',background='medium aquamarine', fg="black", width=10, font=('Comic Sans MS', 18))
                lavel_in_valuta_pid_valuta2.place(x=300, y=32)

        if value_1 == 'Zloty'and value_2 == 'Dollar':
                e = float((entry1.get())) * 0.25
                print(e)
                lavel_in_valuta_pid_valuta2 = Label(frame_2, text=f'{e}',background='medium aquamarine', fg="black", width=10, font=('Comic Sans MS', 18))
                lavel_in_valuta_pid_valuta2.place(x=300, y=32)

        if value_1 == 'Zloty'and value_2 == 'Euro':
                h = float((entry1.get())) * 0.23
                print(h)
                lavel_in_valuta_pid_valuta2 = Label(frame_2, text=f'{h}',background='medium aquamarine', fg="black", width=10, font=('Comic Sans MS', 18))
                lavel_in_valuta_pid_valuta2.place(x=300, y=32)

        if value_1 == 'Zloty'and value_2 == 'Gruvnya':
                f = float((entry1.get())) * 9.71
                print(f)
                lavel_in_valuta_pid_valuta2 = Label(frame_2, text=f'{f}',background='medium aquamarine', fg="black", width=10, font=('Comic Sans MS', 18))
                lavel_in_valuta_pid_valuta2.place(x=300, y=32)

        if value_1 == 'Gruvnya' and value_2 == 'Euro':
                u = float((entry1.get())) * 0.024
                print(u)
                lavel_in_valuta_pid_valuta2 = Label(frame_2, text=f'{u}',background='medium aquamarine', fg="black", width=10, font=('Comic Sans MS', 18))
                lavel_in_valuta_pid_valuta2.place(x=300, y=32)

        if value_1 == 'Gruvnya' and value_2 == 'Dollar':
                m = float((entry1.get())) * 0.026
                print(m)
                lavel_in_valuta_pid_valuta2 = Label(frame_2, text=f'{m}',background='medium aquamarine', fg="black", width=10, font=('Comic Sans MS', 18))
                lavel_in_valuta_pid_valuta2.place(x=300, y=32)

        if value_1 == 'Gruvnya' and value_2 == 'Zloty':
                x = float((entry1.get())) * 0.10
                print(x)
                lavel_in_valuta_pid_valuta2 = Label(frame_2, text=f'{x}',background='medium aquamarine', fg="black", width=10, font=('Comic Sans MS', 18))
                lavel_in_valuta_pid_valuta2.place(x=300, y=32)
    except (ValueError, ZeroDivisionError, TypeError):
        messagebox.showinfo(title='Помилка', message='Сума введена не коректно')


    lavel_in_valuta_pid_valuta4 = Label(frame_2, text=f'{entry1.get()}',background='medium aquamarine', fg="black", width=10,font=('Comic Sans MS',18))
    lavel_in_valuta_pid_valuta4.place(x=5, y=32)


#----------------------------------------------------------------------------------------------------------------------------

label_nazva = Label(root,text='Кантор', fg='midnight blue',background='medium aquamarine',font=('Comic Sans MS',18), width=20,relief='ridge',bd=2)
label_nazva.place(x = 150,y=10)


#------------------------------------------------------------------------------------------------------------------------------


label_1 = Label(root,text=' Виберіть яку валюту хочете конвертувати   ↣',width=58,height=2,justify='left',anchor='w',font=('Comic Sans MS',10),relief='ridge',bd=2,bg='medium aquamarine',highlightbackground='dark cyan',highlightthickness=2)
label_1.place(x=65,y=70)

label_2 = Label(root,text=' Виберіть в яку валюту хочете конвертувати ↣',width=58,height=2,justify='left',anchor='w',font=('Comic Sans MS',10),relief='ridge',bd=2,bg='medium aquamarine',highlightbackground='dark cyan',highlightthickness=2)
label_2.place(x=65,y=120)

label_3 = Label(root,text=' Введіть суму                  ↣',width=58,height=2,justify='left',anchor='w',font=('Comic Sans MS',10),relief='ridge',bd=2,bg='medium aquamarine',highlightbackground='dark cyan',highlightthickness=2)
label_3.place(x=65,y=170)

#-----------------------------------------------------------------------------------------------------------------------




valuta_spusok = ['Gruvnya','Dollar','Euro','Zloty']
combo = tkinter.ttk.Combobox(root,width=20,state="readonly",values=valuta_spusok)
# value_1=combo
combo.place(x = 370,y=85)
combo.bind("<<ComboboxSelected>>", valuta)

combo1 = tkinter.ttk.Combobox(root,width=20,state="readonly",values=valuta_spusok)
# combo['values'] = ('Dollar','Euro','Zloty')
combo1.place(x = 370,y=135)
combo1.bind("<<ComboboxSelected>>", valuta_2)


#------------------------------------------------------------------------------------------------------------------------
entry1 = Entry(root,width=23)
entry1.place(x = 370,y=180)
entry1.bind("<Return>", final_sum)



#-----------------------------------------------------------------------------------------------------------------------

but1 = Button(root,text='ПОРАХУВАТИ',width=15,height=1,font=("Comic Sans MS",10),pady=1,padx=1,command=final_sum,bg='medium aquamarine',relief='ridge',bd=2,activebackground='dark cyan',highlightbackground='dark cyan',highlightthickness=2)
but1.place(x=230,y=220)

#-----------------------------------------------------------------------------------------------------------------------

frame_2 = Frame(root,width=470,height=80,background='medium aquamarine',relief='ridge',bd=2,highlightbackground='dark cyan',highlightthickness=2)
frame_2.place(x=65,y=260)

#-----------------------------------------------------------------------------------------------------------------------


root.mainloop()