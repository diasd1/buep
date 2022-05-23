# -*- coding: utf-8 -*-
"""curiousLiDAR Shape finder"""
__copyright__ = ("Copyright (c) 2022 David Dias Horta, Paul Meier")

from typing import List, Optional, Tuple

from rovex import Speed


class Flat:
    """a Flat's data model"""
    def __init__(self,
                 count: int,
                 startAngle: int,
                 endAngle: int,
                 distance: float) -> None:
        self._count = count
        self._startAngle = startAngle
        self._endAngle = endAngle
        self._distance = distance

    @property
    def count(self) -> int:
        """angle count"""
        return self._count

    @property
    def startAngle(self) -> int:
        """start angle (in deg)"""
        return self._startAngle

    @property
    def endAngle(self) -> int:
        """end angle (in deg)"""
        return self._endAngle

    @property
    def distance(self) -> float:
        """distance in mm"""
        return self._distance

    def __repr__(self) -> str:
        return f"count={self.count} start={self.startAngle} \
end={self.endAngle} dist={self._distance}"

STOP_DISTANCE = 200
FRONT_ANGLE = 90
ANGLE_DEVIATION = 15

def findContestBalloon(data: List[float],
                       direction: bool = False) -> Optional[Tuple[Speed, Speed]]:
    """tries to find a balloon for the contest"""
    flats = _getFlats(data)
    print(flats)

    if not _collisionDetection(data):
        return (Speed.I, Speed.I)

    for count, flat in enumerate(flats):
        if flat.endAngle > FRONT_ANGLE > flat.startAngle:
            if data[FRONT_ANGLE] > STOP_DISTANCE:
                if direction:
                    return _driveToCornerRight(flat)
                return _driveToCornerLeft(flat)
        if count < len(flats) - 1:
            if _angleDeviation(
                    round((flats[count+1].startAngle-flat.endAngle) / 2) + flat.endAngle,
                    FRONT_ANGLE):
                return Speed.D2, Speed.D2
    return None

def _driveToCornerLeft(flat:Flat) -> Tuple[Speed, Speed]:
    if _angleDeviation(flat.endAngle, FRONT_ANGLE):
        return Speed.D2, Speed.D2
    return Speed.R1, Speed.D1

def _driveToCornerRight(flat:Flat) -> Tuple[Speed, Speed]:
    if _angleDeviation(flat.startAngle, FRONT_ANGLE):
        return Speed.D2, Speed.D2
    return Speed.D1, Speed.R1


def _angleDeviation(isAngle: int, shouldAngle: int) -> bool:
    """determines whether the deviation of two angles is acceptable"""
    if abs(isAngle - shouldAngle) <= ANGLE_DEVIATION:
        return True
    return False

def _collisionDetection(data : List[float]) -> bool:
    collisonCone = 5
    if data[FRONT_ANGLE + collisonCone] < STOP_DISTANCE and\
       data[FRONT_ANGLE - collisonCone] < STOP_DISTANCE:
        return False
    return True

def _getFlats(data: List[float]) -> List[Flat]:
    """gets all flats"""
    thresholdDist = 100
    thresholdAngle = 10
    foundFlats = []
    count = 0
    startAngle = 0
    previousDist = abs(data[0])
    #reduce FOV to 180°
    data = data[90:270]
    for angle,point in enumerate(data):
        if 0 < angle < len(data) - 3:
            deltaDistance =abs(data[angle] - data[angle-1])
            if deltaDistance < thresholdDist:
                count += 1
            else:
                previousDist = abs(data[angle-1])
                if abs(previousDist - data[angle+3]) > thresholdDist:
                    if count > thresholdAngle:
                        foundFlats.append(Flat(count, startAngle, angle, point))
                    startAngle = angle + 1
                    count = 0
    return foundFlats


