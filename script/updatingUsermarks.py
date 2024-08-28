import json
import os
from tkinter import *
from tkinter import messagebox

def update_user_data(roll_number, year, updated_subjects):
    filename = 'students_data.json'
    
    # Check if the file exists
    if not os.path.exists(filename):
        messagebox.showerror("Error", "No data found!")
        return
    
    # Load the existing data
    with open(filename, 'r') as file:
        data = json.load(file)
    
    # Check if the roll number exists
    if roll_number in data:
        # Check if the year exists for the roll number
        if year in data[roll_number]:
            # Update the data for the specified subjects
            data[roll_number][year]['subjects'] = updated_subjects
            
            # Save the updated data back to the JSON file
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            
            messagebox.showinfo("Success", f"Details for Roll Number {roll_number} in year {year} have been updated.")
        else:
            messagebox.showerror("Error", f"No data found for year {year} for Roll Number {roll_number}.")
    else:
        messagebox.showerror("Error", f"No data found for Roll Number {roll_number}.")

def submit_update():
    roll_number = roll_number_entry.get()
    year = year_entry.get()
    
    if roll_number and year:
        # Collect marks for each subject
        updated_subjects = {}
        for subject in subjects:
            updated_subjects[subject] = subjects_entries[subject].get()
        
        update_user_data(roll_number, year, updated_subjects)
        root.destroy()
    else:
        messagebox.showerror("Error", "Please fill out all fields.")

# Predefined subjects
subjects = {
    "DSR": "",
    "BLD": "",
    "NS": "",
    "BVG": "",
    "MBV": "",
    "BVG Lab": "",
    "MBV Lab": "",
    "STB": "",
    "VVR": ""
}

# Dictionary to hold Entry widgets for each subject
subjects_entries = {}

# Initialize the main window
root = Tk()
root.title("Update Student Data")

# Set window size and position to center
window_width = 400
window_height = 550
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

# Create Entry fields for each subject
row = 2
for subject in subjects:
    Label(root, text=f"{subject} Mark:").grid(row=row, column=0, padx=10, pady=5, sticky="e")
    entry = Entry(root)
    entry.grid(row=row, column=1, padx=10, pady=5)
    subjects_entries[subject] = entry
    row += 1

submit_button = Button(root, text="Update", command=submit_update)
submit_button.grid(row=row, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
