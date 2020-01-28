from tkinter import *

canv = Tk()
canv.title("Mesurette")

lblnom = Label(canv, text="Nom :")
#lblnom.pack()
lblprenom = Label(canv,text="Prenom :")
#lblprenom.pack()

lblnom.grid(row=0, column=0)
lblprenom.grid(row=1, column=0)


canv.mainloop()

