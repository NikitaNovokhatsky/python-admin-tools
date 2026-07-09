import subprocess


host = input("Enter host: ")

result = subprocess.run(
    ["ping", host],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print(f"{host} is ONLINE")
else:
    print(f"{host} is OFFLINE")