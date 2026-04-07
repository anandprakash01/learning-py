security_clearance = 5
has_badge = True

if not has_badge:
    print("Access Denied: No badge.")
elif has_badge and security_clearance == 5:
    print("Access Granted: Welcome, Admin.")
elif has_badge and security_clearance < 5:
    print("Access Granted: Welcome, User.")
else:
    print("System Error.")


system_checks = 3

while system_checks > 0:
    print("Running check...")
    system_checks -= 1

for i in range(10, 51, 10):
    print(f"Loading core modules: {i}%")
print("Boot Complete.")


malicious_ip = "192.168.1.99"
traffic_log = ["10.0.0.1", "", "10.0.0.2", "192.168.1.99", "10.0.0.3"]

for ip in traffic_log:
    if ip == "":
        print("Blank IP dropped")
        continue
    if ip == malicious_ip:
        print("THREAT DETECTED. Locking down.")
        break
    print(f"Scanned: {ip}")
else:
    print("Scan complete. Network secure.")

http_status = 500
match http_status:
    case 200:
        print("Success: OK")
    case 401 | 403:
        print("Error: Authentication failed")
    case 404:
        print("Error: Not Found")
    case status if status >= 500:
        print("Error: Server Offline")
    case _:
        print("Unknown Status Code")


server_data = ["Database", "Active", [192, 168, 1, 50], ["admin", "root", "guest"]]

service, status, *details = server_data
print(details[1][1])


db = {"host": "10.0.0.1", "port": 5432}
db_user = db.get("user", "admin")

db = {**db, **{"status": "live", "port": 8000}}
old_host = db.pop("host")
print(db_user)
print(old_host)
print(db)
db.update({"status": "live", "port": 8000})


raw_logs = ["10.0.0.1", "192.168.1.5", "10.0.0.1", "10.0.0.2", "192.168.1.5"]

unique_logs = set(raw_logs)

banned_ips = {"10.0.0.2", "10.0.0.99"}

threats = []
print(type(threats))

# for log in unique_logs:
#     if log in banned_ips:
#         threats.append(log)

# The Intersection Operator (&) replaces the entire for-loop
threats = unique_logs & banned_ips

print(unique_logs)
print(threats)
