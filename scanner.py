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
        #Checks the users input to see if it is a valid ip address
        ip_address(ip)
        return ip
    except ValueError:
        print("\nInvalid ip address")
        #Recursive method that calls the function again if the given ip address isn't valid
        return get_ip()

def get_port_range():
    #Get max and min values for ports to be scanned, ensures the entered values are integers
    try:
        min_port = int(input("\nPlease enter lowest port number to be scanned: "))
        max_port = int(input("Please enter highest port number to be scanned: "))
    except:
        print("\nEnter value isn't a number.")
        return get_port_range()

    if min_port > max_port:
        print("\nInvalid range, minimum port value is greater than the maximum port number.")
        return get_port_range()
    elif min_port < 0 or max_port > 65535:
        print("\nGiven values are not in the normal port range.")
        return get_port_range()

    return [min_port, max_port]

def calculate_max_threads(port_range):
    length = port_range[1] - port_range[0]
        
    if length < 1000:
        return int(((length/100) * 10) + 1)
        
    return 100


if __name__ == "__main__":
    ip = get_ip()
    port_range = get_port_range()
    max_threads = calculate_max_threads(port_range)
    print(ip)
    print(port_range)
    print(max_threads)
