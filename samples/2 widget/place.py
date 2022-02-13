# https://www.shido.info/py/index.html
import tkinter as tk


class Frame(tk.Frame):
    """ Frame with three Label """

    def __init__(self, master=None):
        tk.Frame.__init__(self, master, height=100, width=300)
        self.master.title('パッケージうぃずスリーラベル')

        # 1
        la = tk.Label(self, text='Hello everybody. How are you?',
                      bg='yellow',
                      relief=tk.RIDGE,
                      bd=2)
        la.place(relx=0.02, rely=0.1, relheight=0.3, relwidth=0.95)

        # 2
        lb = tk.Label(self, text='Oh My God!',
                      bg='red',
                      relief=tk.RIDGE,
                      bd=2)
        lb.place(relx=0.15, rely=0.45)

        # 3
        lc = tk.Label(self, text='地獄で会おうぜ、ベイベー!',
                      bg='LightSkyBlue',
                      relief=tk.RIDGE,
                      bd=2)
        lc.place(relx=0.5, rely=0.75)


if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
