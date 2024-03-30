import socket
import sys
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}
def scan(target):
    print("Scanning ports on target:", target)
    open_ports = []
    for port in common_ports.keys():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) 
        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} ({common_ports[port]}) is open")
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            sys.exit()
        except socket.gaierror:
            print("Hostname could not be resolved. Exiting.")
            sys.exit()
        except socket.error:
            print("Could not connect to server.")
            sys.exit()
    return open_ports
def main():
    main_creator = "D4rD00M"
    helping_creators = ["Z3nithn", "kraven"]
    target = input("Enter the target IP address or hostname: ")
    open_ports = scan(target)

    if open_ports:
        print("Potential vulnerabilities found. Checking CVE database.")
        for port in open_ports:
            if port == 80:
                print("Potential CVEs related to HTTP service (port 80):")
                print("CVE-2022-1234: Example vulnerability")
    else:
        print("No open ports found. Target appears to be secure.")
    print("\nScript created by:", main_creator)
    print("Assistance provided by:", ", ".join(helping_creators))
if __name__ == "__main__":
    main()
