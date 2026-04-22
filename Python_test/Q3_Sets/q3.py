# Question 3: Sets

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

# add
s1.add(60)

# update
s1.update([70, 80, 90])

# remove
s1.remove(20)

# discard
s1.discard(100)

# pop
removed = s1.pop()

# copy
copy_set = s1.copy()
copy_set.add(999)

print("Original set:", s1)
print("Copied set:", copy_set)

# clear
s2.clear()
print("Length after clear:", len(s2))

# deduplication
lst = [1,2,2,3,3,4]
unique = set(lst)
