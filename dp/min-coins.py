from sys import stdin
import math

import sys
sys.setrecursionlimit(1000000000)

def min_coins_rec(arr, n, sum, mem):
    if sum == 0:
        return 0
    
    if sum < 0:
        return math.inf
    
    if sum in mem:
        return mem[sum]
    
    result = math.inf
    for item in arr:
        result = min(result, 1 + min_coins_rec(arr, n, sum - item, mem))
    
    mem[sum] = result
    return result

def min_coins(arr, n, sum, mem):
    result = min_coins_rec(arr, n, sum, mem)
    if result == math.inf:
        return -1
    return result


if __name__ == "__main__":
    print(min_coins([1, 5, 7], 3, 11, dict())) # 3

'''
if __name__ == "__main__":
    [ n, sum ] = [int(x) for x in stdin.readline().split()]
    arr = [int(x) for x in stdin.readline().split()] 
    print(min_coins(arr, n, sum, dict()))
'''