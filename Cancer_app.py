import streamlit as st
import numpy as np
import pickle

# Load trained SVM model
with open('breast_cancer_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load scaler
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Load the feature list (20 selected features after dropping correlated ones)
with open('feature_list.pkl', 'rb') as feature_file:
    features = pickle.load(feature_file)

# Streamlit app setup
st.set_page_config(page_title="Breast Cancer Prediction", layout="centered")
st.title("🩺 Breast Cancer Prediction App")
st.markdown("Enter the values for the selected clinical features below:")

# Create number input for each feature
user_input = []
for feat in features:
    value = st.number_input(f"{feat}", min_value=0.0, format="%.4f")
    user_input.append(value)

# Predict when button is clicked
if st.button("🔍 Predict"):
    input_array = np.array(user_input).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]
    proba = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"🔴 Likely Malignant (Cancer). Confidence: {proba:.2%}")
    else:
        st.success(f"🟢 Likely Benign. Confidence: {proba:.2%}")
