 
import streamlit as st
import pickle
import numpy as np



# Load the trained model
with open("ckd_model.pkl", "rb") as file:
    model = pickle.load(file)

# Function to make predictions
def predict_ckd(features):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return "Chronic Kidney Disease" if prediction[0] == 1 else "No Chronic Kidney Disease"

# Streamlit App UI
st.title("Chronic Kidney Disease Prediction")

st.write("Enter patient details below to predict whether they have CKD.")

# User Inputs
age = st.number_input("Age", min_value=1, max_value=100, step=1)
bp = st.number_input("Blood Pressure (mmHg)", min_value=50, max_value=200, step=1)
sg = st.number_input("Specific Gravity", min_value=1.000, max_value=1.030, step=0.001)
al = st.number_input("Albumin", min_value=0, max_value=5, step=1)
su = st.number_input("Sugar", min_value=0, max_value=5, step=1)
rbc = st.selectbox("Red Blood Cells", ["Normal", "Abnormal"])
pc = st.selectbox("Pus Cell", ["Normal", "Abnormal"])
pcc = st.selectbox("Pus Cell Clumps", ["Not Present", "Present"])
ba = st.selectbox("Bacteria", ["Not Present", "Present"])
bgr = st.number_input("Blood Glucose Random (mg/dL)", min_value=50, max_value=500, step=1)
bu = st.number_input("Blood Urea (mg/dL)", min_value=1, max_value=300, step=1)
sc = st.number_input("Serum Creatinine (mg/dL)", min_value=0.1, max_value=20.0, step=0.1)
sod = st.number_input("Sodium (mEq/L)", min_value=100, max_value=200, step=1)
pot = st.number_input("Potassium (mEq/L)", min_value=1.0, max_value=10.0, step=0.1)
hemo = st.number_input("Hemoglobin (g/dL)", min_value=3.0, max_value=20.0, step=0.1)
pcv = st.number_input("Packed Cell Volume", min_value=10, max_value=60, step=1)
wbcc = st.number_input("White Blood Cell Count (cells/cumm)", min_value=2000, max_value=20000, step=100)
rbcc = st.number_input("Red Blood Cell Count (millions/cumm)", min_value=2.0, max_value=8.0, step=0.1)

# Convert categorical inputs to numerical
rbc = 1 if rbc == "Abnormal" else 0
pc = 1 if pc == "Abnormal" else 0
pcc = 1 if pcc == "Present" else 0
ba = 1 if ba == "Present" else 0

# Predict Button
if st.button("Predict CKD"):
    features = [age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wbcc, rbcc]
    result = predict_ckd(features)
    st.success(f"Prediction: {result}")
