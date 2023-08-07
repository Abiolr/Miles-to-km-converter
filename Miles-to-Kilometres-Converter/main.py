from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

def convert():
    miles = float(entry.get())
    km = miles * 1.609
    label_2.config(text=km)

label_1 = Label(text="is equal to")
label_1.grid(row=1, column=0)

label_2 = Label(text= 0)
label_2.grid(row=1, column=1)

label_3 = Label(text="Miles")
label_3.grid(row=0, column=3)

label_4 = Label(text="Km")
label_4.grid(row=1, column=3)

entry = Entry()
entry.grid(row=0, column=1)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()