
import sys
sys.setrecursionlimit(1000000000)

def remove_digits(num):
    if num == 0:
        return 0

    digit = 0
    current = num
    while current != 0:
        d = current % 10
        if d > digit:
            digit = d
        current //= 10

    return 1 + remove_digits(num - digit)

'''
if __name__ == "__main__":
    #print(remove_digits(27)) # 5 
    print(remove_digits(167)) # 29

'''
if __name__ == "__main__":
    num = int(input()) 
    print(remove_digits(num))
