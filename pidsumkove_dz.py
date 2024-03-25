from tkinter import filedialog
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pygame
import threading

root = Tk()
root.geometry('900x580+800+200')
root.title('2')
root['bg']='darkcyan'



notebook = ttk.Notebook(root)
tab = tk.Frame(notebook)
tab1 = tk.Frame(notebook, background='darkcyan')
tab2 = tk.Frame(notebook , background='paleturquoise')
tab3 = tk.Frame(notebook, background='paleturquoise')
tab4 = tk.Frame(notebook, background='paleturquoise')
tab5 = tk.Frame(notebook, background='paleturquoise')
# tab6 = tk.Frame(notebook, background='darkcyan')

notebook.add(tab, text="Тест")
notebook.add(tab1, text="Реєстрація")
notebook.add(tab2, text="Завдання 1")
notebook.add(tab3, text="Завдання 2")
notebook.add(tab4, text="Завдання 3")
notebook.add(tab5, text="Завдання 4")
# notebook.add(tab6, text="Результат")

notebook.pack(expand=1, fill="both")

def zberezhenya():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file1:
            file1.write(entry_imya.get() + "\n")
            file1.write(entry_prizvuzhche.get() + "\n")
            file1.write(entry_vik.get() + "\n")
            file1.write(str(b))

def rezultat():
    global b
    global tab6
    rezult = 0
    print(var_babcya1.get(),var_dzidzo1.get(),var_franko1.get(),var_zirka1.get())
    if var_franko1.get() == 4:
        rezult += 1
    if var_dzidzo1.get() == 17:
        rezult += 1
    if var_zirka1.get() == 18:
        rezult += 1
    if var_babcya1.get() == 39:
        rezult += 1

    tab6 = tk.Frame(notebook, background='darkcyan')
    notebook.add(tab6, text="Результат")

    b = f'Ваш результат\n {rezult} з 4'
    frame_label = Label(tab6,text=b,background='brown',width=15,height=5,font=('Comic Sans MS',50))
    frame_label.place(x=130,y=30)

    but = Button(frame_label,text='Зберегти результат',width=20,height=3,fg='black',command=zberezhenya)
    but.place(x=240,y=400)

def next_question(tab_index):
    notebook.select(tab_index)


def dani_korustyvacha():
    a = entry_imya.get()
    b = entry_prizvuzhche.get()
    c = entry_vik.get()
    print(a,b,c)
#-----------------------------------------------------------------------------------------------------------------------

main_menu = Menu()
root.config(menu=main_menu)

spusok_vikon = ['Про програму','Entry','Text','Time','Date Time',
                'Checkbutton','Radiobutton','Listbox','Combobox',
                'Spinbox','Scale','Canvas','Збереження результатів']
# ----------------------------------------------------------------------------------------------------------------------

pro_programy = Menu(main_menu,tearoff=0)
pro_programy.entryconfig(0, anchor="w")
main_menu.add_cascade(label='Про програму',menu=pro_programy)
pro_programy.add_command(label='Дізнатись більше')

#---------------------------------------------------------------------------------------------- Тест на Українця

label_blue = Label(tab , width=900 , height=250 , background='blue')
label_blue.place(x=0,y=0)
label_blue2 = Label(label_blue ,text='Тест\nна',fg='black', width=10 , height=2 , background='blue', font= ('Comic Sans MS',40),pady=2,padx=5)
label_blue2.place(x=250,y=90)
label_yellow = Label(tab , width=900 , height=250 , background='yellow')
label_yellow.place(x=0,y=250)
label_yellow2 = Label(label_yellow ,text='Українця',fg='black', width= 10 , height=1 , background='yellow', font= ('Comic Sans MS',40),pady=2,padx=5)
label_yellow2.place(x=260,y=-10),

but = Button(label_yellow,text='РОЗПОЧАТИ',fg='black', width= 13 , height=1, font= ('Comic Sans MS',20),pady=2,padx=5,activebackground='yellow',background='palegreen', command=lambda: next_question(notebook.index(tab1)))
but.place(x=320,y=130)


#------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------- Реєстрація

frame = Label(tab1, width=53, height=30, background='lightyellow')
frame.place(x=258, y=30)

label_zavdanya_1 = Label(tab1, text="Ведіть свої дані", bg='yellow', width=37, height=2, font=('Comic Sans MS', 13))
label_zavdanya_1.place(x=258, y=25)

entry_imya = Entry(frame, width=17, fg='blue', relief='ridge', bd=3, font=('Comic Sans MS', 13))
entry_imya.place(x=5, y=65)
label_imya = Label(frame, width=17, fg='black', font=('Comic Sans MS', 8), text="         -      введіть ім'я", background='lightyellow')
label_imya.place(x=200, y=70)

entry_prizvuzhche = Entry(frame, width=17, fg='blue', relief='ridge', bd=3, font=('Comic Sans MS', 13))
entry_prizvuzhche.place(x=5, y=130)
label_prizvuzhche = Label(frame, width=22, fg='black', font=('Comic Sans MS', 8),text="           -      введіть прізвище", background='lightyellow')
label_prizvuzhche.place(x=200, y=138)

