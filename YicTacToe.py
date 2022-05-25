from typing import List


def checkio(game_result: List[str]) -> str:
    Owin = False
    Xwin = False
    vertical = [game_result[0][0] + game_result[1][0] + game_result[2][0],
                game_result[0][1] + game_result[1][1] + game_result[2][1],
                game_result[0][2] + game_result[1][2] + game_result[2][2]]

    for x in vertical:
        if x.count('X') > 2:
            Xwin = True
        elif x.count('O') > 2:
            Owin = True
    
    Diagonal = [game_result[0][0] + game_result[1][1] + game_result[2][2],
                game_result[0][2] + game_result[1][1] + game_result[2][0]]
        



if __name__=='__main__':
    print(checkio([
    "XOX",
    "XX.",
    "XOO"]))