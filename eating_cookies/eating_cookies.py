#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  # check for values in cache
  if not cache: 
    cache = {}
  # can't have negative cookies, that's depressing
  if n < 0:
    return 0
  # there's only 1 way to eat 0 cookies, you can't
  elif n == 0:
    return 1
  # if there are values in the cache, use those
  elif cache and cache[n] > 0:
    return cache[n]
  # if not, add them to the cache
  else:
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')