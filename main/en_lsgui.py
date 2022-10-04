from base64 import standard_b64decode
import customtkinter as ctk
from tkinter import *

root = ctk.CTk()

menu_img = PhotoImage(file='main/images/menu.png')
lab_icon = PhotoImage(file='main/images/lab_icon.png')

root.title("Lab Shortcut")
root.iconphoto(True, lab_icon)
root.geometry("320x500+620+150")
root.config(background='#4B5267')
ctk.set_appearance_mode("System")

language_var = StringVar()
language_var.set('English')

entry_var = StringVar()

menu_open = False

def refresh():
    warning_label.grid_forget()

def check_if_number(num):
    try:
        global numbers, real_numbers
        num = float(num)
        real_numbers.append(num)
        numbers.append(f"Num {len(numbers)+1}º: {str(num)}\n")
        standard_deviation(number_list=numbers, real_numbers=real_numbers)
    except ValueError:
        if warning_label.winfo_ismapped() == 0:
            root.after(3000, refresh)
            warning_label.grid(row=10, column=0)

def reset_mainframe():
    for widget in main_frame.winfo_children():
        if widget.winfo_id() != warning_label.winfo_id():
            widget.destroy()

def language_change(language):
    if language == 'English':
        pass
    elif language == 'Português':
        root.destroy()
        import pt_lsgui
        
def language_menu():
    global menu_open
    menu_open = True
    menu()
    reset_mainframe()
    option_title.config(text='Language')
    main_frame.grid(row=1, column=0, columnspan=3, pady=(60, 0))
    ctk.CTkOptionMenu(main_frame, values=['English', 'Português'], variable=language_var).grid(row=1, column=0, padx=(30, 0))
    ctk.CTkButton(main_frame, text='Save', width=100, command= lambda: language_change(language_var.get())).grid(row=1, column=1, padx=10)

def results(type, args):
    if type == 'density':
        density(args)
    elif type == 'std':
        pass

def close_calculator():
    option_title.config(text='Normal')
    main_frame.grid_forget()
    menu()

def open_calculator(type):
    global menu_open
    menu_open = True
    menu()
    reset_mainframe()
    main_frame.grid(row=1, column=0, columnspan=3, pady=(80, 0))
    if type == 'density':
        density()
    elif type == 'std':
        standard_deviation()

def density(values=False):
    from formulas.density import density
    option_title.config(text='Density')
    Label(main_frame, text='Density (g/cm³)', bg="#4B5267", fg="white").grid(row=1, column=0, padx=(40, 0), pady=(15, 0))
    density_entry = ctk.CTkEntry(main_frame, width=80)
    density_entry.grid(row=2, column=0, pady=(15, 0), padx=(35, 0))
    Label(main_frame, text='Mass (g)', bg="#4B5267", fg="white").grid(row=1, column=1, pady=(15, 0))
    mass_entry = ctk.CTkEntry(main_frame, width=80)
    mass_entry.grid(row=2, column=1, pady=(15, 0), padx=(0, 0))
    Label(main_frame, text='Volume (ml)', bg="#4B5267", fg="white").grid(row=1, column=2, pady=(15, 0))
    volume_entry = ctk.CTkEntry(main_frame, width=80)
    volume_entry.grid(row=2, column=2, pady=(15, 0), padx=(0, 0))
    for n, i in enumerate((density_entry, mass_entry, volume_entry)):
        if values:
            i.insert(0, values[n])
        else:
            i.insert(0, '0')
    ctk.CTkButton(main_frame, text='Calculate', width=80, command=lambda: results('density', density(float(density_entry.get()), float(mass_entry.get()), float(volume_entry.get())))).grid(row=3, column=0, columnspan=3, pady=(15, 0), padx=(40, 0))
    ctk.CTkButton(main_frame, text='Close', width=80, command=close_calculator).grid(row=4, column=0, columnspan=3, pady=(15, 0), padx=(40, 0))
    
def standard_deviation():
    option_title.config(text='Standard Deviation', font=('Input', 13))
    ctk.CTkLabel(main_frame, text='Number:').grid(row=1)
    numbers_entry = ctk.CTkEntry(main_frame, textvariable=entry_var, width=180)
    numbers_entry.grid(row=2, column=0, padx=(15, 10))
    add_numbers = ctk.CTkButton(main_frame, text='Add', width=100, command=lambda: [check_if_number(numbers_entry.get()), entry_var.set('')])
    add_numbers.grid(row=2, column=1)

def menu():
    global menu_open
    if warning_label.winfo_ismapped() == 1: 
        warning_label.grid_forget()
    if menu_open == False:
        menu_frame.grid(row=1, column=0, columnspan=2)
        option_title.grid_forget()
        main_frame.grid_forget()
        menu_open = True 
    elif menu_open == True:
        option_title.grid(row=0, column=1, pady=(15, 0), sticky='w')
        menu_frame.grid_forget()
        if option_title['text'] != 'Normal':
            main_frame.grid(row=1, column=0, columnspan=3, pady=(80, 0))
        menu_open = False

menu_frame = ctk.CTkFrame(root, width=280, height=1980, fg_color='#171c2f')
main_frame = ctk.CTkFrame(root, width=280, height=1980, fg_color='#4B5267')
warning_label = ctk.CTkLabel(main_frame, text='Error')

# Config menu

option_title = Label(root,
                text="Normal",
                bg='#4B5267',
                fg='white',
                font=('Input', 15))
option_title.grid(row=0, column=1, columnspan=2, pady=(15, 0), sticky='w')

Button(root,
    image=menu_img,
    bg='#4B5267',
    bd=0,
    activebackground='#4B5267',
    cursor='hand2',
    command=menu).grid(row=0, column=0, padx=25, pady=(15, 0), sticky='w')

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
    command=language_menu,
    bd=0).grid(row=1, column=0, ipadx=15, pady=(0, 10), sticky='w')

Label(menu_frame,
    text="Calculator",
    bg='#171c2f',
    fg='white',
    font=('Input', 12)).grid(row=3, column=0, padx=(15, 185), pady=(15, 10))
Button(menu_frame,
    text="• Standard Deviation",
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
    text="• Relative and absolute error",
    bg='#171c2f',
    fg='white',
    font=('Input', 8),
    activebackground='#171c2f',
    activeforeground='white',
    cursor='hand2',
    bd=0,
    command=lambda: open_calculator('errors')).grid(row=7, column=0, ipadx=15, pady=(0, 20), sticky='w')
root.mainloop()