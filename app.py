from tkinter import *

def convert():
    if ent_value.get():
        val = float(ent_value.get())
        s="1.0"
        e="end"
        if txt1.get(s,e) and txt2.get(s,e) and txt2.get(s,e):
            txt1.delete(s,e)
            txt2.delete(s,e)
            txt3.delete(s,e)
        txt1.insert(END, val * 1000) #grams
        txt2.insert(END, val * 2.20462) #pounds
        txt3.insert(END, val * 3.5274) #ounces


window=Tk()

lab = Label(window, text="KG:")
lab.grid(row=0, column=0)

btn = Button(window, text="Convert", command=convert)
btn.grid(row=0, column=2)

ent_value=StringVar()
ent=Entry(window, textvariable=ent_value)
ent.grid(row=0, column=1)

txt1=Text(window, height=1, width=20)
txt1.grid(row=1, column=0)
txt2=Text(window, height=1, width=20)
txt2.grid(row=1, column=1)
txt3=Text(window, height=1, width=20)
txt3.grid(row=1, column=2)

window.mainloop()