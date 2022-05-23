import math

def index_power(array: list, n: int) -> int:
    return int(math.pow(array[n],n))




if __name__=='__main__':
    print(index_power([1, 2, 3, 4], 2))