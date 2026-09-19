student = {"name" : "Aarav", "age":13, "grade":7}
print(student.get("age"))
print(student.get("school", "N/A"))

student["age"] = 14

student["school"] = "Sunrise Academy"
print(student)

student.pop("grade")
print(student)

student.clear()
print(student)
