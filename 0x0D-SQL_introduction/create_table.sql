-- Script that creates a table called first_table
-- If the table first_table already exists, your script should not fail

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

-- Use the database
USE hbtn_0c_0;

-- Create the table
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

