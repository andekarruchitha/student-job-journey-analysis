import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="Student Job Analysis", layout="wide")

st.title("🎓 Student Job Journey Analysis Dashboard")

# ---------------------------
# LOAD DATA (SAFE PATH)
# ---------------------------
df = pd.read_csv("data/students_job_data.csv")

# FIX: convert Placement Yes/No → 1/0
df["Placement"] = df["Placement"].astype(str).str.strip().map({"Yes": 1, "No": 0})

# ---------------------------
# DEBUG CHECK (IMPORTANT)
# ---------------------------
st.write("Data Loaded Successfully ✔")
st.write(df.head())

# ---------------------------
# KPI METRICS
# ---------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(df))
col2.metric("Placed Students", int(df["Placement"].sum()))
col3.metric("Placement Rate", f"{df['Placement'].mean()*100:.2f}%")

st.markdown("---")

# ---------------------------
# CHART 1: PLACEMENT
# ---------------------------
st.subheader("Placement Distribution")

fig1, ax1 = plt.subplots()
sns.countplot(x="Placement", data=df, ax=ax1)
st.pyplot(fig1)

# ---------------------------
# CHART 2: CGPA vs SALARY
# ---------------------------
st.subheader("CGPA vs Salary")

fig2, ax2 = plt.subplots()
sns.scatterplot(x="CGPA", y="Salary_LPA", data=df, ax=ax2)
st.pyplot(fig2)

# ---------------------------
# CHART 3: ATTENDANCE
# ---------------------------
st.subheader("Attendance vs Placement")

fig3, ax3 = plt.subplots()
sns.boxplot(x="Placement", y="Attendance", data=df, ax=ax3)
st.pyplot(fig3)