# https://www.shido.info/py/index.html
"""
たいまー
"""
import tkinter as Tk
import sys


BLUE = '#99CCFF'
YELLOW = '#FFCC00'
RED = '#FF00FF'
CLOCK = 'omake\\meza-bl-2.gif'


class TimerFrame(Tk.Frame):
    """タイマのフレーム(ウィンドウ)"""
    started:    bool            # 開始したか?
    echo:       Tk.StringVar    # 時刻表示用文字列
    minutes:    int             # 現在の分
    sec:        int             # 現在の秒
    label:      Tk.Label        # くりっくとぅーすたーと
    image:      Tk.PhotoImage   # 画像
    icon:       Tk.Label        # アイコン

    def __init__(self, master, minutes):
        """初期化"""
        Tk.Frame.__init__(self, master)

        # 時刻の初期化
        self.started = False
        self.echo = Tk.StringVar()
        self.minutes = minutes
        self.echo.set('%02d:00' % (self.minutes))
        self.sec = 60 * self.minutes

        # 画面レイアウト初期化
        self.master.title('Alarm')
        self.label = Tk.Label(self, text='Click to start',
                              font=('Helvetica', '8'))
        self.label.pack()
        f = Tk.Frame(self, relief=Tk.RIDGE, bd=4)
        f.pack(fill=Tk.BOTH, expand=1)
        self.image = Tk.PhotoImage(file=CLOCK)
        self.icon = Tk.Label(f, image=self.image, bg=BLUE)
        self.icon.pack(side=Tk.LEFT)
        display = Tk.Label(f, textvariable=self.echo, font=('Helvetica', '24'),
                           bg='white', width=5, anchor=Tk.E)
        display.pack(side=Tk.LEFT)

        # イベント登録
        self.bind_all('<1>', self.start_stop)
        self.bind_all('<3>', self.reset)

    def start_stop(self, event):
        """スタート/ストップ"""
        if not self.started:
            # 開始処理
            self.label.configure(text='Click to stop')
            if 0 < self.sec <= 20:
                self.icon.configure(bg=YELLOW)
            if 0 >= self.sec:
                self.icon.configure(bg=RED)
            self.started = True
            # カウント処理を行う
            self.after(1000, self.counting)
        else:
            # 終了処理
            self.label.configure(text='Click to start, RB tp reset')
            self.icon.configure(bg=BLUE)
            self.started = False

    def counting(self):
        """カウント処理"""
        if self.started:
            self.sec -= 1
            self.echo.set('%02d:%02d' % (self.sec/60, self.sec % 60))
            if self.sec == 20:
                self.icon.configure(bg=YELLOW)
            if self.sec <= 0:
                t = -1 * self.sec
                self.icon.configure(bg=RED)
                self.bell()
                self.echo.set('-%02d:%02d' % (t/60, t % 60))
                self.after(500, self.yellow)

            self.after(1000, self.counting)

    def yellow(self):
        if self.started:
            self.icon.configure(bg=YELLOW)

    def reset(self, event):
        if not self.started:
            self.sec = 60*self.minutes
            self.echo.set('%02d:00' % (self.minutes))


if __name__ == '__main__':
    minutes = len(sys.argv) > 1 and int(sys.argv[1]) or 3
    f = TimerFrame(None, minutes)
    f.pack()
    f.mainloop()
