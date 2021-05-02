from sys import stdin

def missing_number(n, arr):
    total = (n * (n + 1)) // 2
    for item in arr:
        total -= item
    return total

'''
if __name__ == "__main__":
    print(missing_number(3, [1, 2])) # 3

'''
if __name__ == "__main__":
    n = int(input()) 
    arr = [int(x) for x in stdin.readline().split()] 
    print(missing_number(n, arr))
