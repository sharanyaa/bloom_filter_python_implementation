import random
from pylab import plot, show, xlabel, ylabel
import sys
sys.path.insert(0, '/home/sharanya/Documents/'
                'bloom_filter_python_implementation/')
from src.bloomFilter import BloomFilter


def rand_data(n, chars):
    """generate random strings using the characters in chars """
    return ''.join(random.choice(chars) for i in range(n))


def bloomTest(n, k=None):
    """ return the percentage of false positive """
    print(n, k)
    bloom = BloomFilter(capacity=n, hashes=k)
    # generating a random data
    rand_keys = [rand_data(10, 'abcde') for i in range(n)]
    # pushing the items into the data structure
    for rk in rand_keys:
        bloom.add_item(rk)
    # adding other elements to the dataset
    rand_keys = rand_keys + [rand_data(10, 'fghil') for i in range(n)]
    # performing a query for each element of the dataset
    false_positive = 0
    for rk in rand_keys:
        if not bloom.maybe_contains(rk):
            false_positive += 1
    return float(false_positive)/n*100.0

if __name__ == '__main__':
    # testing the filter
    def get_err_rates(start, end, factor):
        res = []
        while start <= end:
            res.append(start)
            start *= factor
        return res
    n = 10000
    k = range(1, 64)
    perc = [bloomTest(n=n, k=kk) for kk in k] # k is varying
    rates = get_err_rates(0.0000001, 1, 10)
    # perc = [bloomTest(n, p) for p in rates]
    print(rates,"\n",  perc)
    # plotting the result of the test

    plot(k, perc, '--ob', alpha=.7)
    ylabel('false positive %')
    xlabel('k')
    show()
