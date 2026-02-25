import tkinter as tk

# Main window of the application
root = tk.Tk()
root.title("Simple App!")

# Create a button widget; root is the parent container for the button.
btn = tk.Button(master=root, text="Click Me!", command=lambda: print("Button Clicked!"))

# Add the button to the window using grid layout manager
# grid() positions widgets in a table-like structure with rows and columns
btn.grid(row=1, column=0)

# Create a label widget to display text; it is also a child of the root window.
lbl = tk.Label(master=root, text="Label")
lbl.grid(row=0, column=0)

# Print the configuration options of the label widget
print(lbl.config().keys())

# Start the main event loop of the tkinter application.
# It continuously listens for events like button clicks, key presses, window resizing, etc.
# The program will remain running until the user closes the window or calls root.quit().
# Without this line, the window would appear briefly and then immediately close.
root.mainloop()
