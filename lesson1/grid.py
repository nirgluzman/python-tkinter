import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Example")

# label
label = tk.Label(root, text="Hello World", font=("Arial", 24))
label.pack(padx=20, pady=20)

# frame for buttons
buttons_frame = tk.Frame(root, relief=tk.SOLID, bd=1)

# make columns equal width by distributing available space evenly
buttons_frame.columnconfigure(0, weight=1)
buttons_frame.columnconfigure(1, weight=1)
buttons_frame.columnconfigure(2, weight=1)

# create 2x3 grid of numbered buttons
buttons = []
num = 1
for row in range(2):
    row_buttons = []
    for col in range(3):
        btn = tk.Button(
            buttons_frame, text=str(num), font=("Arial", 18), relief=tk.SOLID, bd=1
        )
        btn.grid(row=row, column=col, sticky=tk.W + tk.E)
        row_buttons.append(btn)
        num += 1
    buttons.append(row_buttons)


buttons_frame.pack(
    padx=20,
    pady=20,
    fill=tk.X,  # how the widget expands to fill available space (X=horizontal, Y=vertical, BOTH=both directions)
)

root.mainloop()
