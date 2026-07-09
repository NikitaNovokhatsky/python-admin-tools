import psutil
import argparse



def format_size(bytes):
    return round(
        bytes / (1024**3),
        2
    )

def main():

    parser = argparse.ArgumentParser(
        description="Disk usage monitoring tool"
    )

    parser.add_argument(
        "--threshold",
        type=int,
        default=80,
        help="Warning threshold percentage"
    )

    args = parser.parse_args()

    get_disk_usage(args.threshold)
    
def get_disk_usage(threshold):


    partitions = psutil.disk_partitions()

    for partition in partitions:

        usage = psutil.disk_usage(
            partition.mountpoint
        )

        print(
            f"Disk: {partition.device}"
        )

        print(
            f"Total: {format_size(usage.total)} GB"
        )

        print(
            f"Used: {format_size(usage.used)} GB"
        )

        print(
            f"Free: {format_size(usage.free)} GB"
        )

        print(
            f"Usage: {usage.percent}%"
        )


        if usage.percent >= threshold:
            print(
                "WARNING: Disk space is low!"
            )


        print("-" * 30)


if __name__ == "__main__":
    main()