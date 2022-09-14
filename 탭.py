from tkinter import*
from tkinter import ttk

window=Tk()
window.iconbitmap('python.ico')

baseTab=ttk.Notebook(window)

tabDog=ttk.Frame(baseTab)
baseTab.add(tabDog,text='강아지')
tabCat=ttk.Frame(baseTab)
baseTab.add(tabCat,text='고양이')

baseTab.pack(expand=1, fill="both")

photoDog=PhotoImage(file="강아지.jpg")
labelDog=Label(tabDog, image=photoDog)
labelDog.pack()

photoCat=PhotoImage(file="고양이.jpg")
labelCat=Label(tabCat, image=photoCat)
labelCat.pack()

window.mainloop()
