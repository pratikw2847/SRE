'''
with open("Pratik.txt","w") as file:
    file.write("Pratik is aiming for SRE")
with open("Pratik.txt","a") as file:
    file.write("\nIn one year he will be in foreign")

'''

with open("Pratik.txt","r") as file:
    cont = file.readlines()
print(cont)

with open("Pratik.txt","r") as file:
    cont = file.read()
print(cont)