entry_vik = Entry(frame, width=7, fg='blue', relief='ridge', bd=3, font=('Comic Sans MS', 13))
entry_vik.place(x=55, y=195)
label_vik = Label(frame, width=20, fg='black', font=('Comic Sans MS', 8), text="-      введіть вік", background='lightyellow')
label_vik.place(x=200, y=205)

knopka_zareestuvatu_korustyvacha = Button(frame, text='Зареєструватись', width=14, height=2, bg='olivedrab',relief='ridge', bd=3, command=dani_korustyvacha)
knopka_zareestuvatu_korustyvacha.place(x=200, y=350)

#---------------------------------------------------------------------------------------------- Завдання 1
image = Image.open("Ivan_Franko.jpg")
image = image.resize((300, 200))
photo = ImageTk.PhotoImage(image)
canvas = tk.Canvas(tab2, width=300, height=200)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=photo)
canvas.create_text(150, 180, fill="red", font=("Arial", 16))
label_franko = Label(tab2,text='Хто зображений на цій фотографії',width=30,height=2,font= ('Comic Sans MS',15))
label_franko.place(x=260,y=200)
var_franko1 = IntVar() #------------------------------------------------------------ Відповідь Франко ------------------
radiobutton_franko1 = Radiobutton(tab2,text='А) Леся українка',variable=var_franko1,value=1)
radiobutton_franko1.place(x=200,y=300)
radiobutton_franko2 = Radiobutton(tab2,text='Б) Тарас Шевченко',variable=var_franko1,value=2)
radiobutton_franko2.place(x=500,y=300)
radiobutton_franko3 = Radiobutton(tab2,text='В) Олександр Зубач',variable=var_franko1,value=3)
radiobutton_franko3.place(x=200,y=400)
radiobutton_franko4 = Radiobutton(tab2,text='Г) Іван Франко',variable=var_franko1,value=4)
radiobutton_franko4.place(x=500,y=400)
button_franko = Button(tab2,text='Далі',width= 13 , height=1, font= ('Comic Sans MS',10),pady=2,padx=5,activebackground='yellow',background='palegreen', command=lambda: next_question(notebook.index(tab3)))
button_franko.place(x=450,y=450)
button_franko2 = Button(tab2,text='Назад',width= 13 , height=1, font= ('Comic Sans MS',10),pady=2,padx=5,activebackground='yellow',background='palegreen', command=lambda: next_question(notebook.index(tab1)))
button_franko2.place(x=300,y=450)

#----------------------------------------------------------------------------------- Завдання 2

def play_music():
    global thread
    pygame.mixer.init()
    pygame.mixer.music.load("dzidzio-kadlak.mp3")
    total_length = pygame.mixer.Sound.get_length(pygame.mixer.Sound("dzidzio-kadlak.mp3")) * 1000
    progress_bar["maximum"] = total_length
    pygame.mixer.music.play()
    thread = threading.Thread(target=update_progress)
    thread.start()

def update_progress():
    global current_time
    while pygame.mixer.music.get_busy():
        current_time = pygame.mixer.music.get_pos()
        progress_bar["value"] = current_time

def stop_music():
    pygame.mixer.music.stop()
    progress_bar["value"] = current_time

progress_bar = ttk.Progressbar(tab3, orient="horizontal", length=200, mode="determinate")
progress_bar.place(x=300,y=150)

play_button = tk.Button(tab3, text="Play Music", command=play_music)
play_button.place(x=435,y=200)

stop_button = tk.Button(tab3, text="Stop Music", command=stop_music)
stop_button.place(x=300,y=200)

var_dzidzo1 = IntVar() #------------------------------------------------------------ Відповідь Dzizyo ------------------
radiobutton_dzidzo1 = Radiobutton(tab3,text='А)Михайло Хома',variable=var_dzidzo1,value=17)
radiobutton_dzidzo1.place(x=200,y=300)
radiobutton_dzidzo2 = Radiobutton(tab3,text='Б) Ivan Navi',variable=var_dzidzo1,value=27)
radiobutton_dzidzo2.place(x=550,y=300)
radiobutton_dzidzo3 = Radiobutton(tab3,text='В) Олександр Пономарьов',variable=var_dzidzo1,value=37)
radiobutton_dzidzo3.place(x=200,y=400)
radiobutton_dzidzo4 = Radiobutton(tab3,text='Г) Monatik',variable=var_dzidzo1,value=47)
radiobutton_dzidzo4.place(x=550,y=400)
button_dzizo1 = Button(tab3,text='Далі',width= 13 , height=1, font= ('Comic Sans MS',10),pady=2,padx=5,activebackground='yellow',background='palegreen', command=lambda: next_question(notebook.index(tab4)))
button_dzizo1.place(x=450,y=450)
button_dzizo2 = Button(tab3,text='Назад',width= 13 , height=1, font= ('Comic Sans MS',10),pady=2,padx=5,activebackground='yellow',background='palegreen', command=lambda: next_question(notebook.index(tab2)))
button_dzizo2.place(x=300,y=450)
label_dzizo = Label(tab3,text='Хто автор пісні ?',width= 13 , height=1, font= ('Comic Sans MS',40),pady=2,padx=5,activebackground='yellow', background='paleturquoise')
label_dzizo.place(x=220,y=10)


