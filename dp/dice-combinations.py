import sys
sys.setrecursionlimit(1000000000)

'''
def dice_combinations(sum, mem):
    if sum == 0:
        return 1
    if sum < 0:
        return 0
    
    if sum in mem:
        return mem[sum]

    mod=10**9 + 7 

    result = 0
    for i in range(1, 7):
        result += dice_combinations(sum - i, mem)
    
    result = result % mod

    mem[sum] = result 
    
    return result 

'''

magic_num=10**9 + 7 

def dice_combinations(sum, mem):
    mem = [0] * (sum + 1)
    mem[0] = 1
    mem[1] = 1

    for i in range(2, sum + 1):
        #print(i)
        current_sum = 0
        for j in range(1, 7):
            current_sum += mem[i - j] if i - j >= 0 else 0
        mem[i] = current_sum % magic_num
    
    result = mem[sum] % magic_num

    mem[sum] = result 
    
    return result 


def main():
    print(dice_combinations(3, dict())) # 4
    #print(dice_combinations(50, dict())) # 660641036
    #print(dice_combinations(654321, dict())) # 615247550
    #print(dice_combinations(999998, dict())) # 39372206
    print('completed')



if __name__  == '__main__':
    main()
'''

if __name__ == "__main__":
    sum = int(input()) 
    print(dice_combinations(sum, dict()))
'''