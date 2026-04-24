# Question 1: Lists

data = [10, 20, 30, 40, 50, 20, 30, 60, [70, 80], 90]

data.append([100, 110])

data.extend([120, 130])

data.insert(2, 25)

data.remove(20)

last_element = data.pop()

count_30 = data.count(30)

index_40 = data.index(40)

data.reverse()

print("List after operations:", data)
print("Popped element:", last_element)
print("Count of 30:", count_30)
print("Index of 40:", index_40)

# data.sort()  This will give error because of nested list [70, 80]

flat_data = []
for item in data:
    if isinstance(item, list):
        flat_data.extend(item)
    else:
        flat_data.append(item)

print("Flattened list:", flat_data)
