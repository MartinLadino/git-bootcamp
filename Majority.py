def is_majority(items: list) -> bool:
    if len(items) < 1:
        return False
    i = 0
    j = 0
    for x in items:
        if x:
            i+=1
        else:
            j+=1

    return i > j


if __name__=='__main__':
    print(is_majority([]))