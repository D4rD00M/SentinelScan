import socket
import sys
import threading

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}

# Function to scan for open ports
def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} ({common_ports.get(port, 'Unknown')}) is open")
    except Exception as e:
        print(f"Error occurred while scanning port {port}: {e}")
    finally:
        sock.close()

def scan(target):
    print("Scanning ports on target:", target)

    threads = []
    for port in common_ports.keys():
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# Main function
def main():
    # Names of creators
    main_creator = "Xer0Weeds"
    helping_creators = ["Z3nith", "kraven"]

    # Prompt user for target IP address or hostname
    target = input("Enter the target IP address or hostname: ")
    open_ports=scan(target)

    if open_ports:
        print("Potential vulnerabilities found. Checking CVE database.")
        for port in open_ports:
            if port == 80:
                print("Potential CVEs related to HTTP service (port 80):")
                print("CVE-2022-1234: Example vulnerability")
    else:
        print("No open ports found. Target appears to be secure.")

    # Stylishly display creator names
    print("\nScript created by:", main_creator)
    print("Assistance provided by:", ", ".join(helping_creators))

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()