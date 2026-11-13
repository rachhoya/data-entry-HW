from tkinter import *

window=Tk()
window.geometry("400x350")
window.title("Data Entry")
window.config(background="green")

def clear_function():
    enter.delete(0,END)
    enter2.delete(0,END)


first_name=Label(window,text="First Name",font=("Consolas",13))
first_name.place(x=20,y=80)

enter=Entry(window,width=30,font=13)
enter.place(x=122,y=84)

last_name=Label(window,text="Last Name",font=("Consolas",13))
last_name.place(x=20,y=150)

enter2=Entry(window,width=30,font=13)
enter2.place(x=115,y=154)

submit=Button(window,text="submit",font=("Arial",13,"bold"),relief="raised")
submit.place(x=50,y=230)

submit=Button(window,text="clear",font=("Arial",13,"bold"),relief="raised",command=clear_function)
submit.place(x=200,y=230)

window.mainloop()