from datetime import datetime
from datetime import timedelta
from typing import List

def sum_light(els: List[datetime]) -> int:
    timebulb1 = els[0] - els[1]
    timebul2 = els[2] - els[3]

    totaltime = abs(timedelta.total_seconds(timebulb1)) + abs(timedelta.total_seconds(timebul2))
    return totaltime


if __name__=='__main__':
    print(sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
    ]))