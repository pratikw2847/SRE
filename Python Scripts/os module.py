import os

os.mkdir("test")
os.rmdir("test")

pwd = os.getcwd()
print(pwd)

data = (os.listdir(r"C:\Users\HP\Desktop\SRE_ROADMAP"))
for i in data:
    print(f"{i}")


path = r"C:\Users\HP\Desktop\SRE_ROADMAP"
print(os.path.exists(path))