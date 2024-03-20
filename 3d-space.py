import math

class Coord3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def farther_from_origin(p1, p2):
    dist1 = math.sqrt(p1.x ** 2 + p1.y ** 2 + p1.z ** 2)
    dist2 = math.sqrt(p2.x ** 2 + p2.y ** 2 + p2.z ** 2)

    # Compare distances and return the point with the greater distance
    return p1 if dist1 > dist2 else p2

if __name__ == "__main__":
    pointP = Coord3D(10, 20, 30)
    pointQ = Coord3D(-20, 21, -22)

    print("Point P:", pointP.__dict__)
    print("Point Q:", pointQ.__dict__)

    ans = farther_from_origin(pointP, pointQ)
    print("Farther point:", ans.__dict__)
