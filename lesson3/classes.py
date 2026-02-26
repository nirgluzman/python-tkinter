# Tkinter class-based application demonstrating layout managers (grid, pack, place) and widget organization

import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()

        # Set the window title
        self.title(title)

        # Configure window dimensions and minimum size
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # Widgets
        self.menu = Menu(self)
        self.main = Main(self)

        # Run the main event loop
        self.mainloop()


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Place the menu frame on the left side of the window
        self.place(x=0, y=0, relwidth=0.3, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        # Create the widgets
        menu_button1 = ttk.Button(self, text="Button 1")
        menu_button2 = ttk.Button(self, text="Button 2")
        menu_button3 = ttk.Button(self, text="Button 3")

        menu_slider1 = ttk.Scale(self, orient=tk.VERTICAL)
        menu_slider2 = ttk.Scale(self, orient=tk.VERTICAL)

        toggle_frame = ttk.Frame(self)
        menu_toggle1 = ttk.Checkbutton(toggle_frame, text="Check 1")
        menu_toggle2 = ttk.Checkbutton(toggle_frame, text="Check 2")

        entry = ttk.Entry(self)

        # Create the grid
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        # Place the widgets in the grid
        menu_button1.grid(row=0, column=0, columnspan=2, sticky="nsew")
        menu_button2.grid(row=0, column=2, sticky="nsew")
        menu_button3.grid(row=1, column=0, columnspan=3, sticky="nsew")

        menu_slider1.grid(row=2, column=0, rowspan=2, sticky="nsew", pady=20)
        menu_slider2.grid(row=2, column=2, rowspan=2, sticky="nsew", pady=20)

        toggle_frame.grid(row=4, column=0, columnspan=3, sticky="nsew")
        menu_toggle1.pack(side="left", expand=True)
        menu_toggle2.pack(side="left", expand=True)

        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Place the main frame on the right side of the window
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        Entry(self, "Entry 1", "Button 1", label_bg="lightgreen")
        Entry(self, "Entry 2", "Button 2", label_bg="lightblue")


class Entry(ttk.Frame):
    def __init__(self, parent, label_text, button_text, label_bg="lightgray"):
        super().__init__(parent)

        label = ttk.Label(
            self,
            background=label_bg,
            text=label_text,
            font=("Arial", 24),
            anchor="center",
        )
        button = ttk.Button(self, text=button_text)

        label.pack(expand=True, fill="both")
        button.pack(expand=True, fill="both", pady=10)

        self.pack(side="left", expand=True, fill="both", padx=10)


App("Class-Based Application", (600, 600))
