import json
import os
from tkinter import *
from tkinter import messagebox

def fetch_user_data():
    filename = 'students_data.json'
    
    # Check if the file exists
    if not os.path.exists(filename):
        messagebox.showerror("Error", "No data found!")
        return
    
    # Load the data from the JSON file
    with open(filename, 'r') as file:
        data = json.load(file)
    
    roll_number = roll_number_entry.get()
    year = year_entry.get()
    
    # Clear previous results
    for widget in result_frame.winfo_children():
        widget.destroy()
    
    # Fetch and display the details
    if roll_number in data and year in data[roll_number]:
        student_data = data[roll_number][year]
        
        # Display student name and year
        Label(result_frame, text=f"Name: {student_data['name']}").grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        Label(result_frame, text=f"Year: {student_data['year']}").grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        
        # Display table headers with borders
        header_subject = Frame(result_frame, relief="solid", bd=1)
        header_subject.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
        Label(header_subject, text="Subject Code", font=("Arial", 15, "bold")).pack(fill=BOTH, expand=True)
        
        header_marks = Frame(result_frame, relief="solid", bd=1)
        header_marks.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")
        Label(header_marks, text="Marks", font=("Arial", 15, "bold")).pack(fill=BOTH, expand=True)
        
        # Display subjects and marks in a table format with borders
        row = 3
        for subject, mark in student_data['subjects'].items():
            subject_frame = Frame(result_frame, relief="solid", bd=1)
            subject_frame.grid(row=row, column=0, padx=10, pady=5, sticky="nsew")
            Label(subject_frame, text=subject).pack(fill=BOTH, expand=True)
            
            mark_frame = Frame(result_frame, relief="solid", bd=1)
            mark_frame.grid(row=row, column=1, padx=10, pady=5, sticky="nsew")
            Label(mark_frame, text=mark).pack(fill=BOTH, expand=True)
            
            row += 1
    else:
        messagebox.showerror("Error", "No data found for the given roll number and year.")

def submit_fetch():
    fetch_user_data()

# Initialize the main window
root = Tk()
root.title("Fetch Student Data")

# Set window size and position to center
window_width = 400
window_height = 580
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

submit_button = Button(root, text="Fetch", command=submit_fetch)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create a frame to hold the result table
result_frame = Frame(root)
result_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()
