import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Student Job Journey Analysis", layout="wide")

# Title
st.title("🎓 Student Job Journey Analysis Dashboard")
st.markdown("Analyze student data and placement trends using Data Science 🚀")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/students_job_data.csv")
    return df

df = load_data()

# Sidebar
st.sidebar.header("Filters")
selected_option = st.sidebar.selectbox("Choose Analysis", 
                                       ["Overview", "Placement Distribution", "CGPA vs Salary"])

# ---------------- OVERVIEW ----------------
if selected_option == "Overview":
    st.subheader("📊 Dataset Overview")
    st.write(df.head())

    st.write("### Dataset Info")
    st.write(df.describe())

# ---------------- PLACEMENT ----------------
elif selected_option == "Placement Distribution":
    st.subheader("📌 Placement Distribution")

    fig, ax = plt.subplots()
    sns.countplot(x="Placement", data=df, palette="Set2", ax=ax)

    st.pyplot(fig)

    st.image("images/chart.png", caption="Placement Analysis Chart")

# ---------------- CGPA VS SALARY ----------------
elif selected_option == "CGPA vs Salary":
    st.subheader("📈 CGPA vs Salary Analysis")

    fig, ax = plt.subplots()
    sns.scatterplot(x="CGPA", y="Salary", data=df, ax=ax)

    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit | Student Project")