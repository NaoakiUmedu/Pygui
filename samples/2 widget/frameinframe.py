# https://www.shido.info/py/index.html
import tkinter as tk


class Frame(tk.Frame):
    """ Frame with three Label """

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('パッケージうぃずスリーラベル')

        # 1
        la = tk.Label(self, text='Hello everybody. How are you?',
                      bg='yellow',
                      relief=tk.RIDGE,
                      bd=2)
        # la.grid(row=0, column=0, columnspan=2, padx=5, pady=5 )
        la.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)

        # 2
        lb = tk.Label(self, text='Oh My God!',
                      bg='red',
                      relief=tk.RIDGE,
                      bd=2)
        lb.grid(row=1, column=0, padx=5, pady=5)

        # 3
        lc = tk.Label(self, text='地獄で会おうぜ、ベイベー!',
                      bg='LightSkyBlue',
                      relief=tk.RIDGE,
                      bd=2)
        lc.grid(row=1, column=1, padx=5, pady=5)


if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
