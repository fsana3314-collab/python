import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 🎓 Student Class
class Student:
    def _init_(self, roll, name, marks):
        self.roll, self.name, self.marks = roll, name, marks
    def total(self): return np.sum(list(self.marks.values()))
    def avg(self): return np.mean(list(self.marks.values()))
    def grade(self):
        a=self.avg()
        return "A+" if a>=90 else "A" if a>=75 else "B" if a>=60 else "C" if a>=40 else "F"

st.title("📊 Student Marks Analysis")

# Upload CSV
file = st.file_uploader("Upload CSV file", type="csv")
if file:
    df = pd.read_csv(file)
    st.dataframe(df)

    # Create students
    students = [Student(r["Roll No"], r["Name"], r.drop(["Roll No","Name"]).to_dict()) for _,r in df.iterrows()]

    # Class average
    st.subheader("Class Average")
    st.write(df.drop(["Roll No","Name"], axis=1).mean())

    # Topper
    df["Total"] = df.drop(["Roll No","Name"], axis=1).sum(axis=1)
    top = df.loc[df["Total"].idxmax()]
    st.success(f"🏆 Topper: {top['Name']} ({top['Total']} marks)")

    # Subject Average Plot
    fig, ax = plt.subplots()
    df.drop(["Roll No","Name"], axis=1).mean().plot(kind="bar", ax=ax)
    st.pyplot(fig)

    # Individual Student
    st.subheader("Individual Performance")
    choice = st.selectbox("Select Student", [s.name for s in students])
    s = [x for x in students if x.name == choice][0]
    st.write(f"Marks: {s.marks}")
    st.write(f"Total: {s.total()} | Avg: {s.avg():.2f} | Grade: {s.grade()}")