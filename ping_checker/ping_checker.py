import subprocess
import argparse
import logging
import csv
from datetime import datetime
from unittest import result
from urllib.parse import _ResultMixinStr
VERSION = "1.0.0"


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

def save_report(results):
    filename = "ping_report.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            ["Host", "Status", "Time"]
        )

        for result in results:
            writer.writerow(result)

def main():
    parser = argparse.ArgumentParser(
        description="Check host availability"
    )

    parser.add_argument(
        "--version",
    action="version",
    version=f"%(prog)s {VERSION}"
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

    host = []
    results = []

    if args.file:
        hosts = load_hosts(args.file)
    
    elif args.host:
        hosts.append(args.host)
    
    else:
        parser.print_help()
        return
    
    for host in hosts:
        save_report(results)

        if check_host(host):
            status = "ONLINE"
        else:
            status = "OFFLINE"

        print(f"{host} is {status}")

        results.append(
            [host,
             status,
             datetime.now()
             ]
    
        )


logging.basicConfig(
    filename="logs/ping_checker.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

if __name__ == "__main__":
    main()