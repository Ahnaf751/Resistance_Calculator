from tkinter import *
#Creating a window
windows = Tk()
windows.title("Resistance Finder")
windows.geometry("600x450")
# Function to output Resistance
def display():
    try :
        Voltage = float(entry1.get())
        Current = float(entry2.get())
        # Check to see if division by zero occurs
        if Current != 0 :
            output_label.config(text=Voltage/Current)
        else :
            output_label.config(text="Current cannot be zero.Try again.")      
    except :
        output_label.config(text="Please input only numeric values.")
# Function to clear all the text
def delete():
    entry1.delete(0,END)
    entry2.delete(0,END)
    
# Label and Entry for Voltage
voltage_label = Label(windows,text="Enter Voltage",fg="green",width=50,padx=130,font=('Arial'))
voltage_label.pack(pady=(10,0))
entry1 = Entry(width=30,relief="raised",bd=5)
entry1.pack(pady=(0,25))

# Label and Entry for Current
Current_label = Label(windows,text="Enter Current",fg="green",font=('Arial'))
Current_label.pack()
entry2 = Entry(width=30,relief="raised",bd=5)
entry2.pack(pady=(0,25))

# Label for deleting
delete_label = Button(windows,text ="Clear All",command=delete,padx=20,font=('Arial'))
delete_label.pack(pady=(0,25))

# Button for Resistance Calculation
Mybutton = Button(windows,text="Calculate",command=display,padx=20,font=('Arial'))
Mybutton.pack(pady=(0,25))

# Label for Resistance
output = Label(windows,text="Resistance:",width=17,relief="sunken",fg="green",bg="white",bd=5,font=('Arial'))
output.pack(pady=(0,15))

# Label for Output
output_label = Label(windows,text="",font='Arial',fg="green")
output_label.pack()

# Closing window
windows.mainloop()
