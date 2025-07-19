from tkinter import *
# Creating a window
windows = Tk()
windows.title("Resistance Calculator")
windows.geometry("600x550")

# Function to output Resistance
def display():
    try :
        Voltage = float(entry1.get())
        Current = float(entry2.get())
        # Check to see if division by zero occurs
        if Current != 0 :
            output_label.config(text="{:.2f} Ω".format(Voltage/Current))
        else :
            output_label.config(text="Current cannot be zero.Try again.")      
    except :
        output_label.config(text="Please input numeric values.")
        
# Function to delete all the text
def delete():
    entry1.delete(0,END)
    entry2.delete(0,END)
    
# Label and Entry for Voltage
voltage_label = Label(windows,text="Enter  Voltage",fg="green",width=50,padx=130,font=('Georgia'))
voltage_label.pack(padx=(0,60),pady=(10,0))
entry1 = Entry(width=30,relief="raised",bd=5)
entry1.pack(pady=(0,25))

# Label and Entry for Current
current_label = Label(windows,text="Enter  Current",fg="green",font=('Georgia'))
current_label.pack(padx=(0,60))
entry2 = Entry(width=30,relief="raised",bd=5)
entry2.pack(pady=(0,25))

# Delete button
delete_button = Button(windows,text ="Clear All",command=delete,padx=20,font=('Georgia'))
delete_button.pack(pady=(0,25))

# Button for Resistance Calculation
res_button = Button(windows,text="Calculate",command=display,padx=20,font=('Georgia'))
res_button.pack(pady=(0,25))

# Label for Resistance
output = Label(windows,text="Resistance:",width=15,relief="sunken",fg="green",bd=5,bg="whitesmoke",font=('Georgia'))
output.pack(pady=(10,10))

# Label for Output
output_label = Label(windows,text="",font='Arial',fg="green")
output_label.pack()

# Exit Button
exit_button = Button(windows,text="Exit",command=windows.destroy,font=('Georgia'))
exit_button.pack(pady=(15,0))

# Closing window
windows.mainloop()
