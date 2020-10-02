import tkinter as tk



def show_picture():

    return tk.PhotoImage(file='Picture1.png')


window = tk.Tk()
t = tk.Label(window, text="what's my favorite video?", fg="purple")
t.pack()
b = tk.Button(window, text="click to find out!", command=show_picture())
b.pack()

window.mainloop()
