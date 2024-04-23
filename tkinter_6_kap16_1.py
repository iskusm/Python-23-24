import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

def avslut():
    root.destroy()

titeln = tk.Label(frame, text="Vad vill du göra?", font=("comic sans", 16), bd=2)
titeln.grid(row=0, column=0, columnspan=2, pady=5)

menu_item = tk.IntVar()
menu_item.set(-1)
tk.Radiobutton(frame, text="lägga till eller ändra en adress",
               variable=menu_item, value=1).grid(row=1, column=0, sticky='w')
tk.Radiobutton(frame, text="söka en adress",
               variable=menu_item, value=2).grid(row=2, column=0, sticky='w')
tk.Radiobutton(frame, text="ta bort en adress ur listan",
               variable=menu_item, value=3).grid(row=3, column=0, sticky='w')
tk.Radiobutton(frame, text="visa hela registret",
               variable=menu_item, value=4).grid(row=4, column=0, sticky='w')
tk.Radiobutton(frame, text="avsluta",
               variable=menu_item, value=0, command=avslut).grid(row=5, column=0, sticky='w')


root.mainloop()