from asyncio import subprocess
my_ips = {}
with open("access.log", "r") as log:
    for linea in log:
        ip = linea.strip().split(" ")[0] 
        if ip not in my_ips:
            my_ips[ip] = 1
        else:
            my_ips[ip] += 1

with open("banned_ips.log", "a") as log2:
    for ip, contador in my_ips.items():
        if contador > 40:
            log2.write(f"[SYSTEM] IP BANNED: Running iptables to block {ip}\n")
           