import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",   
    database="crimedb"
)

# Read data from MySQL
query = "SELECT * FROM Crime"
df = pd.read_sql(query, connection)

print("\nCrime Dataset")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

# -----------------------------
# Crime Type Distribution
# -----------------------------
crime_counts = df["Crime_Type"].value_counts()

plt.figure(figsize=(8,5))
crime_counts.plot(kind="bar")
plt.title("Crime Type Distribution")
plt.xlabel("Crime Type")
plt.ylabel("Number of Crimes")
plt.tight_layout()
plt.savefig("crime_type_distribution.png")
plt.show()

# -----------------------------
# Crime Hotspots
# -----------------------------
location_counts = df["Location"].value_counts()

plt.figure(figsize=(8,5))
location_counts.plot(kind="bar")
plt.title("Crime Hotspots")
plt.xlabel("Location")
plt.ylabel("Number of Crimes")
plt.tight_layout()
plt.savefig("crime_hotspots.png")
plt.show()

# -----------------------------
# Solved vs Pending
# -----------------------------
status_counts = df["Status"].value_counts()

plt.figure(figsize=(6,6))
status_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Solved vs Pending Cases")
plt.ylabel("")
plt.savefig("crime_status.png")
plt.show()

connection.close()