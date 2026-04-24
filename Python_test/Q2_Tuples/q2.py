# Question 2: Tuples

t = (10, 20, 30, 40, 50, 20, 60)

print("Count of 20:", t.count(20))
print("Index of 40:", t.index(40))

temp = list(t)
temp.append(70)
t = tuple(temp)

print("After adding 70:", t)

print("Slice (2 to 5):", t[2:6])

t = t + (80, 90)

print("Repeated tuple:", t * 2)

