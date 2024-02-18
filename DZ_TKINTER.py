from tkinter import *
root = Tk()
click_count = 0
def on_button_click():
    global click_count
    click_count += 1
    root.title(f"Кількість клацань: {click_count}")
    if click_count % 2 == 0:
        label_text.set("Привіт")
    else:
        label_text.set('Папа')
root['bg'] = 'lightgreen'
root.title('Привіт')
root.geometry('400x250')
root.attributes('-topmost', True)
label_text = StringVar()
label_text.set("Привіт")
napus = Label(root, textvariable=label_text, fg='black', font=('arial', 12))
napus.pack(pady=10)
btn = Button(root, text="Натисни і кількість клацань змінеться", fg='yellow', bg='blue', bd=5, font=('arial', 12),activebackground='yellow', activeforeground='blue', command=on_button_click)
btn.pack()
root.mainloop()