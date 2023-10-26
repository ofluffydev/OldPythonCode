import tkinter as tk

class DrawingApp:
    def __init__(self, master):
        self.master = master
        master.title("Drawing Program")

        # Create a Canvas widget
        self.canvas = tk.Canvas(master, width=500, height=500, bg='white')
        self.canvas.pack()

        # Create a button to switch between drawing modes
        self.mode_button = tk.Button(master, text='Line', command=self.switch_mode)
        self.mode_button.pack()

        # Create a button to clear the canvas
        self.clear_button = tk.Button(master, text='Clear', command=self.clear_canvas)
        self.clear_button.pack()

        # Set the initial drawing mode to 'line'
        self.mode = 'line'

        # Bind mouse events to the Canvas widget
        self.canvas.bind('<Button-1>', self.mouse_down)
        self.canvas.bind('<B1-Motion>', self.mouse_drag)
        self.canvas.bind('<ButtonRelease-1>', self.mouse_up)

        # Initialize drawing variables
        self.start_x = None
        self.start_y = None
        self.current_shape = None

    def switch_mode(self):
        # Cycle between drawing modes
        if self.mode == 'line':
            self.mode = 'rect'
            self.mode_button.config(text='Rectangle')
        elif self.mode == 'rect':
            self.mode = 'oval'
            self.mode_button.config(text='Oval')
        else:
            self.mode = 'line'
            self.mode_button.config(text='Line')

    def clear_canvas(self):
        # Clear the canvas
        self.canvas.delete('all')

    def mouse_down(self, event):
        # Save the starting position
        self.start_x = event.x
        self.start_y = event.y

    def mouse_drag(self, event):
        # Delete the previous shape (if any)
        if self.current_shape:
            self.canvas.delete(self.current_shape)

        # Draw the current shape
        if self.mode == 'line':
            self.current_shape = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y)
        elif self.mode == 'rect':
            self.current_shape = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y)
        else:
            self.current_shape = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y)

    def mouse_up(self, event):
        # Reset the starting position and current shape
        self.start_x = None
        self.start_y = None
        self.current_shape = None

root = tk.Tk()
app = DrawingApp(root)
root.mainloop()
