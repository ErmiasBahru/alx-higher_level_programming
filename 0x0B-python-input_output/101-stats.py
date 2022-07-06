#!/usr/bin/python3

"""
Module that reads stdin line by line and computes metrics
"""

if __name__ == '__main__':

    import sys

    file_size = 0
    possible_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {i: 0 for i in possible_codes}
    counter = 0

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(file_size))
        for i, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(i, v))

    try:
        for line in sys.stdin:
            counter += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                file_size += int(data[-1])
            except BaseException:
                pass
            if counter % 10 == 0:
                print_stats(stats, file_size)
        print_stats(stats, file_size)
    except KeyboardInterrupt:
        print_stats(stats, file_size)
        raise
