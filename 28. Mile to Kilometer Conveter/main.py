from tkinter import *


def calculate_mile():
    miles = float(miles_input.get())
    km = round((miles * 1.609), 2)
    km_calculate.config(text=f"{km}")


window = Tk()
window.title("Mile to Km")
window.config(padx=20, pady=20)

miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

mile_label = Label(text="Miles ")
mile_label.grid(column=2, row=0)

equal_to = Label(text="Equal to ")
equal_to.grid(column=0, row=1)

km_calculate = Label(text="0")
km_calculate.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate_mile)
button.grid(column=1, row=2)

window.mainloop()
