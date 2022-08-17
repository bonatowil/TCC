from tkinter import *
root = Tk()

root.geometry('240x180+800+200')
root.title('Lab Shortcut')

def open(window):
    if window == 'signup':
        pass
    if window == 'signin':
        pass


signup_button = Button(root,
                text='PT-BR',
                font=('Input', 10),
                width='35',
                height='5',
                bd=1,
                fg='white',
                activeforeground='white',
                bg='#4B5267',
                activebackground='#4B5267',
                cursor='hand2',
                command=lambda: open('signup'))
signup_button.pack()

signin_button = Button(root,
                text='EN-US',
                font=('Input', 10),
                width='35',
                height='5',
                bd=1,
                fg='white',
                activeforeground='white',
                bg='#4B5267',
                activebackground='#4B5267',
                cursor='hand2',
                command=lambda: open('signin'))
signin_button.pack()

root.mainloop()