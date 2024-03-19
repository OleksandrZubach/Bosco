import tkinter.messagebox
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import filedialog



root = tkinter.Tk()
root.geometry('700x800')
root['bg']='bisque'
root.attributes('-topmost', True)

#-----------------------------------------------------------------------------------------------------------------------

var = IntVar()
var2 = IntVar()


def nove_avto():

    global machina

    a = var.get()
    b = var2.get()
    #-------------------------------------------------------------------------------------------------------------------

    frame = Frame(root, width=600, height= 610,bg='aquamarine4')
    frame.place(x = 10, y = 160)

    #-------------------------------------------------------------------------------------------------------------------

    machina = StringVar()
    k = vubranuy_regym.get()
    print(k)
    #-------------------------------------------------------------------------------------------------------------------
    if  k == 'Нове авто':

        # with open(f"{file_path}", "w") as file:
        #     file.write(text_content)

        def zberezhenya():
            global file_path

            file_paths = filedialog.askopenfilenames(

                title="Вибрати файли",

                filetypes=[("Текстові файли", "*.txt"), ("Усі файли", "*.*")])

            if file_paths:

                print("Ви обрали наступні файли:")

                for file_path in file_paths:
                    print(file_path)
                    with open(f"{file_path}", "w") as file:
                        file.write(text_content)

            else:

                print("Вибір скасований або нічого не обрано.")





        def rezultat():
            global text_content
            try:
                text = Text(frame,width=25,height=7,wrap="word",font=('Comic Sans MS',18),fg='black')
                text.place(x = 5 , y= 220)
                text_content = (
                    f" Марка машини: {vubrana_marka.get()}\n "
                    f"Вид двигуна: {dvigun_vubranuy.get()}\n "
                    f"Вид двигуна: {dvigun_vubranuy.get()} \n"
                    f"Об'єм двигуна: {obem_dviguna_vubranuy.get()}\n "
                    f"Континент: {vubranuy_kontinent.get()}\n "
                    f"Колір: {selected_color}"
                )

                text.insert("1.0", text_content)
            except(NameError,):
                messagebox.showinfo('oops',text='Мабуть ви не обрали якийсь пункт')

            button_zberezhenya = Button(frame, text='Зберегти результат', width=15, height=2, command=zberezhenya)
            button_zberezhenya.place(x=450, y=270)

        marka_auto = LabelFrame(frame, text="Марка автомобіля")
        marka_auto.place(x = 10,y=10)
        vubrana_marka = StringVar()
        marku = ["Toyota", "Moskvich", "Skoda", "Nissan", "VW", "Lamborgini"]
        for i, x in enumerate(marku):
            marka = Radiobutton(marka_auto, text=x, variable=vubrana_marka, value=x,height=1,pady=3,anchor='w')
            marka.pack()

        dvigun = LabelFrame(frame, text="Вид двигуна")
        dvigun.place(x=150, y=10)
        dvigun_vubranuy = StringVar()
        vuburay_dvigun = ["Бензиновий", "Дизель"]
        for i, x in enumerate(vuburay_dvigun):
            button_vud_dviguna = Radiobutton(dvigun, text=x, variable=dvigun_vubranuy, value=x,anchor='w')
            button_vud_dviguna.pack()

        obem_dviguna = LabelFrame(frame, text="Об'єм двигуна")
        obem_dviguna.place(x=150, y=85)
        obem_dviguna_vubranuy = StringVar()
        vud_obemu_dviguna = ["менше 1200", "1200-1500","1501-2200","більше 2200"]
        for i, x in enumerate(vud_obemu_dviguna):
            button_obem_dviguna = Radiobutton(obem_dviguna, text=x, variable=obem_dviguna_vubranuy, value=x,anchor='w')
            button_obem_dviguna.pack()

        kontinent_vurobnuk = LabelFrame(frame, text="Континент виробник")
        kontinent_vurobnuk.place(x=270, y=10)
        vubranuy_kontinent = StringVar()
        vudu_kontunetviv = ["Азія", "Західна Європа", "Східна Європа", "Америка"]
        for i, x in enumerate(vudu_kontunetviv):
            button_vud_kontinenta = Radiobutton(kontinent_vurobnuk, text=x, variable=vubranuy_kontinent, value=x,anchor='w')
            button_vud_kontinenta.pack()

        # vik_auto = LabelFrame(frame, text="Оберіть вік машини")
        # vik_auto.place(x=420, y=10)
        # vubranuy_vik = StringVar()
        # vudu_vik = ["До 5", "6-10", "11-15", "більше 15 років"]
        # for i, x in enumerate(vudu_vik):
        #     button_vud_kontinenta = Radiobutton(vik_auto, text=x, variable=vubranuy_vik, value=x,anchor='w')
        #     button_vud_kontinenta.pack()


        def change_color():
            global selected_color
            selected_color = spinbox.get()
            label = Label(frame, bg=selected_color,width=15,height=3)
            label.place(x=420,y=140)
            # root.configure(background=selected_color)

        spinbox_frame = LabelFrame(frame , text='Оберіть колір',width=30,height=10)
        spinbox_frame.place(x = 270, y = 150)
        vubranuy_colir = StringVar()
        spinbox_znachenya = ["green", 'yellow', 'black', 'red', 'blue']
        spinbox = Spinbox(spinbox_frame, values=spinbox_znachenya,command=change_color,wrap=True)
        spinbox.pack()


        button_rezult = Button(frame,text='Результат',width=10,height=2,command=rezultat)
        button_rezult.place(x=450,y=220)

    elif k == 'Іноземного виробництва':

        # with open(f"{file_path}", "w") as file:
        #     file.write(text_content)

        def zberezhenya():
            global file_paths1

            file_paths1 = filedialog.askopenfilenames(
                title="Вибрати файли",
                filetype=[("Текстові файли", "*.txt"), ("Усі файли", "*.*")]
            )

            if file_paths1:
                print("Ви обрали наступні файли:")
                for file_path1 in file_paths1:
                    print(file_path1)
                    with open(file_path1, "w") as file1:
                        file1.write(text_content1)
            else:
                print("Вибір скасований або нічого не обрано.")





        def rezultat():
            global text_content1
            try:
                text1 = Text(frame,width=25,height=7,wrap="word",font=('Comic Sans MS',18),fg='black')
                text1.place(x = 5 , y= 220)
                text_content1 = (
                    f" Марка машини: {vubrana_marka1.get()}\n "
                    f"Вид двигуна: {dvigun_vubranuy1.get()}\n "
                    f"Вид двигуна: {dvigun_vubranuy1.get()} \n"
                    f"Об'єм двигуна: {obem_dviguna_vubranuy1.get()}\n "
                    f"Континент: {vubranuy_kontinent1.get()}\n "
                    f"Вік авто: {vubranuy_vik1.get()}\n"
                    f"Колір: {selected_color1}"
                )

                text1.insert("1.0", text_content1)
            except(NameError,):
                messagebox.showinfo('oops',text='Мабуть ви не обрали якийсь пункт')

            button_zberezhenya1 = Button(frame, text='Зберегти результат', width=15, height=2, command=zberezhenya)
            button_zberezhenya1.place(x=450, y=270)

        marka_auto1 = LabelFrame(frame, text="Марка автомобіля")
        marka_auto1.place(x = 10,y=10)
        vubrana_marka1 = StringVar()
        marku1 = ["Toyota",  "Skoda", "Nissan", "VW", "Lamborgini"]
        for i, x in enumerate(marku1):
            marka = Radiobutton(marka_auto1, text=x, variable=vubrana_marka1, value=x,height=1,pady=3,anchor='w')
            marka.pack()

        dvigun1 = LabelFrame(frame, text="Вид двигуна")
        dvigun1.place(x=150, y=10)
        dvigun_vubranuy1 = StringVar()
        vuburay_dvigun1 = ["Бензиновий", "Дизель"]
        for i, x in enumerate(vuburay_dvigun1):
            button_vud_dviguna1 = Radiobutton(dvigun1, text=x, variable=dvigun_vubranuy1, value=x,anchor='w')
            button_vud_dviguna1.pack()

        obem_dviguna1 = LabelFrame(frame, text="Об'єм двигуна")
        obem_dviguna1.place(x=150, y=85)
        obem_dviguna_vubranuy1 = StringVar()
        vud_obemu_dviguna1 = ["менше 1200", "1200-1500","1501-2200","більше 2200"]
        for i, x in enumerate(vud_obemu_dviguna1):
            button_obem_dviguna1 = Radiobutton(obem_dviguna1, text=x, variable=obem_dviguna_vubranuy1, value=x,anchor='w')
            button_obem_dviguna1.pack()

        kontinent_vurobnuk1 = LabelFrame(frame, text="Континент виробник")
        kontinent_vurobnuk1.place(x=270, y=10)
        vubranuy_kontinent1 = StringVar()
        vudu_kontunetviv1 = ["Азія", "Західна Європа", "Східна Європа", "Америка"]
        for i, x in enumerate(vudu_kontunetviv1):
            button_vud_kontinenta1 = Radiobutton(kontinent_vurobnuk1, text=x, variable=vubranuy_kontinent1, value=x,anchor='w')
            button_vud_kontinenta1.pack()

        vik_auto1 = LabelFrame(frame, text="Оберіть вік машини")
        vik_auto1.place(x=420, y=10)
        vubranuy_vik1 = StringVar()
        vudu_vik1 = ["До 5", "6-10", "11-15", "більше 15 років"]
        for i, x in enumerate(vudu_vik1):
            button_vud_kontinenta1 = Radiobutton(vik_auto1, text=x, variable=vubranuy_vik1, value=x,anchor='w')
            button_vud_kontinenta1.pack()


        def change_color1():
            global selected_color1
            selected_color1 = spinbox1.get()
            label1 = Label(frame, bg=selected_color1,width=15,height=3)
            label1.place(x=420,y=140)
            # root.configure(background=selected_color)

        spinbox_frame1 = LabelFrame(frame , text='Оберіть колір',width=30,height=10)
        spinbox_frame1.place(x = 270, y = 150)
        vubranuy_colir1 = StringVar()
        spinbox_znachenya1 = ["green", 'yellow', 'black', 'red', 'blue']
        spinbox1 = Spinbox(spinbox_frame1, values=spinbox_znachenya1,command=change_color1,wrap=True)
        spinbox1.pack()


        button_rezult1 = Button(frame,text='Результат',width=10,height=2,command=rezultat)
        button_rezult1.place(x=450,y=220)






