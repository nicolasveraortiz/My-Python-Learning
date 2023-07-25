from tkinter import *


def miles_to_km():
    miles = float(miles_entry.get())
    result_km = miles * 1.609
    km.config(text=result_km)


screen = Tk()
screen.title("Miles to Km Converter")
screen.minsize(200, 100)
screen.config(padx=20, pady=20)

miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

calculate = Button(text="Calculate", command = miles_to_km)
calculate.grid(column=1, row=2)

km = Label(text=0)
km.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)


screen.mainloop()
