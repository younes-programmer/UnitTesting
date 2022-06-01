import math


def equation_resolve(a, b):
    """
    TODO
    Write a function that resolves equation of type ax + b = 0
    """
    solutions = "non"
    if a == 0:
        return solutions
    solutions = -b/a
    return solutions


def equation_resolve_second_degree(a, b, c):
    """
    TODO
    Write a function that resolves equation of type ax^2 + bx + c = 0
    """
    delta = b*b-4*a*c
    if delta < 0:
        return []
    elif delta == 0:
        return [-b/(2*a)]
    else:
        return[(-b-math.sqrt(delta))/(2*a), (-b+math.sqrt(delta))/(2*a)]
