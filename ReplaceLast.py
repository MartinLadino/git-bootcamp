def replace_last(line: list) -> list:
    return line.insert(0,line[len-1])

if __name__=='__main__':
    print(replace_last([2,3,4,1]))
