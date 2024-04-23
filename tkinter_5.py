# LISTBOX-widget
import tkinter as tk

root = tk.Tk()

l_elever = ['Mario', 'Viggo', 'Lina', 'Mert']

lbox = tk.Listbox(root, width=15, height=8)
lbox.pack(side=tk.LEFT, padx=5)

for i in l_elever:
    lbox.insert(0, i)

# Vi skapar en frame
def flyttright():
    select = lbox.curselection()
    lbox2.insert(tk.END, lbox.get(select))
    lbox.delete(select)

def flyttleft():
    select = lbox2.curselection()
    lbox.insert(tk.END, lbox2.get(select))
    lbox2.delete(select)
    

frame = tk.Frame()
frame.pack(side=tk.LEFT)

btn_right = tk.Button(frame, text=" >>>> ", command=flyttright)
btn_left = tk.Button(frame, text=" <<<< ", command=flyttleft)

btn_right.pack(fill=tk.X, padx=5)
btn_left.pack(fill=tk.X, padx=5, pady=5)

lbox2 = tk.Listbox(root, width=15, height=8)
lbox2.pack(side=tk.LEFT, padx=5)


root.mainloop()

