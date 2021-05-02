
def weird_algorithm(num):
    while num != 1:
        print(num, end=' ')
        if num % 2 == 0:
            num = num // 2
        else:
            num = (num * 3) + 1
    
    print(num, end=' ')



'''
if __name__ == "__main__":
    #weird_algorithm(1)
    #weird_algorithm(2)
    weird_algorithm(3)

'''
if __name__ == "__main__":
    num = int(input()) 
    weird_algorithm(num)
