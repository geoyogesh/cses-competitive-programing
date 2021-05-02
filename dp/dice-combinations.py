import sys
sys.setrecursionlimit(1000000000)


def dice_combinations(sum, mem):
    if sum == 0:
        return 1
    if sum < 0:
        return 0
    
    if sum in mem:
        return mem[sum]

    mod=10**9 + 7 

    result = 0
    for i in range(6, 0, -1):
        result += dice_combinations(sum - i, mem)
    
    result = result % mod

    mem[sum] = result 
    
    return result 


def main():
    print(dice_combinations(3, dict())) # 4
    print(dice_combinations(50, dict())) # 660641036
    #print(dice_combinations(999998, dict()))
    print('completed')



if __name__  == '__main__':
    main()
'''

if __name__ == "__main__":
    sum = int(input()) 
    print(dice_combinations(sum, dict()))
'''