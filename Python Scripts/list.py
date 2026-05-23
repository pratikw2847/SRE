users = ["Pratik", "Ramesh", "Wadekar"]
users.append("Pranav")
users.remove("Pratik")
users.insert(0, "Shiro")
del users[3]
users.sort()
users.reverse()
removed = users.pop()
print(removed)
print(len(users))
for user in users:
    print(user)



set = [1, 2,4, -1, 10, -2]
minimum = min(set)
maximum = max(set)
sum = sum(set)
print(sum)
print(minimum)
print(maximum)