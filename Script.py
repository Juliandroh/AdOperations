from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
from typing import Text

##Funktion
List_solve = []
#now = datetime.now()
#daterange = list(now - timedelta(days=x) for x in range(30))
#datenow = [daterange.strftime("%d.%m.")]

def calc():
    LIG = LIG_feld.get("1.0","end-1c")
    LIO = LIO_feld.get("1.0","end-1c")
    ListLIG = LIG.split("\n")
    ListLIO = LIO.split("\n")
    for i in ListLIG:
        if i not in ListLIO:
            List_solve.append(i)
      

    for item in list(List_solve):
        listbox.insert("end", item)
    

def output():
    file = open('non public campaigns.txt', 'w')
    endList= '\n'.join(List_solve)
    file.write(endList)
    file.close()


##Hauptfenster
root = tk.Tk() 
root.title("Line Item Online-Check")
root.geometry("1300x700")
root.minsize(width=250, height=150)


#Eingabefeld
LIG_feld = tk.Text(root, width=70, height=15)
LIG_feld.grid(row=2, column=1, padx=15)

LIO_feld = tk.Text(root, width=70, height=15)
LIO_feld.grid(row=2, column=3, padx=10)



#Listbox
listbox = tk.Listbox(root, width=60, height=20)
listbox.grid(row=5, column= 1)


##Text
labelLIG = ttk.Label(root, text = "All Line Items")
labelLIG.grid(row=1, column=1)

labelLIO = ttk.Label(root, text = "Line Items online")
labelLIO.grid(row=1, column=3)


##Buttons
submit = ttk.Button(root, text="submit", padding= 10, command=calc)
submit.grid(row=3, column=2)

kopieren = ttk.Button(root, text="create output", padding=10, command=output)
kopieren.grid(row=5, column=2)

quit = ttk.Button(root, text="close", command= root.destroy)
quit.grid(row=5, column=3)


root.mainloop()






