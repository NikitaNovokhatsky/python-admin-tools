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


def main():
    parser = argparse.ArgumentParser(
        description="Check host availability"
    )

    parser.add_argument(
        "host",
        help="IP address or domain name"
    )

    args = parser.parse_args()

    if check_host(args.host):
        print(f"{args.host} is ONLINE")
    else:
        print(f"{args.host} is OFFLINE")

logging.basicConfig(
    filename="logs/ping_checker.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

if __name__ == "__main__":
    main()