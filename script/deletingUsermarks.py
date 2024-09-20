import json
import os
from tkinter import *
from tkinter import messagebox

def delete_user_data(roll_number, year):
    filename = '../data/students_data.json'
    
    # Check if the file exists
    if not os.path.exists(filename):
        messagebox.showerror("Error", "No data found.")
        return
    
    # Load the existing data
    with open(filename, 'r') as file:
        data = json.load(file)
    
    # Check if the roll number exists
    if roll_number in data:
        # Check if the year exists for the roll number
        if year in data[roll_number]:
            # Delete the data for the specified roll number and year
            del data[roll_number][year]
            
            # If no other data exists for that roll number, remove the roll number entry
            if not data[roll_number]:
                del data[roll_number]
            
            # Save the updated data back to the JSON file
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            
            messagebox.showinfo("Success", f"Details for Roll Number {roll_number} in year {year} have been deleted.")
        else:
            messagebox.showerror("Error", f"No data found for year {year} for Roll Number {roll_number}.")
    else:
        messagebox.showerror("Error", f"No data found for Roll Number {roll_number}.")

def submit_deletion():
    roll_number = roll_number_entry.get()
    year = year_entry.get()
    
    if roll_number and year:
        delete_user_data(roll_number, year)
        root.destroy()
    else:
        messagebox.showerror("Error", "Please fill out all fields.")

# Initialize the main window
root = Tk()
root.title("Delete Student Data")

# Set window size and position to center
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = int((screen_width / 2) - (window_width / 2))
y_position = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create and place widgets in the center
Label(root, text="Roll Number:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
roll_number_entry = Entry(root)
roll_number_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Year:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
year_entry = Entry(root)
year_entry.grid(row=1, column=1, padx=10, pady=10)

submit_button = Button(root, text="Delete", command=submit_deletion)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
