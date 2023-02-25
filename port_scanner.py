import socket 
from IPy import IP

def check_ip(ip):
    try:
        # IP validation
        IP(ip)
        return ip
    
    except:
        # if domain, get an IP
        return socket.gethostbyname(ip)
    
    
def scan_port(ip, port):
    try:
        # scan the ports
        sock = socket.socket()
        sock.settimeout(0.2)
        sock.connect((ip, port))
        print("PORT " + str(port) + " IS OPEN")
        
    except:
        pass
        
    
    
domain = input("Enter target(s) to scan: (separate targets with `n`)")
#check if there are multiple targets
ips = []
TARGETS = []
if "," in domain:
    
    for target in domain.split(','): 
        TARGETS.append(target.strip())
        ip = check_ip(target.strip())
        ips.append(ip)

    for i, ip in enumerate(ips):  
        print(TARGETS[i])
        for i in range(1, 100):
            scan_port(ip, i)
            
            
else:
    
    ip = check_ip(domain)

    for i in range(1, 100):
        scan_port(ip, i)
    
    
