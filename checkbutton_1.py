import tkinter as tk

root = tk.Tk()

var1 = tk.IntVar()
var1.set(0)


def visa():
    if var1.get() == 1:
        var2.set(0)
        lbl.config(text="Python")
    elif var2.get() == 1:
        var1.set(0)
        lbl.config(text="JavaScript")


ch1 = tk.Checkbutton(root, text="Python", variable=var1,
                     onvalue=1, offvalue=0,
                     command=visa)
ch1.pack(anchor='w', padx=5)

var2 = tk.IntVar()
var2.set(0)

ch2 = tk.Checkbutton(root, text="JavaScript", variable=var2,
                     onvalue=1, offvalue=0,
                     command=visa)
ch2.pack(anchor='w', padx=5)

lbl = tk.Label(root, width=20, height=10, bg='lightblue')
lbl.pack()


root.mainloop()