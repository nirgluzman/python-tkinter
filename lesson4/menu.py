# Tkinter menu sample code:
# demonstrates creating menu bars, submenus, menu items, checkbuttons, and menu buttons
# https://www.tutorialspoint.com/python/tk_menu.htm

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry("600x400")
window.minsize(600, 400)
window.title("Menu Application")

# menu
menu_bar = tk.Menu(master=window)

# File sub menu
file_menu = tk.Menu(
    master=menu_bar,
    tearoff=False,  # prevent the menu from being separated from the menu bar
)
file_menu.add_command(label="New", command=lambda: print("New file"))
file_menu.add_command(label="Open", command=lambda: print("Open file"))
file_menu.add_separator()  # add a line to separate the menu items
menu_bar.add_cascade(label="File", menu=file_menu)

# Help sub menu
help_menu = tk.Menu(
    master=menu_bar,
    tearoff=False,
)
help_menu.add_command(label="About", command=lambda: print("About this application"))

# create a StringVar to hold the state of the checkbutton (default is "on")
help_check_string = tk.StringVar(value="on")
help_menu.add_checkbutton(
    label="Show tips",
    onvalue="on",
    offvalue="off",
    variable=help_check_string,
    command=lambda: print(f"Show tips: {help_check_string.get()}"),
)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Exercise sub menu
exercise_menu = tk.Menu(master=menu_bar, tearoff=False)
exercise_menu.add_command(label="Exercise 1", command=lambda: print("Exercise 1"))
exercise_menu.add_command(label="Exercise 2", command=lambda: print("Exercise 2"))
menu_bar.add_cascade(label="Exercises", menu=exercise_menu)

exercise_sub_menu = tk.Menu(master=exercise_menu, tearoff=False)
exercise_sub_menu.add_command(
    label="Sub Exercise 1.1", command=lambda: print("Sub Exercise 1.1")
)
exercise_sub_menu.add_command(
    label="Sub Exercise 1.2", command=lambda: print("Sub Exercise 1.2")
)
exercise_menu.add_cascade(label="Sub Exercises", menu=exercise_sub_menu)

# display the menu bar
window.configure(menu=menu_bar)

# menu button
menu_button = ttk.Menubutton(master=window, text="Options")
menu_button.pack(pady=20)  # display the menu button with some padding

menu_button_options = tk.Menu(master=menu_button, tearoff=False)
menu_button_options.add_command(label="Option 1", command=lambda: print("Option 1"))
menu_button_options.add_checkbutton(label="Check 1")

menu_button.configure(
    menu=menu_button_options
)  # associate the options with the menu button

# menu_button["menu"] = (
#     menu_button_options  # alternative way to associate the options with the menu button
# )

# run
window.mainloop()
