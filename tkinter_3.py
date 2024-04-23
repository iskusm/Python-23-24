import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Widgets")
root.geometry("400x200")

def logga_in():
    message = f"Du har angett namn {name_entry.get()}"
    messagebox.showinfo("Information", message)

name_label = tk.Label(root, text="Ange ditt namn:", font=("Arial", 14))
name_entry = tk.Entry(root, width=30)

pwd_label = tk.Label(root, text="Ange lösenord:", font=("Arial", 14))
pwd_entry = tk.Entry(root, width=30)

login_button = tk.Button(root, text="Logga in", font=("Helvetica", 13), command=logga_in)

name_label.grid(row=0, column=0, padx=5, pady=10)
name_entry.grid(row=0, column=1, padx=5, pady=10)
pwd_label.grid(row=1, column=0, padx=5, pady=10)
pwd_entry.grid(row=1, column=1, padx=5, pady=10)
login_button.grid(row=2, column=1, padx=5, pady=10)

root.mainloop()
