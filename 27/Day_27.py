import tkinter


window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)
window.config(padx=35, pady=20)

input = tkinter.Entry()
input.grid(column=2, row=1)

miles_label = tkinter.Label(text='Miles')
miles_label.grid(column=3, row=1)

is_equal_label = tkinter.Label(text='is equal to')
is_equal_label.grid(column=1, row=2)

def calculate():
    our_num_label.config(text=round(float(input.get()) * 1.609, 2))

our_num_label = tkinter.Label(text='0')
our_num_label.grid(column=2, row=2)

km_label = tkinter.Label(text='Km')
km_label.grid(column=3, row=2)

button = tkinter.Button(text='Calculate', command=calculate)
button.grid(column=2, row=3)


window.mainloop()