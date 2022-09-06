import customtkinter as ctk
from tkinter import *

root = ctk.CTk()
root.title("Lab Shortcut")
root.geometry("320x500+620+150")
root.config(background='#4B5267')
ctk.set_appearance_mode("System")

language_var = StringVar()
language_var.set('English')

menu_img = PhotoImage(file='main/images/menu.png')
menu_open = False
calc_open = False

def results(all):
    open_calculator('density', all)

def close_calculator():
    calculator_type.config(text='Normal')
    calculation_frame.grid_forget()
    open_menu()

def open_calculator(type, values=False):
    global menu_open
    menu_open = True
    open_menu()
    if type == 'density':
        from formulas.density import density
        global calc_open
        calc_open = True
        calculation_frame.grid(row=1, column=0, columnspan=2)
        calculator_type.config(text='Density')
        Label(calculation_frame, text='Density (g/cm³)', bg="#4B5267", fg="white").grid(row=1, column=0, padx=(40, 0), pady=(15, 0))
        density_entry = ctk.CTkEntry(calculation_frame, width=80)
        density_entry.grid(row=2, column=0, pady=(15, 0), padx=(35, 0))
        Label(calculation_frame, text='Mass (g)', bg="#4B5267", fg="white").grid(row=1, column=1, pady=(15, 0))
        mass_entry = ctk.CTkEntry(calculation_frame, width=80)
        mass_entry.grid(row=2, column=1, pady=(15, 0), padx=(0, 0))
        Label(calculation_frame, text='Volume (ml)', bg="#4B5267", fg="white").grid(row=1, column=2, pady=(15, 0))
        volume_entry = ctk.CTkEntry(calculation_frame, width=80)
        volume_entry.grid(row=2, column=2, pady=(15, 0), padx=(0, 0))
        for n, i in enumerate((density_entry, mass_entry, volume_entry)):
            if values:
                i.insert(0, values[n])
            else:
                i.insert(0, '0')
        ctk.CTkButton(calculation_frame, text='Calculate', width=80, command=lambda: results(density(float(density_entry.get()), float(mass_entry.get()), float(volume_entry.get())))).grid(row=3, column=0, columnspan=3, pady=(15, 0), padx=(40, 0))
        ctk.CTkButton(calculation_frame, text='Close', width=80, command=lambda: close_calculator()).grid(row=4, column=0, columnspan=3, pady=(15, 0), padx=(40, 0))

def open_menu():
    global menu_open
    if menu_open == False:
        menu_frame.grid(row=1, column=0, columnspan=2)
        calculator_type.grid_forget()
        calculation_frame.grid_forget()
        menu_open = True 
    elif menu_open == True:
        calculator_type.grid(row=0, column=1, pady=(15, 0), padx=(10, 0), sticky='w')
        menu_frame.grid_forget()
        if calculator_type['text'] != 'Normal':
            calculation_frame.grid(row=1, column=0, columnspan=2)
        menu_open = False

menu_frame = ctk.CTkFrame(root, width=280, height=1980, fg_color='#171c2f')
calculation_frame = ctk.CTkFrame(root, width=280, height=1980, fg_color='#4B5267')

# Config menu
Label(menu_frame,
    text="Options",
    bg='#171c2f',
    fg='white',
    font=('Input', 12)).grid(row=0, column=0, padx=(0, 200), pady=(15, 10))
Button(menu_frame,
    text="• Language",
    bg='#171c2f',
    fg='white',
    font=('Input', 8),
    activebackground='#171c2f',
    activeforeground='white',
    cursor='hand2',
    bd=0).grid(row=1, column=0, ipadx=15, pady=(0, 10), sticky='w')
Button(menu_frame,
    text="• Theme",
    bg='#171c2f',
    fg='white',
    font=('Input', 8),
    activebackground='#171c2f',
    activeforeground='white',
    cursor='hand2',
    bd=0).grid(row=2, column=0, ipadx=15, pady=(0, 10), sticky='w')
Label(menu_frame,
    text="Calculator",
    bg='#171c2f',
    fg='white',
    font=('Input', 12)).grid(row=3, column=0, padx=(15, 185), pady=(15, 10))

Button(menu_frame,
    text="• Standart Deviation",
    bg='#171c2f',
    fg='white',
    font=('Input', 8),
    activebackground='#171c2f',
    activeforeground='white',
    cursor='hand2',
    bd=0,
    command=lambda: open_calculator('std')).grid(row=4, column=0, ipadx=15, pady=(0, 10), sticky='w')

Button(menu_frame,
    text="• Coefficient of variation",
    bg='#171c2f',
    fg='white',
    font=('Input', 8),
    activebackground='#171c2f',
    activeforeground='white',
    cursor='hand2',
    bd=0,
    command=lambda: open_calculator('cv')).grid(row=5, column=0, ipadx=15, pady=(0, 10), sticky='w')

Button(menu_frame,
    text="• Density",
    bg='#171c2f',
    fg='white',
    font=('Input', 8),
    activebackground='#171c2f',
    activeforeground='white',
    cursor='hand2',
    bd=0,
    command=lambda: open_calculator('density')).grid(row=6, column=0, ipadx=15, pady=(0, 10), sticky='w')

Button(menu_frame,
    text="• Relative and absolute errors",
    bg='#171c2f',
    fg='white',
    font=('Input', 8),
    activebackground='#171c2f',
    activeforeground='white',
    cursor='hand2',
    bd=0,
    command=lambda: open_calculator('errors')).grid(row=7, column=0, ipadx=15, pady=(0, 20), sticky='w')

Button(root,
    image=menu_img,
    bg='#4B5267',
    bd=0,
    activebackground='#4B5267',
    cursor='hand2',
    command=open_menu).grid(row=0, column=0, padx=(25, 0), pady=(15, 0), sticky='w')

calculator_type = Label(root,
                text="Normal",
                bg='#4B5267',
                fg='white',
                font=('Input', 15))
calculator_type.grid(row=0, column=1, columnspan=2, pady=(15, 0), sticky='w')



root.mainloop()