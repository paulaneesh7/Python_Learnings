from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name: str = 'Aneesh'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')
    
    
    
new_student = {'name': "Lemon", 'age': 25, 'email': 'abc@gmail.com', 'cgpa': 6}

student = Student(**new_student)

# Convertion to dict
student_dict = dict(student)

print(student_dict['age'])


# Convertion to json

student_json = student.model_dump_json()

print(student_json)