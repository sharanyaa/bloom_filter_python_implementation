#!/usr/bin/env
import sys
from math import ceil, log
from hashlib import sha512, sha384, sha256, sha1, md5
import bitarray
# import mmh3 # broken, doesn't seem to work


class BloomFilter:

    def __init__(self, capacity=100000, error_rate=0.001,
                 hashes=None, hash_func=sha256):
        '''initalize the filter, check validity of arguments'''
        if capacity < 1 or capacity > sys.maxsize:
            capacity = 100000
        self.__num_items__ = capacity

        if error_rate <= 0 or error_rate >= 1.0:
            error_rate = 0.001
        self.__false_positive_rate__ = error_rate

        self.__num_bits__ = ceil(
            (self.__num_items__ * log(self.__false_positive_rate__)) /
            log(1.0 / (pow(2.0, log(2.0)))))

        if isinstance(hashes, int):
            self.__num_hashes__ = hashes
        else:
            self.__num_hashes__ = round(
                log(2.0) * self.__num_bits__ /
                self.__num_items__)

        self.__hash_func__ = hash_func
        # print(self.__hash_func__)

        self.__bit_array__ = bitarray.bitarray(self.__num_bits__)
        # print(self.__num_bits__, self.__num_hashes__,
        #      self.__bit_array__.__sizeof__())
        self.__bit_array__.setall(0)
        print(self.__num_items__,
              self.__false_positive_rate__,
              self.__num_hashes__,
              self.__hash_func__)

    def add_item(self, item):
        '''add an item to filter'''
        for n in range(self.__num_hashes__):
            bit_index = self.__get_hashed_index__(
                            item, n, self.__num_bits__)
            self.__bit_array__[bit_index] = 1

    def maybe_contains(self, item):
        '''test membership of item'''
        for n in range(self.__num_hashes__):
            bit_index = self.__get_hashed_index__(
                            item, n, self.__num_bits__)
            if not self.__bit_array__[bit_index]:
                return False
        return True

    def __get_hashed_index__(self, item, n, filter_size):
        '''hash function for filter'''
        digest = self. __hash_func__(item.encode('utf-8')).hexdigest()
        hashA = digest[0:len(digest)//2]
        hashB = digest[len(digest)//2:]
        hc = int(hashA, 16) + n*int(hashB, 16)
        return hc % filter_size
