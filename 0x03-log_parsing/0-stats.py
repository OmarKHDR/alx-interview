#!/usr/bin/python3
"""This script is doing things"""
import signal
import time
import sys
import re
"""script that reads stdin line by line and computes metrics:"""


def get_status_code(line, status):
    """This script is doing things"""
    find_code = re.search("\s\d{3}\s", line)
    if find_code:
        status_code = find_code.group().strip()
        if status_code in status:
            status[status_code] = status[status_code] + 1
        else:
            status[status_code] = 1


status = {}
acc_size = 0
count = 1
while True:
    try:
        count %= 10
        line = input()
        get_status_code(line, status)

        size = re.search("\d*$", line)
        if size:
            acc_size += int(size.group().strip())

        if count == 0:
            print("File size:", acc_size)
            for key, val in status.items():
                print(f"{int(key)}: {val}")
        count += 1
    except KeyboardInterrupt:
        print("File size:", acc_size)
        for key, val in status.items():
            print(f"{int(key)}: {val}")
        raise KeyboardInterrupt
