import socket 
from IPy import IP

def scan(target, p1, p2=None):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning Target] ' + str(target))
    if p2 == None:
        scan_port(converted_ip, p1)
    else: 
        for port in range(int(p1), int(p2+1)):
            scan_port(converted_ip, port)
    

def check_ip(ip):
    try:
        # IP validation
        IP(ip)
        return ip
    
    except:
        # if domain, get an IP
        return socket.gethostbyname(ip)
    
def get_banner(s):
    return s.recv(1024)

    
def scan_port(ip, port):
    try:
        # scan the ports
        sock = socket.socket()
        sock.settimeout(0.2)
        sock.connect((ip, port))
        try: 
            banner = get_banner(sock)
            print("PORT "+str(port) + " IS OPEN : " + str(banner.decode().strip('\n')))
        except:
            print("PORT " + str(port) + " IS OPEN")
            
    except:
        print("PORT " + str(port) + " IS CLOSED")        
        pass
        
    
    
    
    
if __name__ == "__main__":    
    
    target = input("Enter target(s) to scan: (separate targets with `,`)")
    
    range_check = "check"
    
    while range_check not in "s" and range_check not in "r":
        range_check = input("Do you want to scan a single port or a range of ports? (s / r)").lower()
    
    if range_check == "s":
        port1 = int(input("Enter the port you want to be scanned."))
    
    else:
        port1 = int(input("Enter the first port of the range you want to be scanned."))
        port2 = int(input("Enter the last port of the range you want to be scanned."))
        
    
    # check if there are multiple targets
    if "," in target:
    
        if range_check == "s":    
            for ip in target.split(','): 
                scan(ip.strip(), port1)
        
            
        elif range_check == "r":    
            for ip in target.split(','): 
                scan(ip.strip(), port1, port2)        
                
    else:
        
        if range_check == "s":
            scan(target, port1)
            
        elif range_check == "r":
            scan(target, port1, port2)
    
        
