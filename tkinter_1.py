import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Min första program")
root.geometry("300x200")
root.config(bg="lightblue")


def meddelande():
    messagebox.showinfo("Meddelande", "Det gick bra att logga in")


label_1 = tk.Label(root, text="Hello, World!", font=("Helvetica", 16),
                   fg="green", bg="yellow")
label_1.pack(pady=10)

button_1 = tk.Button(root, text="Login", width=15, height=3, relief=tk.RIDGE, command=meddelande)
button_1.pack(pady=10, side="left")

button_2 = tk.Button(root, text="Avsluta", relief="ridge", width=15, height=3, command=root.destroy)
button_2.pack(padx=10, pady=10, side=tk.LEFT)


root.mainloop()