# FLU Vital Readings and Patient Status Monitoring

![FLU Vital Readings and Patient Status Monitoring](project_image.png)

This is a Streamlit web application for monitoring FLU vital readings and predicting patient status based on the provided vital readings. The application allows you to input simulated vital readings for SpO2 (oxygen saturation), heart rate, and body temperature. It can also connect to an Arduino device to fetch real-time sensor data from it.

## Table of Contents

- [Files and Directory Structure](#files-and-directory-structure)
- [How to Run the Streamlit Application](#how-to-run-the-streamlit-application)
- [Functionality](#functionality)
- [Important Note](#important-note)
- [License](#license)

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
Install the required Python packages by running:
bash
Copy code
pip install -r requirements.txt
Run the Streamlit application by executing main.py:
bash
Copy code
streamlit run main.py
The Streamlit web application should open in your default web browser. You can interact with the application to input simulated vital readings or connect to an Arduino device for real-time sensor data.
Functionality
Debug Mode: You can enable the debug mode to input simulated vital readings for SpO2, heart rate, and temperature.

Start Button: Clicking the "Start" button initiates the real-time data fetch from an Arduino device. The application will continuously update the vital readings and predict the patient status based on these readings.

Prediction: The application uses the trained Decision Tree model to predict the patient's status. It displays the predicted result and, if available, the probability score for the predicted class.

Important Note
Make sure to have the best_model_Decision_Tree.pkl file in the same directory as main.py, as the application loads the model from this file.
This Streamlit application provides a simple interface for monitoring and predicting patient status based on FLU vital readings. It can be customized and expanded as needed for specific use cases.
