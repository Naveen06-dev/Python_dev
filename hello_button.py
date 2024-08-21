import tkinter as tk

def on_button_click():
    print("Hello Button Clicked!")

def create_3d_button(root):
    button = tk.Button(root, text="Hello", font=('Helvetica', 16), 
                       relief=tk.RAISED, bd=5, 
                       command=on_button_click)
    button.pack(padx=10, pady=10)
    return button

def main():
    root = tk.Tk()
    root.title("3D Button Example")

    create_3d_button(root)

    root.mainloop()

if __name__ == "__main__":
    main()
