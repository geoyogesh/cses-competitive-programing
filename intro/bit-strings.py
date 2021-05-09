from sys import stdin

magic_num=10**9 + 7 

def bit_strings(n):
    return (2**n) % magic_num

'''
if __name__ == "__main__":
    print(bit_strings(3)) # 8

'''
if __name__ == "__main__":
    n = int(input()) 
    print(bit_strings(n))
