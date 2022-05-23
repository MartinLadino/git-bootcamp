def replace_last(line: list) -> list:
    first = 0
    if len(line) > 1:
        line.insert(first,line[len(line)-1])
        line.pop(len(line)-1)
        return line
    else:
        return line

if __name__=='__main__':
    print(replace_last([2,3,4,1]))
