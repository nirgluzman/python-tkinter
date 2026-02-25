import tkinter as tk
from tkinter import ttk


def main():
    app = Application()
    app.mainloop()


class Application(tk.Tk):
    def __init__(self):
        super().__init__()  # initializes the parent class (tk.Tk) to set up the main application window
        self.title("Tkinter Class Example")
        self.create_widgets()

    def create_widgets(self):
        self.button = ttk.Button(self, text="Click Me", command=self.on_button_click)
        # pack() is a geometry manager that organizes widgets in blocks before placing them in the parent widget
        # pady=20 adds 20 pixels of padding above and below the button
        self.button.pack(pady=20)

    def on_button_click(self):
        print("Button clicked!")


if __name__ == "__main__":
    # This ensures the application only runs when the script is executed directly, not when imported
    # as a module in another script
    main()
