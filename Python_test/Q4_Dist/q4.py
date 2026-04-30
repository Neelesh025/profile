student = {
    "name": "John",
    "age": 21,
    "marks": {"math": 80, "science": 90}
}

print("Name:", student.get("name"))

student["grade"] = "A"

student.update({"age": 22})

student.pop("age")

student.popitem()

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

student.setdefault("city", "Delhi")

student.update({"country": "India"})

print("Final student:", student)
