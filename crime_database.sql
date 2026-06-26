-- Create Database
CREATE DATABASE CrimeDB;

-- Select Database
USE CrimeDB;

-- Create Crime Table
CREATE TABLE Crime (
    Crime_ID INT PRIMARY KEY,
    Crime_Type VARCHAR(50),
    Location VARCHAR(50),
    Crime_Date DATE,
    Crime_Time VARCHAR(20),
    Victim_Age INT,
    Gender VARCHAR(10),
    Status VARCHAR(20)
);

-- View Table Structure
DESCRIBE Crime;

-- Display Records
SELECT * FROM Crime;