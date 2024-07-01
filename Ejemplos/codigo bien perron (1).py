from tkinter import *

# Create the main window
window = Tk()
window.title("NUTRIWANKA")
window.geometry("960x600")

# Create the menu bar
menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=None)
filemenu.add_command(label="Save", command=None)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=None)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=None)
editmenu.add_command(label="Copy", command=None)
editmenu.add_command(label="Paste", command=None)
editmenu.add_command(label="Delete", command=None)
menubar.add_cascade(label="Edit", menu=editmenu)

# Create the main frame
mainframe = Frame(window)
mainframe.pack(fill=BOTH, expand=True)

# Create the top frame
topframe = Frame(mainframe, pady=10)

title = Label(topframe, text="NUTRIWANKA", font=("Arial", 24))
title.pack(side=LEFT)

product_icon = Label(topframe, text="Productos", font=("Arial", 12), fg="gray")
product_icon.pack(side=RIGHT, padx=20)

recipe_icon = Label(topframe, text="Recetario", font=("Arial", 12), fg="gray")
recipe_icon.pack(side=RIGHT, padx=20)

payment_icon = Label(topframe, text="Pago", font=("Arial", 12), fg="gray")
payment_icon.pack(side=RIGHT, padx=20)

topframe.pack(fill=X)

# Create the left frame
leftframe = Frame(mainframe, width=150)
leftframe.pack(side=LEFT, fill=Y, padx=10)

# Create the menu buttons
cliente_button = Button(leftframe, text="Cliente", width=10, command=None)
cliente_button.pack(pady=5)

proveedor_button = Button(leftframe, text="Proveedor", width=10, command=None)
proveedor_button.pack(pady=5)

admin_button = Button(leftframe, text="Administrador", width=10, command=None)
admin_button.pack(pady=5)

# Create the right frame
rightframe = Frame(mainframe, width=400)
rightframe.pack(side=LEFT, fill=BOTH, expand=True, padx=10)

# Create the form
name_label = Label(rightframe, text="Nombre:", font=("Arial", 12))
name_label.grid(row=0, column=0, sticky=W, pady=10)
name_entry = Entry(rightframe, width=30)
name_entry.grid(row=0, column=1, columnspan=2, sticky=W, pady=10)

last_name_label = Label(rightframe, text="Apellidos:", font=("Arial", 12))
last_name_label.grid(row=1, column=0, sticky=W, pady=10)
last_name_entry = Entry(rightframe, width=30)
last_name_entry.grid(row=1, column=1, columnspan=2, sticky=W, pady=10)

email_label = Label(rightframe, text="Correo electrónico:", font=("Arial", 12))
email_label.grid(row=2, column=0, sticky=W, pady=10)
email_entry = Entry(rightframe, width=30)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W, pady=10)

gender_label = Label(rightframe, text="Género:", font=("Arial", 12))
gender_label.grid(row=3, column=0, sticky=W, pady=10)
gender_var = StringVar(rightframe)
gender_var.set("Hombre")
gender_optionmenu = OptionMenu(rightframe, gender_var, "Hombre", "Mujer", "Indefinido")
gender_optionmenu.grid(row=3, column=1, sticky=W, pady=10)

phone_label = Label(rightframe, text="Numero Telefónico:", font=("Arial", 12))
phone_label.grid(row=4, column=0, sticky=W, pady=10)
phone_entry = Entry(rightframe, width=30)
phone_entry.grid(row=4, column=1, columnspan=2, sticky=W, pady=10)

password_label = Label(rightframe, text="Contraseña:", font=("Arial", 12))
password_label.grid(row=5, column=0, sticky=W, pady=10)
password_entry = Entry(rightframe, width=30, show="*")
password_entry.grid(row=5, column=1, columnspan=2, sticky=W, pady=10)

birth_date_label = Label(rightframe, text="Fecha de nacimiento:", font=("Arial", 12))
birth_date_label.grid(row=6, column=0, sticky=W, pady=10)
day_label = Label(rightframe, text="Día", font=("Arial", 10))
day_label.grid(row=6, column=1, sticky=W, pady=10)
day_entry = Entry(rightframe, width=5)
day_entry.grid(row=6, column=1, sticky=E, padx=5)

month_label = Label(rightframe, text="Mes", font=("Arial", 10))
month_label.grid(row=6, column=2, sticky=W, pady=10)
month_entry = Entry(rightframe, width=5)
month_entry.grid(row=6, column=2, sticky=E, padx=5)

year_label = Label(rightframe, text="Año", font=("Arial", 10))
year_label.grid(row=6, column=3, sticky=W, pady=10)
year_entry = Entry(rightframe, width=5)
year_entry.grid(row=6, column=3, sticky=E, padx=5)

products_label = Label(rightframe, text="Productos:", font=("Arial", 12))
products_label.grid(row=7, column=0, sticky=W, pady=10)
products_entry = Entry(rightframe, width=30)
products_entry.grid(row=7, column=1, columnspan=2, sticky=W, pady=10)

card_label = Label(rightframe, text="Nr Tarjeta:", font=("Arial", 12))
card_label.grid(row=8, column=0, sticky=W, pady=10)
card_entry = Entry(rightframe, width=30)
card_entry.grid(row=8, column=1, columnspan=2, sticky=W, pady=10)

# Create the accept button
accept_button = Button(rightframe, text="Aceptar", command=None)
accept_button.grid(row=9, column=0, columnspan=2, sticky=W, pady=10)

# Configure the menu bar
window.config(menu=menubar)

# Start the main loop
window.mainloop()
