# Ambit

Fast, flexible, connection based port scanner written in Python.


```
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
```
