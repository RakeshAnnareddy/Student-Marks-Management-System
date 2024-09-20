import json
import os
import tkinter as tk
from tkinter import messagebox

def store_user_data(name, roll_number, year, subjects):
    filename = '../data/students_data.json'
    
    # Load existing data if the file exists, otherwise start with an empty dictionary
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
    else:
        data = {}

    # Prepare the data to be stored
    student_data = {
        "name": name,
        "year": year,
        "subjects": subjects
    }
    
    # Store data with roll number and year as keys
    if roll_number not in data:
        data[roll_number] = {}
    
    data[roll_number][year] = student_data
    
    # Write data back to the JSON file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    
    messagebox.showinfo("Success", "Data has been stored successfully.")

def submit_data():
    name = name_entry.get()
    roll_number = roll_number_entry.get()
    year = year_entry.get()
    
    if name and roll_number and year:
        # Collect marks for each subject
        for subject in subjects:
            subjects[subject] = subjects_entries[subject].get()
        
        store_user_data(name, roll_number, year, subjects)
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
root = tk.Tk()
root.title("Student Data Entry")

# Set window size and position to center
window_width = 400
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = int((screen_width / 2) - (window_width / 2))
y_position = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


# Create and place widgets in the center
tk.Label(root, text="Name:", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Roll Number:", bg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
roll_number_entry = tk.Entry(root)
roll_number_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Year:", bg="white").grid(row=3, column=0, padx=10, pady=5, sticky="e")
year_entry = tk.Entry(root)
year_entry.grid(row=3, column=1, padx=10, pady=5)

# Create Entry fields for each subject with a background
row = 4
for subject in subjects:
    tk.Label(root, text=f"{subject} Mark:", bg="white").grid(row=row, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(root)
    entry.grid(row=row, column=1, padx=10, pady=5)
    subjects_entries[subject] = entry
    row += 1

submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=row, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
