import tkinter as tk

root = tk.Tk()
root.geometry("150x100")

#var_1 = tk.StringVar()  # skapar en sträng variable
var_1 = tk.IntVar()     # skapar en heltal variabel
#var_1 = tk.BooleanVar() # den kan vara True eller False
var_1.set(2)

r1 = tk.Radiobutton(root, text="Först", variable=var_1, value=1)
r2 = tk.Radiobutton(root, text="Andra", variable=var_1, value=2)
r3 = tk.Radiobutton(root, text="Tredje", variable=var_1, value=3)

r1.pack(anchor='w')
r2.pack(anchor='w')
r3.pack(anchor='w')


root.mainloop()
