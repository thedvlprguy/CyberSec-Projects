import nmap
scanner = nmap.PortScanner()
print(""" 


 ___  ________  ________  ___  ________      
|\  \|\   ____\|\   __  \|\  \|\   ____\     
\ \  \ \  \___|\ \  \|\  \ \  \ \  \___|_    
 \ \  \ \  \  __\ \   _  _\ \  \ \_____  \   
  \ \  \ \  \|\  \ \  \\  \\ \  \|____|\  \  
   \ \__\ \_______\ \__\\ _\\ \__\____\_\  \ 
    \|__|\|_______|\|__|\|__|\|__|\_________\
                                 \|_________|
                                             
                                             
 ___      ___  _____      ________           
|\  \    /  /|/ __  \    |\   __  \          
\ \  \  /  / /\/_|\  \   \ \  \|\  \         
 \ \  \/  / /\|/ \ \  \   \ \  \\\  \        
  \ \    / /      \ \  \ __\ \  \\\  \       
   \ \__/ /        \ \__\\__\ \_______\      
    \|__|/          \|__\|__|\|_______|      

 """)
print("Welcome, this is a simple Nmap Automation Tool")
print("<--------------------------------------------->")
ip_addr = input("Please Enter the IP You wanted to Scan: ")
print("The IP Address You Entered: ",ip_addr)
type(ip_addr)
resp = input("""\nPlease Enter the type of scan you want to run: 
                 1)SYN ACK Scan
                 2)UDP Scan
                 3)Comprehensive Scan \n""")
print("Your Selected Scan is: ", resp)
if resp == '1':
    print('Nmap Version', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024','-v -sS') # -sS -> Used for Syn Ack Scan
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print('Nmap Version', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024','-v -sU') # -sU -> Used for scanning UDP Scan
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())

elif resp == '3':
    print('Nmap Version', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024','-v -sS -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif resp >= 4:
    print("Please Enter a Valid Scan Option")




