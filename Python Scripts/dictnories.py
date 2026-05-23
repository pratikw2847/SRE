servers = {
    "ip": "10.128.1.11",
    "hostname": "production",
    "type": "web server",
    "cpu": 2
}
print(servers)
print(servers["type"])
print(servers.get("storage"))
servers["Ram"] = "32 GB"
print(servers)
del servers["hostname"]
print(servers)

if "USB" in servers:
    print(f"USB  exists {servers["USB"]}")
else:
    print(f"USB  not exists ")
servers["USB"] = "32 GB"
if "USB" in servers:
    print(f"USB  exists and storage is {servers["USB"]}")
else:
    print(f"USB  not exists ")



for specification,value in servers.items():
    if specification == "ip":
        print(f"{specification} has value {value}")
    else:
        print(f"{specification} not exists ")