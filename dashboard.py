import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# MySQL Connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="crimedb"
)

query = "SELECT * FROM Crime"
df = pd.read_sql(query, connection)

st.set_page_config(page_title="Crime Intelligence Dashboard", layout="wide")

st.title("🚔 Crime Intelligence Data Platform")
st.write("Analyze crime trends, hotspots, and case status.")

# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Crimes", len(df))

with col2:
    solved = len(df[df["Status"] == "Solved"])
    st.metric("Solved Cases", solved)

with col3:
    pending = len(df[df["Status"] == "Pending"])
    st.metric("Pending Cases", pending)

st.divider()

# Crime Type Chart
st.subheader("Crime Type Distribution")

crime_counts = df["Crime_Type"].value_counts()

fig, ax = plt.subplots(figsize=(8,4))
crime_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Crime Type")
ax.set_ylabel("Count")
st.pyplot(fig)

# Hotspots
st.subheader("Crime Hotspots")

location_counts = df["Location"].value_counts()

fig2, ax2 = plt.subplots(figsize=(8,4))
location_counts.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Location")
ax2.set_ylabel("Crimes")
st.pyplot(fig2)

# Pie Chart
st.subheader("Solved vs Pending")

status_counts = df["Status"].value_counts()

fig3, ax3 = plt.subplots(figsize=(6,6))
status_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax3)
ax3.set_ylabel("")
st.pyplot(fig3)

connection.close()