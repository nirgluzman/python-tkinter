import tkinter as tk
from tkinter import ttk  # themed widget submodule


def main():
    app = Application()
    app.mainloop()


class Application(tk.Tk):
    def __init__(self):
        # Initialize the parent class (tk.Tk) to set up the main application window
        super().__init__()

        # Set the title
        self.title("Tkinter Class Example")

        # Set the size of the main window
        self.geometry("600x400")

        # Configure grid layout: row 0 expands vertically, column 0 expands horizontally, column 1 expands 3x more than column 0
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        # Create two instances of the InputForm class and place it in the grid
        self.input_form1 = InputForm(self)
        self.input_form1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.input_form2 = InputForm(self)
        self.input_form2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)


class InputForm(ttk.Frame):
    def __init__(
        self,
        parent,  # parent widget that will contain this
    ):
        # Initialize the parent class (ttk.Frame) to set up the frame within the parent widget
        super().__init__(master=parent)

        # Configure grid layout: column 0 expands horizontally, row 1 expands vertically
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Create a single-line text input field where users can type text
        self.entry = ttk.Entry(master=self)
        self.entry.grid(
            row=0,
            column=0,
            sticky="ew",  # Make the entry expand horizontally within its grid cell
        )

        # Bind the Enter key to the add_to_list function
        self.entry.bind("<Return>", self.add_to_list)

        # Create an "Add" button and bind it to the add_to_list function
        self.add_btn = ttk.Button(master=self, text="Add", command=self.add_to_list)
        self.add_btn.grid(row=0, column=1)

        # Create a "Clear" button to clear the Listbox
        self.clear_btn = ttk.Button(
            master=self, text="Clear", command=lambda: self.text_list.delete(0, tk.END)
        )
        self.clear_btn.grid(row=0, column=2)

        # Create a Listbox widget to display a list of items
        self.text_list = tk.Listbox(master=self)

        self.text_list.grid(
            row=1,
            column=0,
            columnspan=3,  # Span the Listbox across three columns to align with the entry and buttons
            sticky="nsew",  # Make the Listbox expand to fill the available space in the grid cell
        )

    def add_to_list(self, _event=None):
        item = self.entry.get()
        if item:
            self.text_list.insert(tk.END, item)

            # Clear the entry field after adding the item to the list
            self.entry.delete(0, tk.END)


if __name__ == "__main__":
    # This ensures the application only runs when the script is executed directly, not when imported
    # as a module in another script
    main()
