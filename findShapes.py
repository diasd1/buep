"""TODO (meierp)"""

from typing import List


def locateFlat(data: List[float]) -> int:
    """TODO (meierp)"""
    tolerance = 500
    pointCount = 0
    distanceChange = []
    for angle, distance in enumerate(data):
        if angle > 0:
            distanceChange.append(distance - data[angle-1])
    for angle, distance in enumerate(distanceChange):
        if angle >= 360:
            pass
        if distance - distanceChange[angle+1] > tolerance or\
           distance - distanceChange[angle+1] < -tolerance:
            break
        pointCount += 1
        if pointCount > 4:
            if angle < 180:
                return 1
            if angle > 180:
                return -1
            return 0 # TODO (meierp)
    return 0 # TODO (meierp)
