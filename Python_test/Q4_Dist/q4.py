# Question 4: Dictionary

student = {
    "name": "John",
    "age": 21,
    "marks": {"math": 80, "science": 90}
}

print("Name:", student.get("name"))

# add
student["grade"] = "A"

# update
student.update({"age": 22})

# pop
student.pop("age")

# popitem
student.popitem()

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# setdefault
student.setdefault("city", "Delhi")

# merge
student.update({"country": "India"})

print("Final student:", student)