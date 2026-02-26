import numpy as np

def FizzBuzz(start, finish):

    nums = np.arange(start, finish + 1)
    v = np.array(nums, dtype=object)

    v[nums % 3 == 0] = 'fizz'
    v[nums % 5 == 0] = 'buzz'
    v[(nums % 3 == 0) & (nums % 5 == 0)] = 'fizzbuzz'
    
    return(v)
