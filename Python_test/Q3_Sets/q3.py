s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

s1.add(60)

s1.update([70, 80, 90])

s1.remove(20)

s1.discard(100)

removed = s1.pop()

copy_set = s1.copy()
copy_set.add(999)

print("Original set:", s1)
print("Copied set:", copy_set)

s2.clear()
print("Length after clear:", len(s2))

lst = [1,2,2,3,3,4]
unique = set(lst)
