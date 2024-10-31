import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# File to store user data
DATA_FILE = "bmi_data.csv"

def calculate_bmi(weight, height):
    """Calculate BMI from weight (kg) and height (m)."""
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Height cannot be zero.")
        return None

def categorize_bmi(bmi):
    """Categorize the BMI into health ranges."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def save_data(name, bmi):
    """Save user data to CSV file with current date and time."""
    data = pd.DataFrame([[name, bmi, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]],
                        columns=["Name", "BMI", "Date"])
    try:
        # Append data to CSV, create file if it doesn't exist
        data.to_csv(DATA_FILE, mode='a', index=False, header=not pd.io.common.file_exists(DATA_FILE))
        messagebox.showinfo("Success", "Data saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save data: {e}")

def plot_data():
    """Display BMI trend analysis for the user."""
    try:
        # Load data and plot the BMI trend over time
        data = pd.read_csv(DATA_FILE)
        data['Date'] = pd.to_datetime(data['Date'])
        
        plt.figure(figsize=(10, 5))
        for name in data["Name"].unique():
            user_data = data[data["Name"] == name]
            plt.plot(user_data['Date'], user_data['BMI'], label=name)
        
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.title("BMI Trend Analysis")
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Could not load data: {e}")

def calculate_and_save():
    """Calculate BMI, categorize, and save data."""
    try:
        name = name_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not name:
            messagebox.showerror("Error", "Please enter a name.")
            return

        bmi = calculate_bmi(weight, height)
        if bmi:
            category = categorize_bmi(bmi)
            result_label.config(text=f"Your BMI is {bmi} ({category})")
            save_data(name, bmi)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for weight and height.")

# Set up GUI
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("400x300")

tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(root, text="Height (m):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Calculate and display result
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_and_save)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Button for viewing trend
view_trend_button = tk.Button(root, text="View BMI Trend", command=plot_data)
view_trend_button.pack(pady=10)

root.mainloop()