if __name__ == "__main__":
    mockData = [0.0, 0.0, 4248.5, 4265.5, 4297.75, 0.0, 0.0, 0.0, 0.0, 4336.5, 317.5, 315.5, 314.5, 0.0, 0.0, 0.0, 0.0, 313.5, 312.0, 311.5, 312.0, 0.0, 0.0, 0.0, 312.0, 310.0, 310.0, 0.0, 310.0, 719.75, 905.0, 2659.25, 3014.75, 3001.75, 3006.25, 3046.25, 1642.25, 1653.75, 2173.0, 4763.0, 4761.0, 3426.25, 1908.25, 1935.5, 779.0, 8478.75, 9706.5, 11119.0, 13569.5, 329.25, 12840.75, 3816.75, 3507.75, 2828.5, 2859.5, 4028.75, 2615.25, 2616.25, 3831.5, 3854.5, 2157.25, 1849.25, 1844.5, 337.75, 2710.0, 2735.0, 2577.5, 2453.0, 2420.75, 2306.0, 2328.0, 1782.75, 2458.0, 2493.75, 1576.5, 1520.25, 1542.0, 1615.75, 1982.75, 335.75, 1490.75, 1521.75, 1529.25, 2117.25, 2157.25, 3961.0, 4402.25, 5682.25, 3800.75, 3632.5, 4374.5, 3123.5, 4124.5, 4610.5, 178.0, 960.75, 952.0, 948.5, 961.25, 962.25, 1264.75, 1252.75, 885.25, 870.75, 864.75, 856.75, 843.75, 829.75, 825.0, 817.0, 795.0, 801.0, 796.0, 792.0, 784.0, 780.0, 776.0, 770.0, 764.25, 760.25, 757.25, 752.25, 747.25, 745.25, 742.25, 738.25, 735.25, 734.25, 732.25, 730.25, 729.25, 727.25, 727.25, 725.25, 725.25, 726.25, 726.25, 726.25, 726.25, 726.25, 726.25, 726.25, 728.25, 728.25, 730.25, 732.25, 734.25, 266.5, 738.25, 741.25, 744.25, 747.25, 749.25, 754.25, 760.25, 326.25, 765.0, 772.0, 779.0, 783.0, 787.0, 795.0, 804.0, 809.0, 814.0, 825.0, 834.75, 839.75, 846.75, 858.75, 866.75, 872.75, 887.75, 902.5, 910.0, 898.5, 882.75, 866.75, 855.25, 842.75, 821.0, 778.0, 791.0, 781.0, 763.25, 746.25, 739.25, 731.25, 716.25, 703.25, 698.5, 691.5, 338.25, 680.5, 675.5, 669.5, 659.5, 649.5, 645.5, 640.5, 632.75, 625.75, 622.75, 618.75, 612.75, 606.75, 603.75, 600.75, 595.75, 591.75, 588.75, 587.75, 583.75, 580.75, 577.75, 576.75, 573.75, 573.75, 572.0, 570.0, 569.0, 568.0, 568.0, 567.0, 567.0, 567.0, 566.0, 568.0, 567.0, 567.0, 567.0, 568.0, 569.0, 570.0, 572.0, 573.0, 575.75, 576.75, 577.75, 581.75, 584.75, 586.75, 588.75, 593.75, 598.75, 600.75, 603.75, 316.0, 608.75, 609.75, 615.75, 621.75, 624.75, 629.75, 636.75, 644.5, 648.5, 653.5, 662.5, 666.5, 676.5, 321.75, 1538.5, 1561.0, 1574.0, 1591.0, 1623.75, 1662.5, 1672.5, 1694.5, 1735.25, 1775.25, 1884.25, 1745.25, 1716.5, 1535.5, 1553.0, 1576.0, 1614.75, 1659.5, 1679.5, 1707.5, 1763.25, 1820.0, 1851.75, 1883.75, 1961.0, 2037.75, 2076.5, 2119.75, 2216.5, 2328.0, 2378.75, 1000.75, 960.25, 924.5, 972.25, 850.25, 1171.0, 940.5, 976.75, 923.0, 1013.75, 953.5, 944.5, 946.5, 936.5, 929.5, 933.5, 963.25, 969.25, 987.25, 999.25, 994.25, 1000.25, 1006.25, 1017.25, 1215.75, 1279.0, 1432.0, 1403.5, 3585.5, 3682.25, 4056.75, 662.0, 662.0, 671.5, 527.0, 4150.25, 4102.5, 4076.75, 4102.0, 4111.0, 4130.0, 4093.0, 0.0, 0.0, 0.0, 0.0, 4157.75, 4171.75, 4179.75, 0.0, 0.0, 0.0, 0.0, 4125.0, 4192.75, 4206.75, 4169.75, 0.0, 0.0, 0.0, 0.0, 4213.5, 4213.5, 4230.5, 4194.75, 0.0, 0.0] # pylint: disable=line-too-long
    findContestBalloon(mockData)
