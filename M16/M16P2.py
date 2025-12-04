import tkinter as tk
from tkinter import messagebox
from program_functions import ticket_price

#Global totals
total_price = 0
ticket_count = 0

#File name 
DATA_FILE = "ticket_data.txt"

def save_to_file(text):
    """
    Save the provided text to the ticket data file.
    If the file does not exist, it will be created.
    If the file exists, results will be appended.
    """
    with open(DATA_FILE, "a") as file:  # 'a' mode ensures append
        file.write(text + "\n")

def process_ticket():
    """
    Process a single ticket entry:
    - Get passenger name and miles from GUI input
    - Compute ticket price using ticket_price function
    - Update totals
    - Display results in GUI output area
    - Save results to file
    """
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
    
    #Format result text
    result_text = (
        "\nTrain Ticket Estimate\n"
        + "-" * 40 + "\n"
        + f"{'Passenger:':<30} {last_name}\n"
        + f"{'Miles from downtown:':<30} {miles:>10.1f}\n"
        + f"{'Ticket price:':<30} ${price:>10.2f}\n"
        + "-" * 40
    )
    
    #Display results in GUI
    output_text.insert(tk.END, result_text + "\n")
    
    #Save results to file
    save_to_file(result_text)
    
    #Clear inputs for next entry
    entry_name.delete(0, tk.END)
    entry_miles.delete(0, tk.END)

def show_summary():
    """
    Display and save the summary of all tickets:
    - Total tickets sold
    - Total ticket revenue
    """
    summary_text = (
        "\nSummary of All Tickets\n"
        + "-" * 40 + "\n"
        + f"{'Total tickets sold:':<30} {ticket_count:>10}\n"
        + f"{'Total ticket revenue:':<30} ${total_price:>10.2f}\n"
        + "-" * 40
    )
    
    #Display in GUI
    output_text.insert(tk.END, summary_text + "\n")
    
    #Save to file
    save_to_file(summary_text)

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

tk.Button(root, text="Add Ticket", command=process_ticket).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="Show Summary", command=show_summary).grid(row=2, column=1, padx=5, pady=5)

#Output area
output_text = tk.Text(root, width=60, height=20)
output_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
