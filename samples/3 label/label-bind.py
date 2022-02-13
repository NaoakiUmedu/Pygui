# https://www.shido.info/py/index.html
import tkinter as Tk
import random as R


class Label(Tk.Label):
    def __init__(self, master=None):
        Tk.Label.__init__(self, master, text='Hello world!',
                          font=('Helvetica', '24', 'bold'))
        # widgetとイベントをバインドする
        self.bind_all('<Control-Shift-KeyPress-Tab>', self.bg_change)

    def bg_change(self, event):
        r = R.randint(0, 255)
        g = R.randint(0, 255)
        b = R.randint(0, 255)
        self.configure(bg='#%02X%02X%02X' % (r, g, b))


if __name__ == '__main__':
    lbl = Label()
    lbl.pack()
    lbl.mainloop()
