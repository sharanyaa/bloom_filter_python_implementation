#!/usr/bin/env
import bitarray
from math import ceil, log
from hashlib import sha256
# import mmh3 # broken, doesn't seem to work


class BloomFilter:

    def __init__(self, capacity=100000, error_rate=0.001):
        self.__num_items__ = capacity
        self.__false_positive_rate__ = error_rate
        # self.__hash_func__ = None
        # self.__log2_num_bits__ = 31
        self.__num_bits__ = ceil(
            (self.__num_items__ * log(self.__false_positive_rate__)) /
            log(1.0 / (pow(2.0, log(2.0)))))
        self.__num_hashes__ = round(
            log(2.0) * self.__num_bits__ /
            self.__num_items__)
        self.__bit_array__ = bitarray.bitarray(self.__num_bits__)
        print(self.__num_bits__, self.__num_hashes__,
              self.__bit_array__.__sizeof__())
        self.__bit_array__.setall(0)

    def add_item(self, item):
        for n in range(self.__num_hashes__):
            bit_index = self.__get_hashed_index__(
                            item, n, self.__num_bits__)
            print(n, bit_index)
        self.__bit_array__[bit_index] = 1

    def remove_item(self, item):
        pass

    def maybe_contains(self, item):
        for n in range(self.__num_hashes__):
            bit_index = self.__get_hashed_index__(
                            item, n, self.__num_bits__)
            print(n, bit_index)
            if self.__bit_array__[index] != 1:
                return False
        return True

    def recreate_bit_array(self):
        pass

    def __get_hashed_index__(self, item, n, filter_size):
        digest = sha256(item.encode('utf-8')).hexdigest()
        hashA = digest[0:len(digest)//2]
        hashB = digest[len(digest)//2:]
        hc = int((hashA + n*hashB), 16)
        return hc % filter_size
