from tkinter import *


def converter():
    given = float(iinput.get())
    output_value["text"] = round(given * 1.609, 2)


window = Tk()
window.title("Miles to Km Converter")

iinput = Entry(width=10)
iinput.insert(END, string="0")
iinput.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

kilometer_label = Label(text="Kilometer")
kilometer_label.grid(row=1, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

button = Button(text="Calculate", command=converter)
button.grid(row=2, column=1)

output_value = Label(text=0)
output_value.grid(row=1, column=1)

window.mainloop()
