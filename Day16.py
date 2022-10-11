import tkinter as tkt
app = tkt.Tk()

app.title("my app")
app.geometry("600x400")

tkt.Label(app, text='a single text label').place(x=50, y=50)


def abc():
    print('wow')



tkt.Label(app, text="Yatharth Jangid").place(x=100, y=100)

tkt.Button(app, text="isko click kar", command=abc).place(x=10, y=10)
tkt.Button(app, text="yeh wala bhi",
           command=lambda: print('wow')).place(x=30, y=30)

app.mainloop()
