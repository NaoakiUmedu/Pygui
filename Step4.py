# https://www.shido.info/py/index.html
"""
Timer project
"""
import tkinter as Tk
import sys
import tkinter.messagebox as TkMsgBox

BLUE = '#99CCFF'
YELLOW = '#FFCC00'
RED = '#FF00FF'
CLOCK = 'omake/meza-bl-2.gif'


class TimerFrame(Tk.Frame):
    """Timer Main Frame"""
    echo: Tk.StringVar
    minutes: int
    MINUTES_DEFAULT = 3
    timer: int
    image: Tk.PhotoImage
    f_display: Tk.Frame
    icon: Tk.Label
    btn_inc: Tk.Button
    btn_dec: Tk.Button
    btn_start: Tk.Button
    btn_stop: Tk.Button
    btn_reset: Tk.Button
    started: bool

    def __init__(self, master=None):
        """Timer Main Frame initialize"""
        Tk.Frame.__init__(self, master)

        # init countdown timer
        self.echo = Tk.StringVar()
        self.minutes = self.MINUTES_DEFAULT
        self.echo_set()

        # init main frame
        self.master.title('Alerm')
        self.master.geometry('300x100')
        f_display = Tk.Frame(self, relief=Tk.RIDGE, bd=4)
        f_display.pack(fill=Tk.X, expand=True)

        # init main display
        # icon
        self.image = Tk.PhotoImage(file=CLOCK)
        self.icon = Tk.Label(f_display, image=self.image, bg=BLUE)
        self.icon.grid(row=0, column=0, rowspan=2)
        # main display
        display: Tk.Label = Tk.Label(f_display, textvariable=self.echo, width=5, relief=Tk.SUNKEN,
                                     bd=2, anchor=Tk.E, font=('Helvetica', 24), bg='white')
        display.grid(row=0, column=1, rowspan=2)

        # buttons
        # increment and decrement
        self.btn_inc = Tk.Button(f_display, font=(
            'Helvetica', '6'), text='+', command=self.inc_time)
        self.btn_inc.grid(row=0, column=2, sticky=Tk.W + Tk.E + Tk.S, pady=1)
        self.btn_dec = Tk.Button(f_display, font=(
            'Helvetica', '6'), text='-', command=self.dec_time)
        self.btn_dec.grid(row=1, column=2, sticky=Tk.W + Tk.E + Tk.S, pady=1)
        # start, stop and reset
        f_button: Tk.Frame = Tk.Frame(self)
        f_button.pack(pady=2)
        self.btn_start = Tk.Button(f_button, text='Start', command=self.start)
        self.btn_start.pack(side=Tk.LEFT, padx=1)
        self.btn_stop = Tk.Button(
            f_button, text='Stop', command=self.stop, state=Tk.DISABLED)
        self.btn_stop.pack(side=Tk.LEFT, padx=1)
        self.btn_reset = Tk.Button(
            f_button, text='Reset', command=self.reset, state=Tk.DISABLED)
        self.btn_reset.pack(side=Tk.LEFT, padx=1)

    def echo_set(self):
        """Initialise countdown timer as seconds"""
        self.timer = 60 * self.minutes
        self.echo.set('%02d:00' % (self.minutes))

    def inc_time(self):
        """Increment timer"""
        self.minutes += 1
        self.echo_set()

    def dec_time(self):
        """Decrement timer"""
        if self.minutes >= 1:
            self.minutes -= 1
        else:
            TkMsgBox.showwarning("Warning!", "Time can not be minus value!")
        self.echo_set()

    def start(self):
        """Start timer"""
        # Set timer started
        self.started = True
        # Set timer color
        if 0 < self.timer <= 20:
            self.icon.configure(bg=YELLOW)
        elif 0 >= self.timer:
            self.icon.configure(bg=RED)
        # Set button state
        self.btn_start.configure(state=Tk.DISABLED)
        self.btn_stop.configure(state=Tk.NORMAL)
        self.btn_inc.configure(state=Tk.DISABLED)
        self.btn_dec.configure(state=Tk.DISABLED)
        # Call period function
        self.after(1000, self.counting)

    def stop(self):
        """Stop timer"""
        # Set timer stopped
        self.started = False
        # Set timer color
        self.icon.configure(bg=BLUE)
        # Set button state
        self.btn_start.configure(state=Tk.NORMAL)
        self.btn_stop.configure(state=Tk.DISABLED)
        self.btn_reset.configure(state=Tk.NORMAL)

    def reset(self):
        """Reset timer"""
        self.echo_set()
        # Set button state
        self.btn_reset.configure(state=Tk.DISABLED)
        self.btn_inc.configure(state=Tk.NORMAL)
        self.btn_dec.configure(state=Tk.NORMAL)

    def counting(self):
        """Countdown timer"""
        if not(self.started):
            return

        # Countdown timer
        self.timer -= 1
        self.echo.set('%02d:%02d' % (self.timer/60, self.timer % 60))

        # Check time left
        if self.timer <= 0:
            self.bell()
            time: int = -1 * self.timer
            self.icon.configure(bg=RED)
            self.echo.set('-%02d:%02d' % (time/60, time % 60))
            self.after(500, self.yellow)
        elif self.timer <= 20:
            self.yellow()

        # Call Period function
        self.after(1000, self.counting)

    def yellow(self):
        """Set timer color to yellow"""
        if self.started:
            self.icon.configure(bg=YELLOW)


# MAIN PROGRAM
if __name__ == '__main__':
    f = TimerFrame()
    f.pack()
    f.mainloop()
