# Voltage-Current Data Generator Application

This application is designed to generate and plot dummy readings for voltage-current data using linear regression. It allows users to input real voltage and current readings, and then, based on these inputs, generates dummy readings which are plotted alongside the real data.

## Features

- Input fields for real voltage and current readings.
- Functionality to add and store multiple voltage-current pairs.
- Option to adjust the slope of the linear regression model.
- Graphical display of real data, dummy data, and lines of best fit.
- Output of dummy voltages, currents, and the gradient of the new line of best fit.
- Functionality to clear all entered data for new inputs.

## Requirements

To run this application, you will need Python installed on your system along with the following libraries:

- numpy
- matplotlib
- scikit-learn

These can be installed using the following command:

```commandline
pip install -r requirements.txt
```


The `requirements.txt` file should contain:
```commandline
numpy
matplotlib
scikit-learn
```


## Usage

1. Run the application.
2. Enter the real voltage (V) and current (I) readings in their respective fields.
3. Click 'Add Data' to store each voltage-current pair.
4. Optionally, adjust the slope by entering a value in the 'Slope Adjustment' field.
5. Click 'Generate Data' to plot the data and generate dummy readings.
6. The dummy readings and the gradient of the new line of best fit will be displayed in the GUI.
7. Use 'Clear Data' to reset all inputs and start with new data.

## Note

- Ensure to close the graph window to view the updated dummy data in the application.
- Tkinter is used for the GUI, which is part of the standard Python library.

## Author

Shahu Wagh :)

