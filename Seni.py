import tkinter as tk


class App(tk.Tk):
    """Application"""
    main_frame: tk.Frame
    frame1: tk.Frame

    def __init__(self, *args, **kwargs):
        """Application initialization"""
        tk.Tk.__init__(self, *args, **kwargs)

        # Window title
        self.title("Tkinter change page")

        # Window size
        self.geometry("800x600")

        # Grid
        # If these lines are commented out, position goes to difference point
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ----------------------------------------------------
        # Main frame
        # ----------------------------------------------------
        # frame
        self.main_frame = tk.Frame()
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        # title
        self.titleLabel = tk.Label(
            self.main_frame, text="Main Page", font=('Helvetica', '35'))
        self.titleLabel.pack(anchor='center', expand=True)
        # button for changing to frame1
        self.changePageButton = tk.Button(
            self.main_frame,
            text="Go to Sub Page",
            command=lambda: self.changePage(self.frame1))
        self.changePageButton.pack()
        # Set visible
        # self.changePage(self.main_frame)

        # ----------------------------------------------------
        # Sub frame
        # ----------------------------------------------------
        # frame
        self.frame1 = tk.Frame()
        self.frame1.grid(row=0, column=0, sticky="nsew")
        # title
        self.titleLabel = tk.Label(
            self.frame1, text="Sub Page", font=('Helvetica', '35'))
        self.titleLabel.pack(anchor='center', expand=True)
        # button for changing to frame1
        self.changePageButton2 = tk.Button(
            self.frame1,
            text="Go to Main Page",
            command=lambda: self.changePage(self.main_frame))
        self.changePageButton2.pack()

        self.main_frame.tkraise()

    def changePage(self, page: tk.Frame):
        """Change frame"""
        page.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
