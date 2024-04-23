import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Widgets")
root.geometry("400x200")

name_label = tk.Label(root, text="Ange ditt namn:", font=("Arial", 14))
name_label.pack(side="left", padx=5, pady=10)

name_entry = tk.Entry(root, width=20)
name_entry.pack(side="left", padx=5, pady=10)

x_choice = tk.StringVar()
rbutton_1 = tk.Radiobutton(root, text="Python", variable=x_choice, value="python")
rbutton_2 = tk.Radiobutton(root, text="JavaScript", variable=x_choice, value="javascript")
rbutton_3 = tk.Radiobutton(root, text="Java", variable=x_choice, value="java")

rbutton_1.pack(padx=5, pady=10, side="bottom")
rbutton_2.pack(padx=5, pady=10, side="bottom")
rbutton_3.pack(padx=5, pady=10, side="bottom")


root.mainloop()