#-----------------------------------------------------------------------------------------------------------------------

novy_abo_by_machina = LabelFrame(root,text='Введіть попередні дані про автомобіль', width=250,height=100 , font=("Verdana",8))
novy_abo_by_machina.place(x = 20, y = 20)

# combo_nova_machina = Checkbutton(novy_abo_by_machina,text='Нова машина',width=10,height=2, font=("Verdana",8),variable=var)
# combo_nova_machina.place(x=14 ,y = 5)
# # combo_nova_machina.bind("<<CheckbuttonSelected>>",nove_avto)
#
# combo_inozemnogo_vurobnutsva_machina = Checkbutton(novy_abo_by_machina,text='Іноземного виробнитсва',width=20,height=2,variable=var2,font=("Verdana",8))
# combo_inozemnogo_vurobnutsva_machina.place(x=11 ,y = 40)


vubranuy_regym = StringVar()
vudu_regym = ["Нове авто", "Іноземного виробництва"]
for i, x in enumerate(vudu_regym):
    button_vud_regumy = Radiobutton(novy_abo_by_machina, text=x, variable=vubranuy_regym, value=x,anchor='w')
    button_vud_regumy.pack()

button = Button(root,text='Основні питання', width=15,height=2,font=("Verdana",8),command=nove_avto)
button.place(x = 400 , y = 80)

#-----------------------------------------------------------------------------------------------------------------------

root.mainloop()
