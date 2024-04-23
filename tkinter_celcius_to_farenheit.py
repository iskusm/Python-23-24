def exit():
    root.destroy()

def convert():
    c = int(e1.get())
    f = ((c*9)/(5))+32
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,f)
    t1.config(state='disabled')
 
import tkinter as tk
root = tk.Tk()
root.geometry("300x250")
root.config(bg="#A569BD")
#root.resizable(width=False,height=False)
root.title('Celsius to Fahrenheit Converter!')
 
l1 = tk.Label(root,
              text="Celsius to Fahrenheit Converter",
              font=("Arial", 15),
              fg="white",bg="black")
l2= tk.Label(root,text="Enter temperature in Celsius: ",font=("Arial", 10,"bold"),fg="white",bg="#A569BD")
l3= tk.Label(root,text="Temperature in Fahrenheit is: ",font=("Arial", 10,"bold"),fg="white",bg="#A569BD")
 
empty_l1 = tk.Label(root,bg="#A569BD")
empty_l2 = tk.Label(root,bg="#A569BD")
 
e1= tk.Entry(root,font=('Arial',10))
 
btn1 = tk.Button(root,text="Convert to Fahrenheit!",font=("Arial", 10),command=convert)
btn2 = tk.Button(root,text="Exit application",font=("Arial", 10),command=exit)
 
t1=tk.Text(root,state="disabled",width=15,height=0)
 
l1.pack()
l2.pack()
e1.pack()
empty_l1.pack()
btn1.pack()
l3.pack()
t1.pack()
empty_l2.pack()
btn2.pack()
 
root.mainloop()
