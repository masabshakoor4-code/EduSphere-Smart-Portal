# =====================================
# EduSphere Smart Portal
# Student: Masab Shakoor
# =====================================

import streamlit as st

# -------------------------------
# User Authentication
# -------------------------------
users = {
    "masab": "626462"  # correct credentials
}

def login(username, password):
    # Remove spaces and handle case sensitivity
    username = username.strip().lower()
    password = password.strip()
    if username in users and users[username] == password:
        return True
    else:
        return False

# -------------------------------
# Person Class (Abstraction)
# -------------------------------
class Person:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

# -------------------------------
# Student Class (Inheritance + Encapsulation)
# -------------------------------
class Student(Person):
    def __init__(self, name, student_id, gpa):
        super().__init__(name, student_id)
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa

# -------------------------------
# Course Classes
# -------------------------------
class Course:
    def __init__(self, course_name):
        self.course_name = course_name

class StemCourse(Course):
    def __init__(self, course_name):
        super().__init__(course_name)

# -------------------------------
# Grade Calculator
# -------------------------------
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

# -------------------------------
# Student Database
# -------------------------------
students = {}
data_logs = []

def add_student(name, student_id, gpa):
    student = Student(name, student_id, gpa)
    students[student_id] = student
    data_logs.append((name, student_id, gpa))

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("EduSphere Smart Portal")

# -------------------------------
# Login Section
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader("Login to Access Portal")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if login(username, password):
            st.success("Login Successful!")
            st.session_state.logged_in = True
        else:
            st.error("Incorrect Username or Password")

# -------------------------------
# Portal Section (after login)
# -------------------------------
if st.session_state.logged_in:
    menu = st.selectbox(
        "Select Option",
        ["Add Student", "View Records", "Calculate Grade"]
    )

    # Add Student
    if menu == "Add Student":
        st.subheader("Add New Student")
        name = st.text_input("Student Name")
        student_id = st.text_input("Student ID")
        gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, step=0.01)

        if st.button("Add Student"):
            if name and student_id:
                add_student(name, student_id, gpa)
                st.success("Student Added Successfully")
            else:
                st.error("Please enter all details")

    # View Records
    elif menu == "View Records":
        st.subheader("Student Records")
        if students:
            for sid, student in students.items():
                st.write("Name:", student.name)
                st.write("ID:", sid)
                st.write("GPA:", student.get_gpa())
                st.write("-------------------")
        else:
            st.write("No Records Found")

    # Calculate Grade
    elif menu == "Calculate Grade":
        st.subheader("Grade Calculator")
        score = st.number_input("Enter Score", min_value=0, max_value=100, step=1)
        if st.button("Calculate"):
            grade = calculate_grade(score)
            st.write("Grade:", grade)