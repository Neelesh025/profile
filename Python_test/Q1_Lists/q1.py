# Question 1: Lists

data = [10, 20, 30, 40, 50, 20, 30, 60, [70, 80], 90]

# append
data.append([100, 110])

# extend
data.extend([120, 130])

# insert
data.insert(2, 25)

# remove first 20
data.remove(20)

# pop last element
last_element = data.pop()

# count 30
count_30 = data.count(30)

# index of 40
index_40 = data.index(40)

# reverse
data.reverse()

print("List after operations:", data)
print("Popped element:", last_element)
print("Count of 30:", count_30)
print("Index of 40:", index_40)

# sort issue
# data.sort() ❌ This will give error because of nested list [70, 80]

# flatten nested list
flat_data = []
for item in data:
    if isinstance(item, list):
        flat_data.extend(item)
    else:
        flat_data.append(item)

print("Flattened list:", flat_data)