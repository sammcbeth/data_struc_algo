import sys
from time import perf_counter
# sys.setrecursionlimit(10000)

def fibonacci(num, memo={}):
    # print(f'processing {num}')
    
    if num in memo:
        return memo[num]

    elif num == 2 or num == 1:
        return 1
    else:
        result = fibonacci(num-1, memo) + fibonacci(num-2, memo)
        memo[num] = result
        return result 

def fibonacci_iter(num):
    if num <= 2:
        return 1
    fibnums = {0:0,1:1,2:1}
    for i in range(3,num+1):
        fibnums[i] = fibnums[i-1] + fibnums[i-2]
    return fibnums[num]


# print(fibonacci(5))
# print(fibonacci(6))
# print(fibonacci(7))
# print(fibonacci(8))
# time1 = 0
# for i in range(0,100): 
#     t1_start = perf_counter()
#     fibonacci(999)
#     t1_end = perf_counter() 
#     time1 += t1_end - t1_start

# tim2 = 0
# for i in range(0,100):
#     t2_start = perf_counter() 
#     fibonacci_iter(999)
#     t2_end = perf_counter() 
#     tim2 += t2_end - t2_start
# # print(sys.getrecursionlimit())
# print(f'first one took {time1} seconds')
# print(f'first one took {tim2} seconds')
print(fibonacci_iter(999999))
# print(fibonacci(9999))