#-------------------------------------------------------------------------------- Завдання 3 ---------------------------

label_zirka = Label(tab4,text='points = [(100, 10), (125, 90), (200, 90), (140, 130)\n '
              '(100, 160), (40, 200), (60, 130), (0, 90), (75, 90)],(160, 200) \n'
            'for i in range(len(points)):\n'
                    'canvas.create_line(points[i][0], points[i][1], points[(i + 2) % len(points)][0], points[(i + 2) % len(points)][1])',width=100,height=10, background='paleturquoise')
label_zirka.place(x=100,y=70)

var_zirka1 = IntVar() #------------------------------------------------------------ Відповідь Zirka ------------------
radiobutton_zirka1 = Radiobutton(tab4,text='А)Зірка',variable=var_zirka1,value=18)
radiobutton_zirka1.place(x=200,y=300)
radiobutton_zirka2 = Radiobutton(tab4,text='Б) Палалелограм',variable=var_zirka1,value=28)
radiobutton_zirka2.place(x=550,y=300)
radiobutton_zirka3 = Radiobutton(tab4,text='В) Паралелепіпед',variable=var_zirka1,value=38)
radiobutton_zirka3.place(x=200,y=400)
radiobutton_zirka4 = Radiobutton(tab4,text='Г) Трапеція',variable=var_zirka1,value=48)
radiobutton_zirka4.place(x=550,y=400)
button_zirka1 = Button(tab4,text='Далі',width= 13 , height=1, font= ('Comic Sans MS',10),pady=2,padx=5,activebackground='yellow',background='palegreen', command=lambda: next_question(notebook.index(tab5)))
button_zirka1.place(x=450,y=450)
button_zirka2 = Button(tab4,text='Назад',width= 13 , height=1, font= ('Comic Sans MS',10),pady=2,padx=5,activebackground='yellow',background='palegreen', command=lambda: next_question(notebook.index(tab3)))
button_zirka2.place(x=300,y=450)
label_zirka = Label(tab4,text='Що за фігура ?',width= 13 , height=1, font= ('Comic Sans MS',20),pady=2,padx=5,activebackground='yellow', background='paleturquoise')
label_zirka.place(x=330,y=10)

#-------------------------------------------------------------------------------------  Завдання 4

label_babcya = Label(tab5,text='Якими діями українська бабця під час бойових \n дій 2022 отримала титул "сучасної княгині Ольги"', background='paleturquoise', font=('Comic Sans MS', 20))
label_babcya.place(x=100,y=30)

var_babcya1 = IntVar() #------------------------------------------------------------ Відповідь babcya ------------------
radiobutton_babcya1 = Radiobutton(tab5,text='А) Вкрала танк та передала ЗСУ',variable=var_babcya1,value=19)
radiobutton_babcya1.place(x=200,y=250)
radiobutton_babcya2 = Radiobutton(tab5,text='Б) Передала 100 банок консервації \nдля збивання ворожих дронів',variable=var_babcya1,value=29)
radiobutton_babcya2.place(x=550,y=250)
radiobutton_babcya3 = Radiobutton(tab5,text='В) Підсипала проносне у чай \nокупантів та підпалила в у туалеті',variable=var_babcya1,value=39)
radiobutton_babcya3.place(x=200,y=350)
radiobutton_babcya4 = Radiobutton(tab5,text='Г) Тримала в заручниках загін окупантів',variable=var_babcya1,value=49)
radiobutton_babcya4.place(x=550,y=350)
button_babcya1 = Button(tab5,text='Далі',width= 13 , height=1, font= ('Comic Sans MS',10),pady=2,padx=5,activebackground='yellow',background='palegreen', command=lambda: next_question(notebook.index(tab6)))
button_babcya1.place(x=450,y=450)
button_babcya2 = Button(tab5,text='Назад',width= 13 , height=1, font= ('Comic Sans MS',10),pady=2,padx=5,activebackground='yellow',background='palegreen', command=lambda: next_question(notebook.index(tab3)))
button_babcya2.place(x=300,y=450)
button_kinec = Button(tab5,text='Завершити тест',width= 13 , height=1, font= ('Comic Sans MS',10),pady=2,padx=5,activebackground='yellow',background='palegreen', command=rezultat)
button_kinec.place(x=630,y=450)

# c = Canvas(root, width=200, height=150)
# c.pack()

print(var_babcya1.get(), var_dzidzo1.get(), var_franko1.get(), var_zirka1.get())

root.mainloop()