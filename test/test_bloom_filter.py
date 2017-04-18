import random
from hashlib import sha512, sha384, sha256, sha1, md5
from pylab import plot, show, xlabel, ylabel
import sys
sys.path.insert(0, '/home/sharanya/Documents/'
                'bloom_filter_python_implementation/')


def generate_rand_data(n, chars):
    """generates random strings using the characters in chars """
    return ''.join(random.choice(chars) for i in range(n))


def test_bloom_filter(n, hash_func, k=None):
    """ returns the percentage of false positives """
    print(n, k)
    bloom = BloomFilter(capacity=n, hashes=k, )
    rand_keys = [generate_rand_data(10, 'abcde') for i in range(n)]
    # pushing the items into the data structure
    for rk in rand_keys:
        bloom.add_item(rk)
    # adding other elements to the dataset
    rand_keys = rand_keys + [generate_rand_data(10, 'fghil') for i in range(n)]
    # performing a query for each element of the dataset
    false_positive = 0
    for rk in rand_keys:
        if not bloom.maybe_contains(rk):
            false_positive += 1
    return float(false_positive)/n*100.0

if __name__ == '__main__':
    ''' testing the filter '''
    hash_functions = [sha512, sha384, sha256, sha1, md5]
    hash_func_names = ['sha512', 'sha384', 'sha256', 'sha1', 'md5']
    err_rates = [test_bloom_filter(n=10000, hash_func=hash_fn)
                 for hash_fn in hash_functions]
    print(hash_func_names, "\n", err_rates)

