from sys import stdin
import math

import sys
sys.setrecursionlimit(1000000000)

def distinct_coins_rec(arr, n, sum, i, mem):
    if sum == 0:
        return 1
    
    if sum < 0 or n == 0:
        return 0
    
    
    if (i, sum) in mem:
        return mem[(i, sum)]
    
    
    result = distinct_coins_rec(arr, n - 1, sum, i + 1, mem) + distinct_coins_rec(arr, n, sum - arr[i], i, mem)
    mem[(i, sum)] = result
    return result

def distinct_coins(arr, n, sum, mem):
    result = distinct_coins_rec(arr, n, sum, 0, mem)
    return result

'''
if __name__ == "__main__":
    print(distinct_coins([1, 5, 7], 3, 11, dict())) # 4
    print(distinct_coins([2, 3, 5], 3, 9, dict())) # 3

'''
if __name__ == "__main__":
    [ n, sum ] = [int(x) for x in stdin.readline().split()]
    arr = [int(x) for x in stdin.readline().split()] 
    print(distinct_coins(arr, n, sum, dict()))
