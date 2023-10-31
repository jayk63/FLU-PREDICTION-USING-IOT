# FLU Vital Readings and Patient Status Monitoring

![FLU Vital Readings and Patient Status Monitoring](project_image.png)

This is a Streamlit web application for monitoring FLU vital readings and predicting patient status based on the provided vital readings. The application allows you to input simulated vital readings for SpO2 (oxygen saturation), heart rate, and body temperature. It can also connect to an Arduino device to fetch real-time sensor data from it.

## Table of Contents

- [Files and Directory Structure](#files-and-directory-structure)
- [How to Run the Streamlit Application](#how-to-run-the-streamlit-application)
- [Functionality](#functionality)
- [Important Note](#important-note)

## Files and Directory Structure

Here's an overview of the files and directories in this project:

- `best_model_Decision_Tree.pkl`: This is the trained machine learning model (Decision Tree) used for predicting patient status based on vital readings.

- `fs.ipynb`: A Jupyter Notebook file that might contain code related to feature selection or preprocessing.

- `main.py`: The main Streamlit application code, where you can run the Streamlit web application.

- `qt_dataset.csv` and `qt_dataset.xlsx`: These files might contain datasets used for training the machine learning model or testing the application.

- `requirements.txt`: A file specifying the Python packages and dependencies required for running this project. You can use it to set up a virtual environment and install the necessary packages.

## How to Run the Streamlit Application

To run the Streamlit application, follow these steps:

1. Make sure you have Python installed on your system.

2. Create a virtual environment and activate it (recommended).

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
