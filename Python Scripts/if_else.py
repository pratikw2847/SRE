service_status = input("Please enter service status: ")

if service_status == "started":
    print("Service is working")
elif service_status == "stopped":
    print("Service is stopping")
else:
    print("Service is does not exist")