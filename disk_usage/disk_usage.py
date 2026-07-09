import psutil


WARNING_THRESHOLD = 80


def format_size(bytes):
    return round(
        bytes / (1024**3),
        2
    )


def get_disk_usage():

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


        if usage.percent >= WARNING_THRESHOLD:
            print(
                "WARNING: Disk space is low!"
            )


        print("-" * 30)


if __name__ == "__main__":
    get_disk_usage()