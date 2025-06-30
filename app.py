# Generating the complete Streamlit dashboard code for app.py
code = """
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Set page config
st.set_page_config(page_title="Employee Attrition Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("EA.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("Filter the Data")
departments = st.sidebar.multiselect("Department", options=df["Department"].unique(), default=df["Department"].unique())
genders = st.sidebar.multiselect("Gender", options=df["Gender"].unique(), default=df["Gender"].unique())
ages = st.sidebar.slider("Age", int(df["Age"].min()), int(df["Age"].max()), (25, 45))

filtered_df = df[
    (df["Department"].isin(departments)) &
    (df["Gender"].isin(genders)) &
    (df["Age"] >= ages[0]) & (df["Age"] <= ages[1])
]

st.title("📊 Employee Attrition Insights Dashboard")
st.markdown("This interactive dashboard provides insights into employee attrition for strategic decision-making by HR and leadership.")

# Summary stats
st.header("1. Overall Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Employees", df.shape[0])
col2.metric("Attrition Rate", f"{(df['Attrition'].value_counts(normalize=True).get('Yes', 0) * 100):.2f}%")
col3.metric("Filtered Records", filtered_df.shape[0])

# Visuals section
st.header("2. Key Visualizations")

st.subheader("2.1 Attrition Count")
st.markdown("Distribution of attrition in the organization.")
fig1 = px.histogram(filtered_df, x="Attrition", color="Attrition")
st.plotly_chart(fig1)

st.subheader("2.2 Attrition by Department")
st.markdown("Which departments face higher attrition?")
fig2 = px.histogram(filtered_df, x="Department", color="Attrition", barmode="group")
st.plotly_chart(fig2)

st.subheader("2.3 Age Distribution")
st.markdown("Age-wise breakdown of employees and their attrition status.")
fig3 = px.histogram(filtered_df, x="Age", color="Attrition", nbins=30)
st.plotly_chart(fig3)

st.subheader("2.4 Monthly Income Distribution")
st.markdown("Income levels of employees and how they relate to attrition.")
fig4 = px.box(filtered_df, x="Attrition", y="MonthlyIncome", color="Attrition")
st.plotly_chart(fig4)

st.subheader("2.5 Attrition by Job Role")
st.markdown("Some roles have higher turnover. This graph reveals which.")
fig5 = px.histogram(filtered_df, x="JobRole", color="Attrition", barmode="group")
st.plotly_chart(fig5)

st.subheader("2.6 Attrition by Marital Status")
fig6 = px.histogram(filtered_df, x="MaritalStatus", color="Attrition", barmode="group")
st.plotly_chart(fig6)

st.subheader("2.7 Job Satisfaction Levels")
st.markdown("Higher attrition often correlates with lower satisfaction.")
fig7 = sns.countplot(data=filtered_df, x="JobSatisfaction", hue="Attrition")
st.pyplot(fig7.figure)

st.subheader("2.8 Overtime vs Attrition")
fig8 = px.pie(filtered_df, names="OverTime", color="Attrition", title="Overtime and Attrition")
st.plotly_chart(fig8)

st.subheader("2.9 Heatmap of Feature Correlations")
st.markdown("Visualizing correlations among numerical features.")
corr = filtered_df.select_dtypes("number").corr()
fig9, ax = plt.subplots(figsize=(12,8))
sns.heatmap(corr, annot=True, fmt=".1f", cmap="coolwarm", ax=ax)
st.pyplot(fig9)

st.subheader("2.10 Distance from Home vs Attrition")
st.markdown("Farther commute could indicate higher attrition.")
fig10 = px.box(filtered_df, x="Attrition", y="DistanceFromHome", color="Attrition")
st.plotly_chart(fig10)

# Data Table
st.header("3. View Filtered Data")
st.markdown("Below is the data matching selected filters.")
st.dataframe(filtered_df)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit.")
"""
with open("/mnt/data/app.py", "w") as f:
    f.write(code)

