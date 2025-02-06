WARNING!!!!
DO NOT USE TO SCAN PUBLIC IP ADDRESSES!
Using this to scan ports of public ip addresses can be considered a cyberattack, and can lead to legal action being taken.

This is a educational tool only to be used on your personal LAN using private ip addresses.

This script ues the python sockets library to try and connect to ports using a TCP three-way handshake. If a port doesn't achknowledge the TCP
request, the port is closed and the script ignores it. If a connection is made, the port is open, and a message warning the user is shown.
If necessary, the port can be closed by updating your firewall settings.

This script uses Thread Pool Executor to run the scan function in multiple threads, allowing large chunks of hundreds of ports to be scanned
asynchronically, drastically decreasing the time to scan thousands of ports.
