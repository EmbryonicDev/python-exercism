def inequality(a, b, c):
    # Check the triangle inequality
    return a + b >= c and a + c >= b and b + c >= a


def equilateral(sides):
    if not inequality(sides[0], sides[1], sides[2]):
        return False

    # Check if all sides are equal
    return all(side == sides[0] and side != 0 for side in sides)


def isosceles(sides):
    if not inequality(sides[0], sides[1], sides[2]):
        return False

    # Check if at least two sides are equal
    return any(sides.count(side) >= 2 for side in sides)


def scalene(sides):
    if not inequality(sides[0], sides[1], sides[2]):
        return False

    # Check if all sides are different
    return len(set(sides)) == 3


if __name__ == "__main__":
    print(scalene([7, 3, 2]), False)
