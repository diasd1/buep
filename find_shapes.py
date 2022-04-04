
def locate_flat(data: list) -> int:
    tolerance = 500
    point_count = 0
    distance_change = []
    for angle, distance in enumerate(data):
        if angle > 0:
            distance_change.append(distance - data[angle-1])
    for angle,distance in enumerate(distance_change):
        if angle >= 360:
            pass
        if distance - distance_change[angle+1] > tolerance or distance - distance_change[angle+1] < -tolerance:
            break
        point_count += 1
        if point_count > 4:
            if angle < 180:
                return 1
            elif angle > 180:
                return -1
