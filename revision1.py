# w1 = [1, 2, 3, 56]
# print(type(w1))
# print(w1)

# print(w1[0])
# print(w1[1])
# print(w1[2])
# print(w1[3])

# print(len(w1))

# a1 = ["aana", 2.3, 12]
# print(type(a1[0]))
# print(type(a1[1]))
# print(type(a1[2]))

# print(a1[-2])

# if 2.3 in a1:
#     print("yes")
# else:
#     print("no")

# if "na" in "aana":
#     print("yes")
# else:
#     print("no")

# even = [i for i in range(20) if i%2 == 0]
# print(even)

# l = [1, 2, 3, 4, 5]
# l.append(6)
# print(l)

s = [223, 4, 555, 6454, 677, 33422123, 56]
s.sort()
print(s)
s.sort(reverse=True)
print(s)

print(s.count(6))

s.insert(1, 40)
print(s)

t = [20, 30, 40]
t.extend(s)
print(t)

r = s + t
print(r)

t.insert(3, 50)
print(t)