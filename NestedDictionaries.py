students = {
    "Priya": {"Math": 90, "English": 85},
    "Khushi": {"Math": 88, "English": 92},
    "Rahul": {"Math": 72, "English": 78},
}

# Access nested value
print(students["Khushi"]["Math"]) 

# Adding a new subject
students["Priya"]["Science"] = 95
print(students["Priya"])  

