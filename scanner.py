#Library for executing multiple instances of a function as once
#Does simultanious exection with threading
from concurrent.futures import ThreadPoolExecutor
#Allows connections between ports with TCP
import socket
#Library to check if user inputted ip address is a valid ip address
from ipaddress import ip_address
import time

def get_ip():
    ip = input("\nPlease enter ip address: ")
    try:
        ip_address(ip)
        return ip
    except ValueError:
        print("\nInvalid ip address")
        return get_ip()

if __name__ == "__main__":
    ip = get_ip()
    print(ip)

