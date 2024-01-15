import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def generate_and_plot_dummy_readings(real_voltages, real_currents, slope_adjustment, cur_variance, vol_variance):
    # Convert lists to numpy arrays for calculations
    voltages = np.array(real_voltages).reshape(-1, 1)
    currents = np.array(real_currents)

    # Perform linear regression to find the original slope and y-intercept
    model = LinearRegression().fit(currents.reshape(-1, 1), voltages)
    original_slope = model.coef_[0]
    original_intercept = model.intercept_
    new_intercept = original_intercept - np.random.uniform(1, 2)

    # Adjust the slope by the specified value
    new_slope = original_slope + slope_adjustment

    # Generate dummy current readings with slight variation
    dummy_currents = currents + np.random.uniform(-1*cur_variance, cur_variance, currents.size)

    # Calculate dummy voltages using the new slope and original y-intercept
    dummy_voltages = new_slope * dummy_currents + new_intercept
    # Introduce random variation to dummy voltages
    dummy_voltages += np.random.uniform(-1*vol_variance, vol_variance, dummy_voltages.size)

    # Perform linear regression on the dummy data to find the new line of best fit
    dummy_model = LinearRegression().fit(dummy_currents.reshape(-1, 1), dummy_voltages)
    new_dummy_slope = dummy_model.coef_[0]
    new_dummy_intercept = dummy_model.intercept_

    # Plot original data
    plt.scatter(currents, voltages, color='blue', label='Real Data')
    plt.plot(currents, model.predict(currents.reshape(-1, 1)), color='green', label='Original Line of Best Fit')

    # Plot the new line of best fit from dummy data
    extended_currents = np.linspace(min(currents), max(currents), 100)
    plt.plot(extended_currents, new_dummy_slope * extended_currents + new_dummy_intercept, color='purple', label='New Line of Best Fit from Dummy Data')

    # Plot dummy data points
    plt.scatter(dummy_currents, dummy_voltages, color='orange', marker='x', label='Dummy Data Points')

    plt.xlabel('Current (I)')
    plt.ylabel('Voltage (V)')
    plt.title('Real Data and New Line of Best Fit from Dummy Data')
    plt.legend()
    plt.show()

    print("Gradient of the New Line of Best Fit from Dummy Data:", new_dummy_slope)

    return dummy_voltages, dummy_currents, new_dummy_slope

def add_data():
    try:
        voltage = float(voltage_entry.get())
        current = float(current_entry.get())
        real_voltages.append(voltage)
        real_currents.append(current)
        data_display.insert(tk.END, f"V: {voltage}, I: {current}")
        voltage_entry.delete(0, tk.END)
        current_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values.")

def generate_data():
    try:
        slope_adjustment = float(slope_adjustment_entry.get())
        cur_variance = float(cur_variance_entry.get())
        vol_variance = float(vol_variance_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numerical value for slope adjustment.")
        return

    if not real_voltages or not real_currents:
        messagebox.showerror("No Data", "Please add voltage and current data.")
        return

    dummy_voltages, dummy_currents, gradient = generate_and_plot_dummy_readings(real_voltages, real_currents, slope_adjustment, cur_variance, vol_variance)
    status_display.config(state=tk.NORMAL)
    status_display.delete(1.0, tk.END)
    status_display.insert(tk.END, f"Dummy Voltages: {dummy_voltages}\nDummy Currents: {dummy_currents}\nGradient: {gradient}")
    status_display.config(state=tk.DISABLED)

def clear_data():
    real_voltages.clear()
    real_currents.clear()
    data_display.delete(0, tk.END)
    status_display.config(state=tk.NORMAL)
    status_display.delete(1.0, tk.END)
    status_display.config(state=tk.DISABLED)
    messagebox.showinfo("Data Cleared", "All input data has been cleared.")

# GUI setup
root = tk.Tk()
root.title("Voltage-Current Data Generator")

real_voltages = []
real_currents = []

# Input fields for voltage and current
tk.Label(root, text="Voltage (V):").grid(row=0, column=0)
voltage_entry = tk.Entry(root)
voltage_entry.grid(row=0, column=1)

tk.Label(root, text="Current (I):").grid(row=1, column=0)
current_entry = tk.Entry(root)
current_entry.grid(row=1, column=1)

# Slope adjustment input
tk.Label(root, text="Slope Adjustment (Specify +/-):").grid(row=2, column=0)
slope_adjustment_entry = tk.Entry(root)
slope_adjustment_entry.grid(row=2, column=1)

tk.Label(root, text="Current Variance (0.05-0.20):").grid(row=3, column=0)
cur_variance_entry = tk.Entry(root)
cur_variance_entry.grid(row=3, column=1)

tk.Label(root, text="Voltage Variance (0.40-0.90):").grid(row=4, column=0)
vol_variance_entry = tk.Entry(root)
vol_variance_entry.grid(row=4, column=1)

# Buttons to add data and generate dummy data
add_button = tk.Button(root, text="Add Data", command=add_data)
add_button.grid(row=5, column=0, columnspan=2)

generate_button = tk.Button(root, text="Generate Data", command=generate_data)
generate_button.grid(row=6, column=0, columnspan=2)

# Display area for entered data and results
data_display = tk.Listbox(root)
data_display.grid(row=7, column=0, columnspan=2)

status_display = tk.Text(root, height=10, state=tk.DISABLED)
status_display.grid(row=8, column=0, columnspan=2)

# Text to inform user to close the graph to view data
info_label = tk.Label(root, text="Please close the graph to view the data.")
info_label.grid(row=9, column=0, columnspan=2)

# Button to clear all data
clear_data_button = tk.Button(root, text="Clear Data", command=clear_data)
clear_data_button.grid(row=10, column=0, columnspan=2)

root.mainloop()
