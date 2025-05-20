import random


def generate_random_points(n_points):
    points = set()
    random.seed(n_points)
    spread = 5
    while len(points) < n_points:
        x = random.randint(-spread,spread)
        y = random.randint(-spread,spread)
        points.add((x,y))
    points_list = list(points)
    return sorted(points_list)

def cross(P, A, B):
    PA = ((A[0] - P[0]), (A[1] - P[1]))
    PB = ((B[0] - P[0]), (B[1] - P[1]))
    return (PA[0] * PB[1]) - (PA[1] * PB[0])

def convex_hull(n_points):
    points = generate_random_points(n_points)
    if len(points) < 3:
        return points, "A Convex Polygon must have at least 3 points"
    
    #lower hull
    lower = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)

    #upper hull
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)

    full_hull = lower[:-1] + upper[:-1]
    return points, sorted(full_hull)