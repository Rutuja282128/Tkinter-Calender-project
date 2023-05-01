import calendar
import tkinter as tk

class CalendarApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calendar App")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create calendar header
        header = tk.Label(self, text="Calendar", font=("Arial", 16))
        header.grid(row=0, column=0, columnspan=7)

        # create calendar buttons
        button_prev = tk.Button(self, text="<", command=self.prev_month)
        button_prev.grid(row=1, column=0)

        button_next = tk.Button(self, text=">", command=self.next_month)
        button_next.grid(row=1, column=6)

        # create calendar days labels
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            label_day = tk.Label(self, text=day)
            label_day.grid(row=2, column=i)

        # initialize calendar
        self.year = 2023
        self.month = 5
        self.cal = calendar.monthcalendar(self.year, self.month)

        # create calendar days buttons
        for week_num, week in enumerate(self.cal):
            for day_num, day in enumerate(week):
                if day != 0:
                    button_day = tk.Button(self, text=str(day), width=3)
                    button_day.grid(row=week_num+3, column=day_num)

    def prev_month(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.update_calendar()

    def next_month(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.update_calendar()

    def update_calendar(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_widgets()

root = tk.Tk()
app = CalendarApp(master=root)
app.mainloop()
