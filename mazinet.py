#!/usr/bin/env python3

import requests as req
import subprocess
import socket
from ipaddress import ip_address
from datetime import datetime
import sys
from ipwhois import IPWhois

PIPE = subprocess.PIPE


def url_checker(host):
    a = host.split(":")
    if a[0] == ('http' or 'https'):
        print(host)
        return host
    # elif a[0] == host:
    #     new_url = "http://" + str(host)
    #     return new_url

    else:
        new_url = "http://" + str(host)
        print(new_url)
        return new_url


def ping(host):
    # This program is designed to be run on linux, for windows, "-c" would be turned to "-n"
    command = ['ping', '-c', '1', host]
    a = subprocess.call(command) == 0
    return a


def dnslookup(host):
    try:

        ip = ip_address(host)
        res = socket.gethostbyaddr(ip)
        return res

    except:

        res = socket.gethostbyname(host)
        return res


def resp_time(url):
    # Response time
    try:
        res = req.get(url=url, timeout=6)
        restime = res.elapsed.total_seconds()
        print("Response time is: ", restime, "\n")
        logfile.write("\nResponse time: \n")
        logfile.write(str(restime))

    except Exception as e:
        print("We face and error:  ", e)


def icmp_checker(indata):
    # Ping
    try:
        pingres = ping(indata)
        print("Ping response is: ", pingres)
        logfile.write("\nPing Response:(Returns True if ICMP works fine)\n")
        logfile.write(str(pingres))


    except Exception as e:
        print("We face and error:  ", e)


def dns_resolve(indata):
    # DNS lookup
    try:
        dnsres = dnslookup(indata)
        print("DNS Lookup result is: ", dnsres)
        logfile.write("\nDNS Lookup Result:\n")
        logfile.write(str(dnsres))
    except Exception as e:
        print("We face and error:  ", e)


def route(indata):
    # Trace Route
    try:
        print("\nTrace routing is processing... \n")
        tr_res = subprocess.run(['traceroute', indata], stdout=PIPE, universal_newlines=True, bufsize=1)
        output = str(tr_res).split('\\n')
        logfile.write("\nTrace Route:\n")

        for line in output:
            print(line)
            logfile.write(str("\n" + line))



    except Exception as e:
        print("We face and error:  ", e)


def who_is(indata):
    try:
        ip = ip_address(indata)
    except:
        ip = socket.gethostbyname(indata)
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap()
        print("\nWhois result for host ", indata, " is: \n", "Country: ", res['network']['country'])
        print("Provider: ", res['network']['name'], "\n IP range: " + res['network']['handle'])
        log = "\n Whois result for host " + indata + " is: \n" + "Country: " + res['network']['country'] + "\nProvider: "\
              + res['network']['name'] \
              + "\n IP range: " + res['network']['handle'] + "\n"
        logfile.write(log)
    except Exception as e:
        print("We face and error:  ", e)
    return ip


def who_are(indata):
    file_location = str(indata)
    file = open(file_location, "r")
    lines = file.readlines()
    for line in lines:
        ip_detail = who_is(line)
        print(ip_detail)


arg = sys.argv
indata = arg[(len(arg) - 1)]
url = url_checker(indata)

# Start Logfile
try:
    logfile = open("/var/log/mazinet.log", "a")
    logtime = datetime.now()
    log_header = "\n\n" + str(logtime) + "\n" + "Investigated Host: " + indata
    logfile.write(str(log_header))

except Exception as e:
    print("Error while creating log file: ", e)

if arg[1] == "all":
    resp_time(url)
    icmp_checker(indata)
    dns_resolve(indata)
    route(indata)
    who_is(indata)
    logfile.close()

elif arg[1] == "trace":
    route(indata)
    logfile.close()
elif arg[1] == "whois":
    who_is(indata)
    logfile.close()
elif arg[1] == "whoare":
    who_are(indata)
