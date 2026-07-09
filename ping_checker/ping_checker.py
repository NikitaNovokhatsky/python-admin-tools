import subprocess
import argparse
import logging


def check_host(host):
    result = subprocess.run(
        ["ping", host],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        logging.info(f"{host} is ONLINE")
        return True
    
    logging.error(f"{host} is OFFLINE")
    return False

def load_hosts(filename):
    with open(filename, "r") as file:
        return [
            line.strip()
            for line in file
            if line.strip()
        ]

def main():
    parser = argparse.ArgumentParser(
        description="Check host availability"
    )

    parser.add_argument(
        "host",
        nargs="?",
        help="IP address or domain name"
    )

    parser.add_argument(
        "-f",
        "--file",
        help="File with list of hosts"
    )

    args = parser.parse_args()

    hosts = []

    if args.file:
        hosts = load_hosts(args.file)
    
    elif args.host:
        hosts.append(args.host)
    
    else:
        parser.print_help()
        return
    
    for host in hosts:

        if check_host(host):
            print(f"{hosts} is ONLINE")
        else:
            print(f"{host} is OFFLINE")


logging.basicConfig(
    filename="logs/ping_checker.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

if __name__ == "__main__":
    main()