from sys import stdin

def static_range_sum(n, arr, queries):
    prefix_sum = [0]*n

    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i] 
    
    '''
    result = []
    for s, e in queries:
        result.append(prefix_sum[e - 1] - prefix_sum[s - 1] + arr[s - 1])
    return result
    '''
    for s, e in queries:
        print(prefix_sum[e - 1] - prefix_sum[s - 1] + arr[s - 1], end = ' ')


'''
if __name__ == "__main__":
    static_range_sum(8, [3, 2, 4, 5, 1, 1, 5, 3], [(2, 4), (5, 6), (1, 8), (3, 3)]) # 11 2 24 4

'''
if __name__ == "__main__":
    [ n, q ] = [int(x) for x in stdin.readline().split()]
    arr = [int(x) for x in stdin.readline().split()] 
    queries = []
    for _ in range(q):
        [ start, end ] = [int(x) for x in stdin.readline().split()]
        queries.append((start, end))
    static_range_sum(n, arr, queries)
