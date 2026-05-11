import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# PAGE CONFIG (PRO LOOK)
# ---------------------------
st.set_page_config(
    page_title="Student Job Analysis",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------
# LOAD DATA
# ---------------------------
df = pd.read_csv("data/students_job_data.csv")

# ---------------------------
# SIDEBAR FILTERS (PRO FEATURE)
# ---------------------------
st.sidebar.title("🔎 Filters")

cgpa_filter = st.sidebar.slider("Minimum CGPA", 0.0, 10.0, 5.0)
intern_filter = st.sidebar.selectbox("Internships", sorted(df["Internships"].unique()))

filtered_df = df[
    (df["CGPA"] >= cgpa_filter) &
    (df["Internships"] == intern_filter)
]

# ---------------------------
# HEADER
# ---------------------------
st.title("🎓 Student Job Journey Analysis Dashboard")
st.markdown("### 📊 HR-Friendly Analytics & Placement Insights")

# ---------------------------
# KPI METRICS (VERY IMPORTANT FOR IMPRESSION)
# ---------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(df))
col2.metric("Placed Students", df["Placement"].sum())
col3.metric("Placement Rate", f"{df['Placement'].mean()*100:.2f}%")

st.markdown("---")

# ---------------------------
# DATA PREVIEW
# ---------------------------
st.subheader("📌 Filtered Data Preview")
st.dataframe(filtered_df)

# ---------------------------
# VISUALIZATION 1
# ---------------------------
st.subheader("🎯 Placement Distribution")

fig1, ax1 = plt.subplots()
sns.countplot(x="Placement", data=df, ax=ax1)
st.pyplot(fig1)

# ---------------------------
# VISUALIZATION 2
# ---------------------------
st.subheader("📈 CGPA vs Salary")

fig2, ax2 = plt.subplots()
sns.scatterplot(x="CGPA", y="Salary_LPA", data=df, ax=ax2)
st.pyplot(fig2)

# ---------------------------
# VISUALIZATION 3
# ---------------------------
st.subheader("📊 Attendance vs Placement")

fig3, ax3 = plt.subplots()
sns.boxplot(x="Placement", y="Attendance", data=df, ax=ax3)
st.pyplot(fig3)

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
st.markdown("🚀 Built by Ruchitha| Streamlit ML Project | Student Job Analysis")