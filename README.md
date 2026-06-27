Crime Intelligence Data Platform

Overview

The Crime Intelligence Data Platform is a Python-based data analytics dashboard that helps analyze crime records stored in a MySQL database. The platform provides visual insights into crime trends, crime hotspots, and case status using an interactive Streamlit dashboard.

The main objective of this project is to help law enforcement agencies identify crime patterns and support data-driven decision-making.

Technologies Used

• Python

• Streamlit

• MySQL

• Pandas

• Matplotlib

• MySQL Connector

Features

• Connects to a MySQL database

• Retrieves crime records using SQL queries

• Displays Key Performance Indicators (KPIs)

• Crime Type Distribution Analysis

• Crime Hotspot Analysis

• Solved vs Pending Case Analysis

• Interactive dashboard using Streamlit

Project Workflow

Connect to the MySQL database.
Retrieve crime records using SQL queries.
Load the data into a Pandas DataFrame.
Analyze the data.
Generate charts using Matplotlib.
Display KPIs and visualizations in the Streamlit dashboard.

Database

Database Name: crimedb

Table Name: Crime

Example Columns

• Crime_ID

• Crime_Type

• Location

• Date

• Status

Configure MySQL

Update the database credentials in the Python file.

connection = mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="crimedb"
)

Run the Application

streamlit run app.py

Open the browser and navigate to:

http://localhost:8501

Dashboard Modules

• Total Crimes

• Solved Cases

• Pending Cases

• Crime Type Distribution

• Crime Hotspots

• Solved vs Pending Cases

Future Enhancements

• Crime Prediction using Machine Learning

• Real-time Crime Monitoring

• Interactive Crime Maps

• User Authentication

• Role-Based Access Control

• Cloud Deployment


