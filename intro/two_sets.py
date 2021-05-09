from sys import stdin


def two_sets(n):
    if n <=  1 or n % 2 == 0:
        print('NO')
    else:
        print('YES')
        print(n//2 + 1)
        for i in range(1, n, 2):
            print(i, end = ' ')
        print()
        print(n//2)
        for i in range(2, n + 1, 2):
            print(i, end = ' ')
        print()

if __name__ == "__main__":
    two_sets(7) # YES
    two_sets(4) # NO
    two_sets(3) # YES

'''
if __name__ == "__main__":
    n = int(input()) 
    two_sets(n)
'''