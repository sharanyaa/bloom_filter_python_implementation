#!/usr/bin/env
import bitarray


class BloomFilter:

    def __init__(self):
        self.__num_items__ = 100000
        self.__num_hashes__ = 8
        self.__false_positive_rate__ = 0.001
        self.__hash_func__ = None
        self.__log2_num_bits = 31
        self.__bit_array__ = bitarray.bitarray()

    def add_item(self, item):
        print("adding")
        for k in range(self.__num_hashes__):
            # hashcode = get_hashcode(s, k)
            # bit_index = get_bit_index(hashcode, self.__log2_num_bits)
            pass
        self.__bit_array__.frombytes(b'a')
        print(self.__bit_array__)

    def remove_item(self, item):
        pass

    def maybe_contains(self, item):
        pass

    def recreate_bit_array(self):
        pass
