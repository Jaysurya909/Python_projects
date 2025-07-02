import tkinter as tk
from time import strftime

clock=tk.Tk()
clock.title("Digital Clock")

def time():
    string=strftime("%H:%M:%S %p \n %D \n %A \n %B - %Y ")
    label.config(text=string)
    label.after(1000,time)



label=tk.Label(clock,font=('calibari',50,'bold'),foreground='gold',background='gray')
label.pack(anchor='center')

time()




clock.mainloop()