import math

def get_distance(point1, point2):
    # Euclidean distance between 2 points represented as tuples
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((y2-y1)**2 + (x2-x1)**2)


def get_point_on_line(start, end, distance):
    magnitude = get_distance(start, end)
    if magnitude == 0:
        return start

    start_x, start_y = start
    end_x, end_y = end
    unit_vector = ((end_x-start_x)/magnitude, (end_y-start_y)/magnitude)
    return start_x + unit_vector[0]*distance, start_y + unit_vector[1]*distance

def get_nearest_point(curr_point, other_points):
    if not other_points:
        return curr_point

    min_distance = float('inf')
    nearest_point = None

    for other_point in other_points:
        distance = get_distance(curr_point, other_point)
        if distance < min_distance:
            min_distance = distance
            nearest_point = other_point
    return nearest_point