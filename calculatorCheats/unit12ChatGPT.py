import os
from tkinter import mess
import tkinter as tk

# Define the update function
def update_python():
    os.system('sudo apt-get update')
    os.system('sudo apt-get install python3')
    tk.messagebox.showinfo('Update', 'Python has been updated successfully!')

# Create the GUI
root = tk.Tk()
root.title('Python Updater')

# Add a label
label = tk.Label(root, text='Click the button to update Python')
label.pack(pady=10)

# Add a button to update Python
button = tk.Button(root, text='Update Python', command=update_python)
button.pack()

# Start the main event loop
root.mainloop()
