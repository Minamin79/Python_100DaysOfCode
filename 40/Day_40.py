import tkinter, time

window = tkinter.Tk() 
window.title("DigiClock") 
window.geometry("350x150") 
window.resizable(1, 1)


label = tkinter.Label(window, font=('Helvetica', 50, 'bold'), bg='cadetblue', fg='cadetblue1', bd=25) 
label.grid(row=0, column=1, padx=15, pady=10)

def clock(): 
   label.config(text=time.strftime("%H:%M:%S")) 
   label.after(200, clock)

clock()
window.mainloop()