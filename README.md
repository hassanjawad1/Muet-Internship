Assignment Uploader Website by Hassan Jawad

This Streamlit web application is designed for uploading and managing assignments for students, teachers, and administrators.

## Features

- Select user role (Admin, Student, Teacher) and table (student, submission, Courses, assignment).
- Display data from the selected table.
- Connects to a SQL Server database to retrieve and display data.

## Prerequisites

- Python 3.x installed
- Required Python packages: `streamlit`, `pandas`, `sqlalchemy`

## Setup

1. Install the required packages:

2. Configure the SQL Server connection:
- Open the `main.py` file and replace the connection details in the `conn_str` variable with your SQL Server details.

3. Run the Streamlit app:

## SQL Database Schema

### `student` Table

- `StudentID` INT PRIMARY KEY
- `StudentName` VARCHAR(50)
- `StudentRollNumber` VARCHAR(20)

### `assignment` Table

- `AssignmentID` INT PRIMARY KEY
- `AssignmentName` VARCHAR(50)
- `Deadline` DATE

### `Courses` Table

- `CourseID` INT PRIMARY KEY
- `CourseName` VARCHAR(50)

### `submission` Table

- `SubmissionID` INT PRIMARY KEY
- `StudentID` INT (FOREIGN KEY referencing `student`)
- `AssignmentID` INT (FOREIGN KEY referencing `assignment`)
- `SubmissionDate` DATE
- `PDFFilePath` VARCHAR(255)
- `CourseID` INT (FOREIGN KEY referencing `courses`)

## Sample Data

- Sample data has been inserted into the tables `student`, `assignment`, `Courses`, and `submission`.

---
