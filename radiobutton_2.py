import tkinter as tk

root = tk.Tk()
root.geometry("150x300")

def byt():
    if var.get() == 1:
        # lbl['bg'] = 'red'
        lbl.config(bg='red')
    elif var.get() == 2:
        # lbl['bg'] = 'green'
        lbl.config(bg='green')
    elif var.get() == 3:
        # lbl['bg'] = 'blue'
        lbl.config(bg='blue')


var = tk.IntVar()
var.set(1)

röd = tk.Radiobutton(root, text="Röd", variable=var, value=1)
grön = tk.Radiobutton(root, text="Grön", variable=var, value=2)
blå = tk.Radiobutton(root, text="Blå", variable=var, value=3)

btn = tk.Button(root, text="Byt färg", command=byt)
lbl = tk.Label(root, width=20, height=10)

röd.pack(anchor='w')
grön.pack(anchor='w')
blå.pack(anchor='w')
btn.pack()
lbl.pack(fill='both')

root.mainloop()