import json
from pathlib import Path
from abc import ABC, abstractmethod

import pandas as pd
import streamlit as st

DATABASE = "school_data.json"

# ----------------------------------------------------------------------------
# Data layer
# ----------------------------------------------------------------------------

def load_data():
    if Path(DATABASE).exists():
        with open(DATABASE, "r") as f:
            content = f.read()
            if content:
                return json.loads(content)
    return {"students": [], "teachers": []}


def save_data(data):
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=4)


if "data" not in st.session_state:
    st.session_state.data = load_data()

data = st.session_state.data


def persist():
    save_data(data)


# ----------------------------------------------------------------------------
# Domain classes (same shape/roles as the original script, minus input())
# ----------------------------------------------------------------------------

class Person(ABC):
    @abstractmethod
    def get_role(self):
        pass

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email


class Student(Person):
    def get_role(self):
        return "Student"

    def register(self, name, age, email, roll_no):
        if not name or not roll_no:
            return False, "Name and roll number are required."
        if not Person.validate_email(email):
            return False, "Invalid email address."
        if any(s["roll_no"] == roll_no for s in data["students"]):
            return False, "A student with this roll number already exists."
        data["students"].append({
            "name": name,
            "age": age,
            "email": email,
            "roll_no": roll_no,
            "grades": {},
        })
        persist()
        return True, f"Student {name} registered."

    def add_grade(self, roll_no, subject, marks):
        for s in data["students"]:
            if s["roll_no"] == roll_no:
                s["grades"][subject] = marks
                persist()
                return True, "Grade added successfully."
        return False, "Student not found."

    def delete(self, roll_no):
        before = len(data["students"])
        data["students"] = [s for s in data["students"] if s["roll_no"] != roll_no]
        if len(data["students"]) < before:
            persist()
            return True, "Student removed."
        return False, "Student not found."


class Teacher(Person):
    def get_role(self):
        return "Teacher"

    def register(self, name, age, email, subject, emp_id):
        if not name or not emp_id:
            return False, "Name and employee ID are required."
        if not Person.validate_email(email):
            return False, "Invalid email address."
        if any(t["emp_id"] == emp_id for t in data["teachers"]):
            return False, "A teacher with this employee ID already exists."
        data["teachers"].append({
            "name": name,
            "age": age,
            "email": email,
            "subject": subject,
            "emp_id": emp_id,
        })
        persist()
        return True, f"Teacher {name} registered."

    def delete(self, emp_id):
        before = len(data["teachers"])
        data["teachers"] = [t for t in data["teachers"] if t["emp_id"] != emp_id]
        if len(data["teachers"]) < before:
            persist()
            return True, "Teacher removed."
        return False, "Teacher not found."


stud = Student()
teach = Teacher()

# ----------------------------------------------------------------------------
# UI
# ----------------------------------------------------------------------------

st.set_page_config(page_title="School Management System", page_icon="🎓", layout="wide")

