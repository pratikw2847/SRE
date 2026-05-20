print("Hello World")


name = input("What is your name? ")
age = input("How old are you? ")
org = input("What is your organization? ")
position = input("What is your position? ")

print(f"My name is {name} and I am {age} years old. I am working at {org} with position {position}")
print(name.lower() + " " + org.upper() + " " + position.title())
if age > 18:
    print("You are older than your age.")
else:
    print("You are not older than your age.")