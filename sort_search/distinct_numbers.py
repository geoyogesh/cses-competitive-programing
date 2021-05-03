from sys import stdin


def distinct_numbers(arr):
    return len(set(arr))

'''
if __name__ == "__main__":
    print(distinct_numbers([1, 1]))
    print(distinct_numbers([1, 1]))
    print(distinct_numbers([1, 1, 2]))
    print(distinct_numbers([1, 1, 2, 3, 6]))

'''
if __name__ == "__main__":
    n = int(input()) 
    arr = [int(x) for x in stdin.readline().split()]
    print(distinct_numbers(arr))

