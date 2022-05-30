from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    out = list()

    if border not in items:
        return items
    for x in items:
        if x is not border:
            out.append(x)
        else:
            break
    out.append(border)

    return out



if __name__ == '__main__':
    print(list(remove_all_after([1, 1, 2, 2, 3, 3], 2)))