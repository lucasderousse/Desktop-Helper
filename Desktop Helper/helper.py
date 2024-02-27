import tkinter as tk
from datetime import datetime
from tkinterdnd2 import TkinterDnD

defaultFont = ("Ubuntu", 20)

# Function to update the label with current date and time
def update_datetime():
    current_datetime = datetime.now().strftime("%B %d, %Y %H:%M:%S")
    datetime_label.config(text=current_datetime)
    # Schedule the next update after 1000 milliseconds (1 second)
    root.after(1000, update_datetime)

# Create the main application window
root = tk.Tk()
root.title("Bot")

# Set the size of the window
root.geometry("800x600")  # Width x Height
root.configure(bg="#1d0074")

# Create a label widget
label = tk.Label(root, text="Hello, World!", bg="#1d0074")
label.configure(font = defaultFont)

# datetime label
datetime_label = tk.Label(root, text="", font=("Ubuntu", 15), bg="#1d0074")
datetime_label.pack(pady=5, anchor="ne")
update_datetime()

# Create a button widget
button = tk.Button(root, text="I fuckin suck at coding")
button.place(x=50, y=100)

# Define a function to be called when the button is clicked
def button_click():
    label.config(text="It works!")

# Bind the button click event to the function
button.config(command=button_click)

# Start the Tkinter event loop
root.mainloop()