#!/usr/bin/env
import sys
import os
import bloomFilter


class BloomFilterWrapper:
    def __init__(self):
        self.bloom_filter = bloomFilter.BloomFilter()

    def call_add_item(self, item=None):
        if not item:
            item = input(' Add a word: ')
        self.bloom_filter.add_item(item)

    def call_maybe_contains(self):
        item = input(' Query a word: ')
        if self.bloom_filter.maybe_contains(item):
            print("Maybe in dictionary.")
        else:
            print("Definitely not in dictionary")

    def call_recreate_bit_array(self):
        self.bloom_filter.recreate_bit_array()


def main():

    def read_file(path):
        if os.path.exists(path):
            print(" Reading input...")
            with open(path) as input_file:
                for line in input_file:
                        wrapper.call_add_item(line.strip())
            print(" File input read and added to filter.")
        else:
            print(" Invalid file path.")

    wrapper = BloomFilterWrapper()
    menu = '\nSpell Checker Dictionary Options:\n 1. Add a word'\
        '\n 2. Query a word \n 3. Recreate dictionary'\
        '\n 4. Read an input file '\
        '\n Any other key - Exit \n Enter choice: '

    if len(sys.argv) == 2:
        path = sys.argv[1]
        read_file(path)

    while True:
        choice = input(menu)
        if choice == "1":
            wrapper.call_add_item(),
        elif choice == "2":
            wrapper.call_maybe_contains(),
        elif choice == "3":
            wrapper.call_recreate_bit_array()
        elif choice == "4":
            path = input(' Enter input file path: ')
            read_file(path)
        else:
            break

if __name__ == '__main__':
    main()
