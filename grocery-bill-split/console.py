#!/usr/bin/env python3
import sys
import traceback
from common import process_bill


def get_input_from_stdin():
    lines = []
    while True:
        line = input()
        if not len(line):
            # Break on empty line.
            break
        lines.append(line)
    return lines


def main():
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        with open(input_file_path) as input_file:
            lines = input_file.readlines()
    else:
        lines = get_input_from_stdin()
    try:
        entity_vs_amount = process_bill(lines)
        print(entity_vs_amount)
        total_amount = sum(entity_vs_amount.values())
        print("Total amount = {}".format(total_amount))
    except Exception:
        exception_traceback = traceback.format_exc()
        print("Error while processing input:\n\n---- start ----\n{}\n---- end ----\n\nwith the following exception trace:\n{}".format(
            lines, exception_traceback))


if __name__ == '__main__':
    main()
