#teste de eficiencia entre estruturas de loop utilizando operação quadrática
import timeit
import numpy as np

def using_for(arr):
    res = []
    for num in arr:
        res.append(num*num)
    return res

def using_while(arr):
    res = []
    i = 0
    while i < len(arr):
        res.append(arr[i] * arr[i])
        i += 1
    return res

def using_list_comprehention(arr):
    return [num * num for num in arr]

#construindo um list_comprehention
def using_list_map_lambda(arr):
    return list(map(lambda x : x * x, arr))

def using_square_numpy(np_arr):
    return np.square(np_arr)

arr = list(range(1,1_000_001))
np_arr = np.arange(1,1_000_001)

for_time = timeit.timeit("using_for(arr)", globals=globals(), number=1)
while_time = timeit.timeit("using_while(arr)", globals=globals(), number=1)
list_comprehention_time = timeit.timeit("using_list_comprehention(arr)", globals=globals(), number=1)
list_map_lambda_time = timeit.timeit("using_list_map_lambda(arr)", globals=globals(), number=1)
square_numpy_time = timeit.timeit("using_square_numpy(np_arr)", globals=globals(), number=1)

print(f'for_time: {for_time:.6f}')
print(f'while_time: {while_time:.6f}')
print(f'list_comprehention_time: {list_comprehention_time:.6f}')
print(f'list_map_lambda_time: {list_map_lambda_time:.6f}')
print(f'square_numpy_time: {square_numpy_time:.6f}')