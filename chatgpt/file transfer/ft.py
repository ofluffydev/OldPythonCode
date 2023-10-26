import tkinter as tk
from tkinter import filedialog
from shutil import copy2
import os

class FileCopyApp:
    def __init__(self, root):
        self.root = root
        self.source_dir = tk.StringVar()
        self.destination_dir = tk.StringVar()
        self.setup_gui()

    def setup_gui(self):
        self.root.title("File Copy App")
        self.root.configure(bg='#BBDEFB')

        tk.Label(self.root, text="Source Directory", bg='#BBDEFB').grid(row=0, column=0)
        tk.Label(self.root, text="Destination Directory", bg='#BBDEFB').grid(row=1, column=0)

        tk.Entry(self.root, textvariable=self.source_dir).grid(row=0, column=1)
        tk.Entry(self.root, textvariable=self.destination_dir).grid(row=1, column=1)

        tk.Button(self.root, text="Browse...", command=self.browse_source, bg='#90CAF9', fg='white').grid(row=0, column=2)
        tk.Button(self.root, text="Browse...", command=self.browse_destination, bg='#90CAF9', fg='white').grid(row=1, column=2)

        tk.Button(self.root, text="Copy Files", command=self.copy_files, bg='#90CAF9', fg='white').grid(row=2, column=1)

    def browse_source(self):
        self.source_dir.set(filedialog.askdirectory())

    def browse_destination(self):
        self.destination_dir.set(filedialog.askdirectory())

    def copy_files(self):
        source_dir = self.source_dir.get()
        destination_dir = self.destination_dir.get()
        
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            if os.path.isfile(source_file):
                copy2(source_file, destination_dir)

        print("Files copied successfully!")

root = tk.Tk()
app = FileCopyApp(root)
root.mainloop()
