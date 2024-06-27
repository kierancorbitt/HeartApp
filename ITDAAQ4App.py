import streamlit as st
import pandas as pd
import numpy as np

def get_user_input():
    
    age = st.sidebar.number_input('Age', min_value=1, max_value=100)
    sex = st.sidebar.selectbox('Sex', ('Male', 'Female'))
    cp = st.sidebar.selectbox('Chest Pain Type', ('Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'))
    trestbps = st.sidebar.number_input('Resting Blood Pressure (mm Hg)', min_value=50, max_value=200)
    chol = st.sidebar.number_input('Serum Cholesterol (mg/dl)', min_value=100, max_value=500)
    fbs = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl', ('True', 'False'))
    restecg = st.sidebar.selectbox('Resting Electrocardiographic Results', ('Normal', 'Abnormal', 'Ventricular Hypertrophy'))
    thalach = st.sidebar.number_input('Maximum Heart Rate Achieved', min_value=50, max_value=220)
    exang = st.sidebar.selectbox('Exercise Induced Angina', ('Yes', 'No'))
    oldpeak = st.sidebar.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0)
    slope = st.sidebar.selectbox('Slope of the Peak Exercise ST Segment', ('Upsloping', 'Flat', 'Downsloping'))
    ca = st.sidebar.number_input('Number of Major Vessels Colored by Fluoroscopy', min_value=0, max_value=4)
    thal = st.sidebar.selectbox('Thalassemia', ('Normal', 'Fixed Defect', 'Reversible Defect', 'Unknown'))

    user_input = {'age': age,
                 'sex': 1 if sex == 'Male' else 0,
                 'cp': cp,
                 'trestbps': trestbps,
                 'chol': chol,
                 'fbs': 1 if fbs == 'True' else 0,
                 'restecg': restecg,
                 'thalach': thalach,
                 'exang': 1 if exang == 'Yes' else 0,
                 'oldpeak': oldpeak,
                 'slope': slope,
                 'ca': ca,
                 'thal': thal}
    
    features = pd.DataFrame(user_input, index=[0])
    return features

def main():
    st.title("Heart Disease Prediction")
    st.write("Enter the details of the patient.")

    user_input = get_user_input()
    
    st.subheader("Patient Details")
    st.write(user_input)

    cp_mapping = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
    slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
    thal_mapping = {'Normal': 1, 'Fixed Defect': 2, 'Reversible Defect': 3, 'Unknown': 0}
    restecg_mapping = {'Normal': 0, 'Abnormal': 1, 'Ventricular Hypertrophy': 2}
    
    user_input['cp'] = user_input['cp'].map(cp_mapping)
    user_input['slope'] = user_input['slope'].map(slope_mapping)
    user_input['thal'] = user_input['thal'].map(thal_mapping)
    user_input['restecg'] = user_input['restecg'].map(restecg_mapping)

    st.subheader("Prediction")
    heart_disease = "Yes" if prediction[0] == 1 else "No"
    st.write(f"Heart Disease: {heart_disease}")
    
    st.subheader("Prediction Probability")
    st.write(f"Probability of having heart disease: ")
    st.write(f"Probability of being healthy: ")

# Running the app
if __name__ == '__main__':
    main()
