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
        return int((((length) / 100) * 10) + 1)
        
    return 100

def generate_port_chunks(port_range, max_threads):
    port_chunks = []
    # Get the average chunk size (excluding the remainder)
    chunk_size = (int(port_range[1]) - int(port_range[0])) // max_threads
    
    start = int(port_range[0])

    for i in range(max_threads):
        # The first (max_threads - 1) chunks will get the chunk_size
        if i < max_threads - 1:
            end = start + chunk_size
        else:
            # The last chunk will take the remaining ports
            end = int(port_range[1])

        port_chunks.append([start, end])

        # Move the start to the next port after the current chunk
        start = end + 1

    return port_chunks

def scan(ip, port_chunk):
    print(f"\nScanning {ip} from port {port_chunk[0]} to port {port_chunk[1]}.")
    #Loop through the minto the max ports
    for port in range(port_chunk[0], port_chunk[1]):
        #Attemps a TCP connection with the port
        try:
            scan_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scan_socket.timeout(1)

            scan_socket.connect(ip, port)
            print(f"[!] {port} is open!")
        except:
            none


def main():
    #Get an ip from the user that will be scanned
    ip_address = get_ip()
    #Get range of ports to be scanned for this ip address
    port_range = get_port_range()
    #Generates a certain number of threads based on the range of ports give
    max_threads = calculate_max_threads(port_range)
    #Uses the number of max threads to divide the range of ports into roughly equal chunks
    port_chunks = generate_port_chunks(port_range, max_threads)

    #Starts timer to time how long it takes to scan all ports
    start_time = time.time()

    #Calls the scan scan function
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(scan, [ip_address] * len(port_chunks), port_chunks)

    end_time = time.time()
    print(f"Scanned {port_range[1] - port_range[0]} ports in {end_time - start_time} seconds.")

if __name__ == "__main__":
    main()
