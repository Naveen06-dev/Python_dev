import tkinter as tk

class Whiteboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Whiteboard")
    
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()

        self.old_x = None
        self.old_y = None

        self.canvas.bind('<B1-Motion>', self.paint)  
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, 
                                    width=5, fill='black', capstyle=tk.ROUND, smooth=tk.TRUE)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

if __name__ == "__main__":
    root = tk.Tk()
    whiteboard = Whiteboard(root)
    root.mainloop()
