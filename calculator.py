from tkinter import *
def dia(value):
    a = pole_var.get()
    pole_var.set(a + str(value))

def calculate():
    try:
        result = eval(pole_var.get())
        pole_var.set(result)
    except Exception as e:
        pole_var.set("Error")

def clear():
    pole_var.set("")

def exit_app():
    root.quit()

root = Tk()

root.geometry('350x500')
root.title('Калькулятор')
root.resizable(False, False)
root.configure(bg='#2c3e50')

pole_var = StringVar()
pole = Entry(root, textvariable=pole_var, width=20, font=('Arial', 20), bd=10, insertwidth=4, justify='right')
pole.grid(row=0, column=0, columnspan=4, pady=10)

buttons_frame = Frame(root, bg='#2c3e50')
buttons_frame.grid(row=1, column=0, columnspan=4)

buttons_list = ['7', '8', '9', '/','4', '5', '6', '*','1', '2', '3', '-','0', '.', '=', '+','C', 'Exit']

row_val = 0
col_val = 0

for button in buttons_list:
    if button == '=':
        btn = Button(buttons_frame, text=button, width=5, height=2, command=calculate, font=('Arial', 14), bg='#3498db', fg='white')
    elif button == 'C':
        btn = Button(buttons_frame, text=button, width=5, height=2, command=clear, font=('Arial', 14), bg='#e74c3c', fg='white')
    elif button == 'Exit':
        btn = Button(buttons_frame, text=button, width=5, height=2, command=exit_app, font=('Arial', 14), bg='#95a5a6', fg='white')
    else:
        btn = Button(buttons_frame, text=button, width=5, height=2, command=lambda val=button: dia(val), font=('Arial', 14), bg='#34495e', fg='white')

    btn.grid(row=row_val, column=col_val, padx=10, pady=10)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()