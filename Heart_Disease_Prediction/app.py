import streamlit as st
import pandas as pd
import joblib
# Load the pre-trained model
model = joblib.load('heart_disease_model.pkl')
scaler = joblib.load('scaler.pkl')
expecqted_columns=joblib.load('columns.pkl')

st.title('Heart Stroke Prediction App by Tannoo')
st.markdown('This app predicts the likelihood of heart disease based on user input.')

age = st.slider('Age', 18, 100, 30)
sex = st.selectbox('sex',['M', 'F'])
chest_pain = st.selectbox('chest_pain', ['ATA', 'NAP', 'ASY', 'TA'])
resting_bp = st.number_input('Resting Blood Pressure', min_value=80, max_value=200, value=120)
cholesterol = st.number_input('Cholesterol', min_value=100, max_value=600, value=200)
fasting_blood_sugar = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
resting_ecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST', 'LVH'])
max_heart_rate = st.slider('Maximum Heart Rate', 60, 220, 150)
exercise_angina = st.selectbox('Exercise Induced Angina', ["Yes", "No"])
oldpeak = st.number_input('Oldpeak', min_value=0.0, max_value=6.0, value=1.0)
slope = st.selectbox('Slope of ST Segment', ['Up', 'Flat', 'Down'])

if st.button('Predict'):
    
    raw_data = {
        'age': age,
        'sex': sex,
        'chest_pain': chest_pain,
        'resting_bp': resting_bp,
        'cholesterol': cholesterol,
        'fasting_blood_sugar': fasting_blood_sugar,
        'resting_ecg': resting_ecg,
        'max_heart_rate': max_heart_rate,
        'exercise_angina': exercise_angina,
        'oldpeak': oldpeak,
        'slope': slope

    }
    # Create a DataFrame for the input data
    input_data = pd.DataFrame([raw_data])
    for col in expecqted_columns:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[expecqted_columns]
    # scaled_data = scaler.transform(input_data)
    prediction = model.predict(input_data)[0]
    # prediction_proba = model.predict_proba(input_data)
    if prediction == 1:
        st.error('High risk of Heart Disease')
    else:
        st.success('Low risk of Heart Disease')




