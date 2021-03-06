from typing import Iterable


def except_zero(items: list) -> Iterable:
    out = list()
    myitems = items.copy()
    items.sort()
    

    for item in items:
        if item:
            out.append(item)
    
    for num,item in enumerate(myitems):
        if not item:
            out.insert(num,item)
    
    return out

if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))