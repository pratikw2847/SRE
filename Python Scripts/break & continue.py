servers = [
    {"Server_type": "Production", "ip": "10.128.1.11"},
    {"Server_type": "QA", "ip": "10.128.1.12"},
    {"Server_type": "DEV", "ip": "10.128.1.13"},
    {"Server_type": "STG", "ip": "10.128.1.14"}
]

server_down = input("Which server is down? ")

for server in servers:
    if server["ip"] == server_down:
        print(f"The server is down having IP {server['ip']} belongs to {server['Server_type']}")
        break
else:
    print("Server IP not found")