import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/students_job_data.csv")

# Title
st.title("🎓 Student Job Journey Analysis Dashboard")

# -----------------------
# Dataset Overview
# -----------------------
st.subheader("📊 Dataset Overview")
st.write(df.head())

st.subheader("📌 Dataset Info")
st.write(df.describe())

# -----------------------
# Placement Distribution
# -----------------------
st.subheader("🎯 Placement Distribution")
fig1, ax1 = plt.subplots()
sns.countplot(x="Placement", data=df, ax=ax1)
st.pyplot(fig1)

# -----------------------
# CGPA vs Salary
# -----------------------
st.subheader("📈 CGPA vs Salary")
fig2, ax2 = plt.subplots()
sns.scatterplot(x="CGPA", y="Salary_LPA", data=df, ax=ax2)
st.pyplot(fig2)

# -----------------------
# Attendance vs Placement
# -----------------------
st.subheader("📊 Attendance vs Placement")
fig3, ax3 = plt.subplots()
sns.boxplot(x="Placement", y="Attendance", data=df, ax=ax3)
st.pyplot(fig3)