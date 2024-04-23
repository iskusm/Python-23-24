# LISTBOX-widget
import tkinter as tk

root = tk.Tk()

l_elever = ['Mario', 'Viggo', 'Lina', 'Mert']

lbox = tk.Listbox(root, width=15, height=8)
lbox.pack(side=tk.LEFT)

for i in l_elever:
    lbox.insert(0, i)

# Vi skapar en frame
def läggtill():
    lbox.insert(tk.END, entry.get())
    entry.delete(0, tk.END)

def tabort():
    selekt = list(lbox.curselection())
    selekt.reverse()
    
    for i in selekt:
        lbox.delete(i)

def spara():
    f = open("list001.txt", "w")
    f.writelines("\n".join(lbox.get(0, tk.END)))
    f.close()

frame = tk.Frame()
frame.pack(side=tk.LEFT)

entry = tk.Entry(frame, width=15)
entry.pack(padx=5)

btn1 = tk.Button(frame, text="Lägg till", command=läggtill)
btn2 = tk.Button(frame, text="Ta bort", command=tabort)
btn3 = tk.Button(frame, text="Spara", command=spara)

btn1.pack(fill=tk.X, padx=5)
btn2.pack(fill=tk.X, padx=5)
btn3.pack(fill=tk.X, padx=5)

root.mainloop()
