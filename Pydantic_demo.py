from pydantic import BaseModel, EmailStr, Field  # 1. Field import kiya aur extra comma hataya
from typing import Optional

# 1. Class define karein
class Student(BaseModel):
    name: str
    id: int
    name1: str = 'usman'
    age: Optional[int] = None
    email: EmailStr
    
    # 2. lt=10 ka sahi syntax use kiya aur default value bhi da saskte hoo aur description bhi da sakte hoo
    cgpa: float = Field(gt=0, lt=10,default=6,description='a decimal value can represnet the cgpa of the student')

# 2. Class se BAHAR data define karein (Extra space hataya)
# Aapne sahi kaha! '19' string ko Pydantic automatically int(19) mein convert kar dega.
new_student = {'name': 'Abdullah', 'id': '3743284','age': '19', 'email': 'abdullah@gmail.com', }

# Object create karein
student = Student(**new_student)

# 3. Print karein
print("--- Full Object ---")
# isko hum json aur dick ma bhi convert kar skste hai
print(student)
student_dict=dict(student)
print(student_dict['age'])
print("\n--- Specific Fields ---")
print("Name:", student.name)
print("Age (Converted):", student.age, type(student.age)) # Type check karne ke liye
print("Email:", student.email)
print("CGPA:", student.cgpa)
print("name1:", student.name1)
print(student_dict['age'])
print(student_dict['cgpa'])
student_json=student.model_dump_json()