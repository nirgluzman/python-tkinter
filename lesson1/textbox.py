import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Example")

# label
label = tk.Label(root, text="Hello World", font=("Arial", 24))
label.pack(padx=20, pady=20)

# multiline text box
textbox = tk.Text(root, height=10, width=30, font=("Arial", 14))
textbox.pack(padx=20, pady=20)

# single line text box
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(padx=20, pady=20)

root.mainloop()
