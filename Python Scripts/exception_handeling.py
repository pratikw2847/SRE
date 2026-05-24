def deployment_status(server):
    try:
        ip = server["ip"]
        host = server["host"]
        port = server["port"]

        if not ip or not host:
            raise KeyError("IP or Host missing")

        if deployment == "Deployed":


            print(f"Deployment is success on server {ip}:{port} which is  {host} enviroment because deployment status is {deployment}")
        else:
            print("Deployment is failed as status is not deployed")
    except KeyError as e:
        print(f"Deployment failed because {e} not found")


n = int(input("Enter number of servers: "))

for i in range(1, n + 1):

    ip = input("Enter your ip: ")
    host = input("Enter your host: ")
    port = int(input("Enter your port: "))
    deployment = input("Enter deployment status: ")

    server = {
        "ip": ip,
        "host": host,
        "port": port,
        "deployment": deployment
    }

    deployment_status(server)