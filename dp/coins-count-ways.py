from sys import stdin

import sys
sys.setrecursionlimit(1000000000)

magic_num=10**9 + 7 

def count_ways_rec(arr, n, sum, mem):
    if sum == 0:
        return 1
    
    if sum < 0:
        return 0
    
    if sum in mem:
        return mem[sum]
    
    result = 0
    for item in arr:
        result += count_ways_rec(arr, n, sum - item, mem)
    
    mem[sum] = result
    return result

def count_ways(arr, n, sum):
    arr.sort(reverse=True)
    return count_ways_rec(arr, n, sum, dict()) % magic_num

'''
if __name__ == "__main__":
    #print(count_ways([2, 3, 5], 3, 9, dict())) # 8
    print(count_ways([1], 1, 1000000)) # 8

'''
if __name__ == "__main__":
    [ n, sum ] = [int(x) for x in stdin.readline().split()]
    arr = [int(x) for x in stdin.readline().split()] 
    print(count_ways(arr, n, sum))
