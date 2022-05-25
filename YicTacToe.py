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

    vertical = [game_result[0][0] + game_result[1][0] + game_result[2][0],
                game_result[0][1] + game_result[1][1] + game_result[2][1],
                game_result[0][2] + game_result[1][2] + game_result[2][2]]

    for x in vertical:
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
    
    Diagonal = [game_result[0][0] + game_result[1][1] + game_result[2][2],
                game_result[0][2] + game_result[1][1] + game_result[2][0]]
    
    for x in vertical:
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
    
    if Xwin == False and Owin == False:
        return 'D'
        



if __name__=='__main__':
    print(checkio([ "OOX", 
                    "XXO", 
                    "XOX"]))