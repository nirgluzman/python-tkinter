import tkinter as tk
from tkinter import ttk  # themed widget submodule

# Main window of the application
root = tk.Tk()
root.title("Simple App!")

# Set the size of the main window
root.geometry("600x400")

# Configure the grid layout of the root window to make it resizable
# root.rowconfigure(0, weight=1) makes the first row (index 0) expandable with a weight of 1
# This means when the window is resized vertically, the first row will grow to fill the extra space
# root.columnconfigure(0, weight=1) makes the first column (index 0) expandable with a weight of 1
# This means when the window is resized horizontally, the first column will grow to fill the extra space
# The weight parameter determines how much space each row/column gets relative to others (higher weight = more space)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


def add_to_list(event=None):
    item = entry.get()
    if item:
        text_list.insert(tk.END, item)

        # Clear the entry field after adding the item to the list
        entry.delete(0, tk.END)


# Create a frame (container widget) and add it to the main window
frame = ttk.Frame(
    master=root,
)

# Place the frame in the grid layout of the root window at row 0, column 0
frame.grid(
    row=0,
    column=0,
    sticky="nsew",  # Make the frame fill the entire cell of the grid
    padx=5,  # Add horizontal padding around the frame
    pady=5,  # Add vertical padding around the frame
)

# Configure the grid layout of the frame to make it resizable
# Configure the first column (index 0) of the frame to be expandable with weight=1
# This allows the entry widget in column 0 to expand horizontally when the window is resized
frame.columnconfigure(0, weight=1)

# Configure the second row (index 1) of the frame to be expandable with weight=1
frame.rowconfigure(1, weight=1)

# Create a single-line text input field where users can type text
entry = ttk.Entry(master=frame)
entry.grid(
    row=0,
    column=0,
    sticky="ew",  # Make the entry expand horizontally within its grid cell
)

# Bind the Enter key to the add_to_list function
entry.bind("<Return>", add_to_list)

# Create a Submit button and bind it to the add_to_list function
entry_btn = ttk.Button(master=frame, text="Submit", command=add_to_list)
entry_btn.grid(row=0, column=1)

# Create a Listbox widget to display a list of items
text_list = tk.Listbox(master=frame)
text_list.grid(
    row=1,
    column=0,
    columnspan=2,  # Span the Listbox across two columns to align with the entry and button
    sticky="nsew",  # Make the Listbox expand to fill the available space in the grid cell
)

# Start the main event loop
root.mainloop()
