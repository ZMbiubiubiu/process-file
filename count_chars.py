# count_chars.py
# Created: 4 24 2019
# meta
__author__ = 'ZzLee'
__version__ = '1.0'
"""
Get the number of each character in any given text.
"""

"""
What I have learned from this script?
-collections.Counter
class Counter(builtins.dict)
 |  Dict subclass for counting hashable items.  Sometimes called a bag
 |  or multiset.  Elements are stored as dictionary keys and their counts
 |  are stored as dictionary values.
 |  
 |  >>> c = Counter('abcdeabcdabcaba')  # count elements from a string
 |  
 |  >>> c.most_common(3)                # three most common elements
 |  [('a', 5), ('b', 4), ('c', 3)]
"""

import pprint
import argparse
import collections

usage = "python count_chars.py -file [FILE]"
description = "print the number of each character in this given text"
parser = argparse.ArgumentParser(usage=usage, description=description)
parser.add_argument('-file', required=True, type=str, help='(REQUIRED)')
args = parser.parse_args()

file = args.file

def main():
    try:
        with open(file, 'r') as info:
            count = collections.Counter(info.read().upper())
    except FileNotFoundError:
        print("This a valid file name.")
        exit(1)

    value = pprint.pformat(count)
    print(value)


if __name__ == "__main__":
    main()