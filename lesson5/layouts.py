# Tkinter Layout sample app:
# demonstrates the three layout managers (pack, grid, place) for positioning widgets

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Layout intro")
window.geometry("600x400")
window.minsize(600, 400)

# widgets
label1 = ttk.Label(window, text="Label 1", background="red")
label2 = ttk.Label(window, text="Label 2", background="green")

#########################
# pack
#########################
# label1.pack(side=tk.LEFT, expand=True, fill=tk.X)
# label2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

#########################
# grid
#########################
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)  # 2 times more space than the other columns
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)

# label1.grid(
#     row=0,
#     column=0,
#     sticky="n",  # stick to the north (top) of the cell
# )
# label2.grid(
#     row=1,
#     column=1,
#     columnspan=2,  # span across 2 columns
#     sticky="nsew",  # stick to all sides of the cell (north, south, east, west)
# )

#########################
# place
#########################
label1.place(
    x=0,
    y=0,  # top left corner of the label will be at (0, 0)
    width=100,  # the label will be 100 pixels wide
    height=50,  # the label will be 50 pixels tall
)

label2.place(
    relx=0.5,  # the center of the label will be at 50% of the window's width
    rely=0.5,  # the center of the label will be at 50% of the window's height
    anchor=tk.CENTER,  # the anchor point is the center of the label
)


# run
window.mainloop()