st.markdown(
    """
    <style>
        .block-container {padding-top: 2rem;}
        div[data-testid="stMetric"] {
            background-color: rgba(120,120,120,0.08);
            border-radius: 10px;
            padding: 12px 16px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎓 School Management System")

col1, col2, col3 = st.columns(3)
col1.metric("Students", len(data["students"]))
col2.metric("Teachers", len(data["teachers"]))
total_grades = sum(len(s["grades"]) for s in data["students"])
col3.metric("Grades recorded", total_grades)

st.divider()

tabs = st.tabs([
    "👨‍🎓 Register Student",
    "👩‍🏫 Register Teacher",
    "📝 Add Grade",
    "📋 Students",
    "📋 Teachers",
])

# --- Register Student --------------------------------------------------
with tabs[0]:
    st.subheader("Register a new student")
    with st.form("register_student", clear_on_submit=True):
        c1, c2 = st.columns(2)
        name = c1.text_input("Name")
        age = c2.number_input("Age", min_value=3, max_value=100, step=1, value=15)
        email = c1.text_input("Email")
        roll_no = c2.text_input("Roll number")
        submitted = st.form_submit_button("Register", type="primary")
        if submitted:
            ok, msg = stud.register(name.strip(), int(age), email.strip(), roll_no.strip())
            if ok:
                st.success(msg)
            else:
                st.error(msg)

# --- Register Teacher ----------------------------------------------------
with tabs[1]:
    st.subheader("Register a new teacher")
    with st.form("register_teacher", clear_on_submit=True):
        c1, c2 = st.columns(2)
        name = c1.text_input("Name", key="t_name")
        age = c2.number_input("Age", min_value=18, max_value=100, step=1, value=30, key="t_age")
        email = c1.text_input("Email", key="t_email")
        subject = c2.text_input("Subject department", key="t_subject")
        emp_id = c1.text_input("Employee ID", key="t_emp_id")
        submitted = st.form_submit_button("Register", type="primary")
        if submitted:
            ok, msg = teach.register(name.strip(), int(age), email.strip(), subject.strip(), emp_id.strip())
            if ok:
                st.success(msg)
            else:
                st.error(msg)

# --- Add Grade -------------------------------------------------------------
with tabs[2]:
    st.subheader("Add a grade")
    if not data["students"]:
        st.info("No students registered yet.")
    else:
        roll_options = {f'{s["name"]} ({s["roll_no"]})': s["roll_no"] for s in data["students"]}
        with st.form("add_grade", clear_on_submit=True):
            choice = st.selectbox("Student", list(roll_options.keys()))
            subject = st.text_input("Subject")
            marks = st.number_input("Marks", min_value=0.0, max_value=100.0, step=0.5)
            submitted = st.form_submit_button("Add grade", type="primary")
            if submitted:
                if not subject.strip():
                    st.error("Subject is required.")
                else:
                    ok, msg = stud.add_grade(roll_options[choice], subject.strip(), float(marks))
                    if ok:
                        st.success(msg)
                    else:
                        st.error(msg)

# --- Students list -----------------------------------------------------
with tabs[3]:
    st.subheader("All students")
    if not data["students"]:
        st.info("No students registered yet.")
    else:
        rows = []
        for s in data["students"]:
            avg = (sum(s["grades"].values()) / len(s["grades"])) if s["grades"] else None
            rows.append({
                "Name": s["name"],
                "Roll No.": s["roll_no"],
                "Age": s["age"],
                "Email": s["email"],
                "Subjects graded": len(s["grades"]),
                "Average": round(avg, 1) if avg is not None else "—",
            })
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

        with st.expander("View grade breakdown for a student"):
            roll_options = {f'{s["name"]} ({s["roll_no"]})': s["roll_no"] for s in data["students"]}
            choice = st.selectbox("Student", list(roll_options.keys()), key="detail_choice")
            chosen = next(s for s in data["students"] if s["roll_no"] == roll_options[choice])
            if chosen["grades"]:
                st.table(pd.DataFrame(chosen["grades"].items(), columns=["Subject", "Marks"]))
            else:
                st.write("No grades recorded yet.")

        with st.expander("Remove a student"):
            roll_options = {f'{s["name"]} ({s["roll_no"]})': s["roll_no"] for s in data["students"]}
            choice = st.selectbox("Student to remove", list(roll_options.keys()), key="del_stud")
            if st.button("Delete student", type="secondary"):
                ok, msg = stud.delete(roll_options[choice])
                if ok:
                    st.success(msg)
                else:
                    st.error(msg)
                st.rerun()

# --- Teachers list -------------------------------------------------------
with tabs[4]:
    st.subheader("All teachers")
    if not data["teachers"]:
        st.info("No teachers registered yet.")
    else:
        rows = [{
            "Name": t["name"],
            "Employee ID": t["emp_id"],
            "Age": t["age"],
            "Email": t["email"],
            "Subject": t["subject"],
        } for t in data["teachers"]]
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

        with st.expander("Remove a teacher"):
            emp_options = {f'{t["name"]} ({t["emp_id"]})': t["emp_id"] for t in data["teachers"]}
            choice = st.selectbox("Teacher to remove", list(emp_options.keys()), key="del_teach")
            if st.button("Delete teacher", type="secondary"):
                ok, msg = teach.delete(emp_options[choice])
                if ok:
                    st.success(msg)
                else:
                    st.error(msg)
                st.rerun()