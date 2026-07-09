import subprocess
import argparse


def check_host(host):
    result = subprocess.run(
        ["ping", host],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return True

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


if __name__ == "__main__":
    main()