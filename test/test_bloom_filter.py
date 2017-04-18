import random
from hashlib import sha512, sha384, sha256, sha1, md5
from pylab import plot, show, xlabel, ylabel
import sys
sys.path.insert(0, '../../'
                'bloom_filter_python_implementation/')
from src.bloomFilter import BloomFilter


def generate_rand_data(n, chars):
    """generates random strings using the characters in chars """
    return ''.join(random.choice(chars) for i in range(n))


def test_bloom_filter(n, hash_func, p=0):
    """ returns the percentage of false positives """
    bloom = BloomFilter(capacity=n, hash_func=hash_func, error_rate=p)
    rand_data = [generate_rand_data(10, 'abcde') for i in range(n)]
    for rd in rand_data:
        bloom.add_item(rd)
    # adding other elements to the dataset
    rand_data = rand_data + [generate_rand_data(10, 'fghij')
                             for i in range(n)]
    # performing a query for each element of the dataset
    false_positive = 0
    for rd in rand_data:
        if not bloom.maybe_contains(rd):
            false_positive += 1
    return float(false_positive)/n*100.0

if __name__ == '__main__':
    ''' testing the filter '''
    hash_functions = [sha512, sha384, sha256, sha1, md5]
    hash_func_names = ['sha512', 'sha384', 'sha256', 'sha1', 'md5']
    err_rates = [test_bloom_filter(n=100000, hash_func=hash_fn)
                 for hash_fn in hash_functions]
    print(hash_func_names, "\n", err_rates)
    p_values = [0.0000001, 0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1]
    for p in p_values:
        err_rates = [test_bloom_filter(n=100000, hash_func=hash_fn, p=p)
                     for hash_fn in hash_functions]
        print(p, hash_func_names, "\n", err_rates)

