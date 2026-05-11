import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

# Load data
df = pd.read_csv("students_job_data.csv")

# Encode target
le = LabelEncoder()
df["Placement"] = le.fit_transform(df["Placement"])

# Features & target
X = df.drop("Placement", axis=1)
y = df["Placement"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# UI Title
st.title("🎓 Student Job Journey Predictor")
st.write("Enter student details to predict placement")

# Input fields
cgpa = st.number_input("CGPA", 0.0, 10.0, 7.0)
attendance = st.number_input("Attendance %", 0, 100, 80)
internships = st.number_input("Internships", 0, 10, 1)
certifications = st.number_input("Certifications", 0, 10, 1)
communication = st.number_input("Communication Skills (1-10)", 1, 10, 5)
placed_input = 0  # placeholder (not needed for prediction input)
salary = 0  # placeholder

# Prediction button
if st.button("Predict Placement"):
    input_data = [[cgpa, attendance, internships, certifications, communication, 0, 0]]
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("🎉 Student will be PLACED")
    else:
        st.error("❌ Student may NOT be placed")