
disk_total = int(input("Enter Total disk space in GB: "))
disk_free = int(input("Enter free disk space in GB: "))


def disk_free_GB(total,free):
    disk_free = total - free
    return disk_free
disk_free_GB(disk_total,disk_free)
print(disk_free_GB(disk_total,disk_free))



user_number = int(input("Enter user number: "))
people = []
def my_info(name,age,org):
    return(f"{name} is {age} years old and working in org {org}")

for i in range(1, user_number+1):
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    org = input("Enter your organization: ")

    people.append(my_info(name,age,org))

for person in people:
    print(person)


