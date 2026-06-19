from pydantic import BaseModel,EmailStr, Field

from typing import Optional

class Student(BaseModel):
    name : str="Piyush" #default value
    age:Optional[int]=None #agar kuch value nahi hai to None hogi
    email:EmailStr
    cgpa: float =Field(gt=0,lt=10,default=9)

new_student={'age':'32',"email":'abc@gmail.com',"description": "A decimal value representing the cgpa of the student"}

student=Student(**new_student)

student_dict=dict(student)

print(student_dict['age'])

student_json=student.model_dump_json()

