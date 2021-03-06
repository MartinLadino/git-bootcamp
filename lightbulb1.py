from datetime import datetime
from datetime import timedelta
from typing import List

def sum_light(els: List[datetime]) -> int:
    lenght = len(els) - 1
    totaltime = 0
    while lenght > 0:
        totaltime += abs(timedelta.total_seconds(els[lenght] - els[lenght - 1]))
        lenght -= 2
    
    return int(totaltime)

    
if __name__=='__main__':
    print(sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 0 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 13, 11, 0 , 0),
    ]))