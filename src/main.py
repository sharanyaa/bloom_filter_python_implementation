#!/usr/bin/env
import bloomFilter


class BloomFilterWrapper:
    def __init__(self):
        self.bloom_filter = bloomFilter.BloomFilter()

    def call_add_item(self):
        item = input('Add a word: ')
        self.bloom_filter.add_item(item)

    def call_remove_item(self):
        item = input('Remove a word: ')
        self.bloom_filter.remove_item(item)

    def call_maybe_contains(self):
        item = input('Query a word: ')
        self.bloom_filter.maybe_contains(item)

    def call_recreate_bit_array(self):
        self.bloom_filter.recreate_bit_array()


def main():

    wrapper = BloomFilterWrapper()
    menu = '\nSpell Checker Dictionar Options: \n 1. Add a word'\
        '\n 2. Remove a word \n 3. Query a word'\
        '\n 4. Recreate dictionary \n 5. File input '\
        '6. Exit \n Enter choice: '

    while True:
        choice = int(input(menu))
        if choice < 1 or choice > 5:
            break
        if choice == 1:
            wrapper.call_add_item(),
        elif choice == 2:
            wrapper.call_remove_item(),
        elif choice == 3:
            wrapper.call_maybe_contains(),
        elif choice == 4:
            wrapper.call_recreate_bit_array()
        elif choice == 5:
            path = input('\nEnter input file path: ')


if __name__ == '__main__':
    main()
