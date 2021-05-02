def dice_combinations(sum, mem):
    if sum == 0:
        return 1
    if sum < 0:
        return 0
    
    if sum in mem:
        return mem[sum] 

    result = 0
    for i in range(1, 7):
        result += dice_combinations(sum - i, mem)
    
    mem[sum] = result
    
    return result 


def main():
    print(dice_combinations(3, dict()))

if __name__  == '__main__':
    main()