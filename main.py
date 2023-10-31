import streamlit as st
import warnings
import pandas as pd
import pickle
import requests
import time

warnings.filterwarnings("ignore", category=UserWarning, module="sklearn.base")
warnings.filterwarnings("ignore", category=FutureWarning, module="sklearn.utils.validation")

arduino_ip = "192.168.4.1"  

def get_sensor_data(endpoint):
    url = f"http://{arduino_ip}/{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

st.title("COVID-19 Vital Readings and Patient Status")


# Debug options
debug_mode = st.checkbox("Debug Mode")
if debug_mode:
    oxygen = st.text_input("Enter SpO2 (Simulated Data):", "98")
    pulse_rate = st.text_input("Enter Heart Rate (Simulated Data):", "80")
    temperature = st.text_input("Enter Temperature (Simulated Data):", "98.6")
else:
    oxygen = None
    pulse_rate = None
    temperature = None

def prediction(oxygen, pulse_rate, temperature):
    st.success(f"SpO2: {oxygen}, Heart Rate: {pulse_rate}, Temperature: {temperature}")

    model_filename = 'best_model_Decision_Tree.pkl'
    with open(model_filename, 'rb') as model_file:
        best_model = pickle.load(model_file)

    # Create a DataFrame with user input
    user_input = pd.DataFrame({'Oxygen': [oxygen], 'PulseRate': [pulse_rate], 'Temperature': [temperature]})


    # Make predictions        
    prediction = best_model.predict(user_input)

    # Optionally, display the probability score for the predicted class
    if hasattr(best_model, 'predict_proba'):
        st.subheader('Predicted Result')
        probabilities = best_model.predict_proba(user_input)

        # Find the class with the highest probability
        predicted_class = best_model.classes_[probabilities.argmax()]
        st.write(f'The predicted result is: {predicted_class}')
        return True


@st.cache_resource
def fetch_sensor_data():
    while True:
        oxygen = get_sensor_data("spo2")
        pulse_rate = get_sensor_data("heartrate")
        temperature = get_sensor_data("temperature")

        st.session_state.oxygen = oxygen
        st.session_state.pulse_rate = pulse_rate
        st.session_state.temperature = temperature
        
        if (st.session_state.oxygen is not None and
            st.session_state.pulse_rate is not None and
            float(st.session_state.oxygen) != 0.0 and
            float(st.session_state.pulse_rate) != 0.0):
            print(f"SpO2: {st.session_state.oxygen}, Heart Rate: {st.session_state.pulse_rate}, Temperature: {st.session_state.temperature}")
            result = prediction(st.session_state.oxygen, st.session_state.pulse_rate, st.session_state.temperature)
            if result:
                exit()
                
        time.sleep(5)


if st.button('Start'):
    fetch_sensor_data()







