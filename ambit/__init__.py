"""
Ambit is a simple tool which exposes open ports on network connected machines.

Usage:
    ambit [hosts:ports] 

Syntax:
    Ambit uses a cool format for specifying targets. Here's some examples.

    

    Check one host for one port.

    ambit 192.168.1.1:22                       

        

    Check two host for two ports, using commas.

    ambit 192.168.1.1,192.168.1.2:22,80

     
    
    Check a range of hosts for a range of ports.

    ambit 192.168.1.1-192.168.1.100:100-300

    

    You can combine any of these formats.

    ambit 192.168.1.1,192.168.1.5-192.168.1.200:20-23,80,8000,8080,500-1000



    You can also have multiple groups.

    ambit 192.168.1.1-192.168.1.2:9100,515,80 96.60.22.10:80,443,20-23
"""
 

from socket import *
from sys import argv



def addresses(start, end):
    addresses = []
    address = start
    
    while (address != end):
        addresses.append(address)
        
        octets = [int(octet) for octet in address.split('.')]
        octets[-1] += 1
        
        for index in range(3, 1, -1):
            if (octets[index] > 255):
                octets[index] = 0
                octets[index - 1] += 1
             
        octets = [str(octet) for octet in octets]
        address = '.'.join(octets)

    return addresses



def hosts(segments):
    segments = segments.split(',')
    hosts = []

    for segment in segments:
        if ('-' in segment):
            scope = segment.split('-')
            start = scope[0]
            end = scope[1]
            hosts += addresses(start, end)

        else:
            hosts.append(segment)

    return hosts


                
def ports(segments):
    segments = segments.split(',')
    ports = []

    for segment in segments:
        if ('-' in segment):
            scope = segment.split('-')
            start = int(scope[0])
            end = int(scope[1])
            ports += range(start, end)

        else:
            ports.append(int(segment))

    return ports



def check(host, port):
    _socket = socket()
    _socket.settimeout(0.1)

    try:
        _socket.connect((host, port))
        return True

    except:
        return False



def examine(hosts, ports):
    for host in hosts:
        print('\n[+] Checking ports on %s' % host)

        for port in ports:
            open = check(host, port)

            if (open):
                print('[+] %s, open' % port)

#	    else:
#               print('[-] %s, closed' % port)

                 

def main():
    if (len(argv) == 2):
        targets = argv[1].split(':')

        _hosts = hosts(targets[0])
        _ports = ports(targets[1])
        
        print('\n[+] Starting examination')

        examine(_hosts, _ports)
        
    else:
        print(__doc__)

        
if __name__ == '__main__':
  main()
