from typing import List


def checkio(game_result: List[str]) -> str:
    Owin = False
    Xwin = False
    for x in game_result:
        if x.count('X') > 2:
            Xwin = True
        elif x.count('O') > 2:
            Owin = True
    
    if Xwin and Owin:
        return 'D'
    elif Xwin:
        return 'X'
    elif Owin:
        return 'O'



if __name__=='__main__':
    print(checkio([
    "XXX",
    "XX.",
    "OOO"]))