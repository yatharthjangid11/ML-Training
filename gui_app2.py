import tkinter as  ttk
from unittest import result
app=ttk.Tk()
app.title('My App')
app.geometry('600x400')


msg= ttk.Variable(app)
print(msg.get())
msg.set('Empty')
print(msg.get())

app.mainloop()