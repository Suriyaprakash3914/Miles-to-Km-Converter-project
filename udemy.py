from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    result.config(text=f"{km}")

window = Tk()
window.title("miles to km converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)
my_label = Label(text="miles to km converter")
my_label.config(text="is equal to ")
my_label.grid(column=2, row=4)

new_label= Label(text="miles")
new_label.config(text="Miles")
new_label.grid(column=4, row=1)

km_label = Label(text="km")
km_label.config(text="KM")
km_label.grid(column=4, row=4)

result = Label(text="0")
result.config(text="0")
result.grid(column=3, row=4)

miles_input = Entry(width=10)
print(miles_input.get())
miles_input.grid(column=3, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=3, row=5)

window.mainloop()