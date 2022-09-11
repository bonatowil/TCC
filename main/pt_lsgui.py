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
language_var.set('Português')

menu_open = False
calc_open = False

def language_change(language):
    if language == 'English':
        root.destroy()
        import en_lsgui
    elif language == 'Português':
        pass
        
def language_menu():
    global menu_open
    menu_open = True
    open_menu()
    for widget in main_frame.winfo_children():
        widget.destroy()
    option_title.config(text='Idioma')
    main_frame.grid(row=1, column=0, columnspan=3, pady=(60, 0))
    ctk.CTkOptionMenu(main_frame, values=['English', 'Português'], variable=language_var).grid(row=1, column=0, padx=(30, 0))
    ctk.CTkButton(main_frame, text='Salvar', width=100, command= lambda: language_change(language_var.get())).grid(row=1, column=1, padx=10)

def results(all):
    open_calculator('density', all)

def close_calculator():
    option_title.config(text='Padrão')
    main_frame.grid_forget()
    open_menu()

def open_calculator(type, values=False):
    global menu_open
    menu_open = True
    for widget in main_frame.winfo_children():
        widget.destroy()
    open_menu()
    if type == 'density':
        from formulas.density import density
        global calc_open
        calc_open = True
        main_frame.grid(row=1, column=0, columnspan=3, pady=(60, 0))
        option_title.config(text='Densidade')
        Label(main_frame, text='Densidade \n(g/cm³)', bg="#4B5267", fg="white").grid(row=1, column=0, padx=(40, 0), pady=(15, 0))
        density_entry = ctk.CTkEntry(main_frame, width=80)
        density_entry.grid(row=2, column=0, pady=(15, 0), padx=(35, 0))
        Label(main_frame, text='Massa (g)', bg="#4B5267", fg="white").grid(row=1, column=1, pady=(15, 0))
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
        ctk.CTkButton(main_frame, text='Calcular', width=80, command=lambda: results(density(float(density_entry.get()), float(mass_entry.get()), float(volume_entry.get())))).grid(row=3, column=0, columnspan=3, pady=(15, 0), padx=(40, 0))
        ctk.CTkButton(main_frame, text='Fechar', width=80, command=close_calculator).grid(row=4, column=0, columnspan=3, pady=(15, 0), padx=(40, 0))

def open_menu():
    global menu_open
    if menu_open == False:
        menu_frame.grid(row=1, column=0, columnspan=2)
        option_title.grid_forget()
        main_frame.grid_forget()
        menu_open = True 
    elif menu_open == True:
        option_title.grid(row=0, column=1, pady=(15, 0), sticky='w')
        menu_frame.grid_forget()
        if option_title['text'] != 'Padrão':
            main_frame.grid(row=1, column=0, columnspan=3, pady=(60, 0))
        menu_open = False

menu_frame = ctk.CTkFrame(root, width=280, height=1980, fg_color='#171c2f')
main_frame = ctk.CTkFrame(root, width=280, height=1980, fg_color='#4B5267')

# Config menu

option_title = Label(root,
                text="Padrão",
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
    command=open_menu).grid(row=0, column=0, padx=25, pady=(15, 0), sticky='w')

Label(menu_frame,
    text="Opções",
    bg='#171c2f',
    fg='white',
    font=('Input', 12)).grid(row=0, column=0, padx=(0, 200), pady=(15, 10))
Button(menu_frame,
    text="• Idioma",
    bg='#171c2f',
    fg='white',
    font=('Input', 8),
    activebackground='#171c2f',
    activeforeground='white',
    cursor='hand2',
    command=language_menu,
    bd=0).grid(row=1, column=0, ipadx=15, pady=(0, 10), sticky='w')

Label(menu_frame,
    text="Calculadora",
    bg='#171c2f',
    fg='white',
    font=('Input', 12)).grid(row=3, column=0, padx=(15, 185), pady=(15, 10))
Button(menu_frame,
    text="• Desvio Padrão",
    bg='#171c2f',
    fg='white',
    font=('Input', 8),
    activebackground='#171c2f',
    activeforeground='white',
    cursor='hand2',
    bd=0,
    command=lambda: open_calculator('std')).grid(row=4, column=0, ipadx=15, pady=(0, 10), sticky='w')
Button(menu_frame,
    text="• Coeficiente de variação",
    bg='#171c2f',
    fg='white',
    font=('Input', 8),
    activebackground='#171c2f',
    activeforeground='white',
    cursor='hand2',
    bd=0,
    command=lambda: open_calculator('cv')).grid(row=5, column=0, ipadx=15, pady=(0, 10), sticky='w')
Button(menu_frame,
    text="• Densidade",
    bg='#171c2f',
    fg='white',
    font=('Input', 8),
    activebackground='#171c2f',
    activeforeground='white',
    cursor='hand2',
    bd=0,
    command=lambda: open_calculator('density')).grid(row=6, column=0, ipadx=15, pady=(0, 10), sticky='w')
Button(menu_frame,
    text="• Erro relativo e absoluto",
    bg='#171c2f',
    fg='white',
    font=('Input', 8),
    activebackground='#171c2f',
    activeforeground='white',
    cursor='hand2',
    bd=0,
    command=lambda: open_calculator('errors')).grid(row=7, column=0, ipadx=15, pady=(0, 20), sticky='w')

root.mainloop()