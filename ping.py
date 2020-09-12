import subprocess
import platform
import json

def ping_ip(current_ip_address):
        try:
            output = subprocess.check_output("ping -{} 1 -w 100 {}".format('n' if platform.system().lower(
            ) == "windows" else 'c', current_ip_address ), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
                return False

ns = -1
finishl = 255

up = []

ip1 = "1"

ip0 = "192.168.1."
ip0in = input("Pon que ip quieres escanear en un rango de 255 ips.\n En la típica de casa 192.168.1.X debería de estar como (192.168.1.) sin paréntesis y con punto al final: ")
if ip0in != "":
    ip0 = ip0in
    
hostname = ip0+ip1
while ip1 != finishl:
    ns = ns + 1
    ip1 = str(ns)
    hostname = ip0+ip1
    if ns == 256:
        print("Ow mama I've finished")
        print(up)
        with open('upips.txt', 'w') as f:
            for item in up:
                f.write("%s\n" % item)
        exit()
    elif ping_ip(hostname):
        print(f"{hostname} is available")
        up.append(hostname)
    else:
        print(f"{hostname} is not available")
exit()
