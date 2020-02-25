# What is this app:
**MaziNet** is an app which is supposed to make your network investigation jobs easier.

This app has some built-in tools that provides below tests on the host you enter:

- Measures Response time by sending a post request.
- Pings the host and returns `True` if host is reachable
- DNS-Lookup: returns DNS IP address of host if you enter a domain.  
- TraceRoute: traces the route from your device to the host to see where the packet losts or gets recieved.
- Whois: App runs a whois (Finds source details of an IP) on the IP you enter or a group of IPs in a file.
# How to use:
you need just to run installer bash script:
`./installer.sh`
or
`bash ./installer.sh`

**_Make sure you are in the directory of project while installation_**

After you installed the app, it makes a shortcut on `/usr/bin` directory which lets you use the app without specifying python extention or other commands you might need to run a python program.

# Commands:

**`sudo mazinet all <host>`** :

This command runs all the tests on the entered host.
for example:

mazinet all mendmind.ir (test with domain)

or

mazinet all 192.168.1.1 (test with IP)

**`sudo mazinet resp <host>`** :

This command only measures response time of the host.

**`sudo mazinet trace <host>`** :

This command only runs `traceroute` test on the entered host.

**`sudo mazinet whoare <filename>`** :

eg. sudo mazinet whoare /home/yourprettyhostname/filename

This command runs whois on a number of IP addresses which you have entered in a file (each IP in one line)

**`sudo mazinet whois <IP address>`** :

This command runs whois only on the entered host(if you enter a domain, it would try to get the IP but there might be some issues specially when the domain is behind clouds, firewalls or etc)

**Plus seeing the result of command in terminal, it also will be written down on a logfile in: `/var/log/mazinet.log`**

_this app is tested on ubuntu 18.04_
____

if you had any question, we can be in touch via:

[maziar.sh110@gmail.com](mailto:maziar.sh110@gmail.com)

[Linkedin](https://www.linkedin.com/in/maziar-shahsavanpour-a4210088/)

[Whatsapp](https://api.whatsapp.com/send?phone=+989156262067)
