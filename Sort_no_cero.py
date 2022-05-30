from typing import Iterable


def except_zero(items: list) -> Iterable:
    items.sort()
    return items

if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))