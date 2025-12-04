import tkinter as tk
from tkinter import messagebox
from program_functions import ticket_price

#Global totals
total_price = 0
ticket_count = 0

#Function to process ticket entry
def process_ticket():
    global total_price, ticket_count
    
    last_name = entry_name.get()
    try:
        miles = float(entry_miles.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Miles must be a number.")
        return
    
    #Compute ticket price
    price = ticket_price(miles)
    
    #Update totals
    total_price += price
    ticket_count += 1
    
    #Display results
    output_text.insert(tk.END, "\nTrain Ticket Estimate\n")
    output_text.insert(tk.END, "-" * 40 + "\n")
    output_text.insert(tk.END, f"{'Passenger:':<30} {last_name}\n")
    output_text.insert(tk.END, f"{'Miles from downtown:':<30} {miles:>10.1f}\n")
    output_text.insert(tk.END, f"{'Ticket price:':<30} ${price:>10.2f}\n")
    output_text.insert(tk.END, "-" * 40 + "\n")
    
    #Clear inputs 
    entry_name.delete(0, tk.END)
    entry_miles.delete(0, tk.END)

#Function for summary
def show_summary():
    output_text.insert(tk.END, "\nSummary of All Tickets\n")
    output_text.insert(tk.END, "-" * 40 + "\n")
    output_text.insert(tk.END, f"{'Total tickets sold:':<30} {ticket_count:>10}\n")
    output_text.insert(tk.END, f"{'Total ticket revenue:':<30} ${total_price:>10.2f}\n")
    output_text.insert(tk.END, "-" * 40 + "\n")

#GUI 
root = tk.Tk()
root.title("Train Ticket Calculator")

#Input fields
tk.Label(root, text="Passenger Last Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Miles from Downtown Chicago:").grid(row=1, column=0, padx=5, pady=5)
entry_miles = tk.Entry(root)
entry_miles.grid(row=1, column=1, padx=5, pady=5)

#Buttons
tk.Button(root, text="Add Ticket", command=process_ticket).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="Show Summary", command=show_summary).grid(row=2, column=1, padx=5, pady=5)

#Output area
output_text = tk.Text(root, width=60, height=20)
output_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
