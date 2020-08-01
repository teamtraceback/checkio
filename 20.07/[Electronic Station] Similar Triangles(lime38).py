from typing import List, Tuple
Coords = List[Tuple[int, int]]

import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:


    # Set x, y position; point ( p1, p2, p3 // p4, p5, p6 )
    p1 = Point2D(x=coords_1[0][0], y=coords_1[0][1])
    p2 = Point2D(x=coords_1[1][0], y=coords_1[1][1])
    p3 = Point2D(x=coords_1[2][0], y=coords_1[2][1])
    
    p4 = Point2D(x=coords_2[0][0], y=coords_2[0][1])
    p5 = Point2D(x=coords_2[1][0], y=coords_2[1][1])
    p6 = Point2D(x=coords_2[2][0], y=coords_2[2][1])
    
         
    # Width & height is maximum value of triangles ( width/height1 // width/height2 )
    xa = abs(p2.x - p1.x)
    xb = abs(p3.x - p2.x)
    xc = abs(p3.x - p1.x)

    ya = abs(p2.y - p1.y)
    yb = abs(p3.y - p2.y)
    yc = abs(p3.y - p1.y)
    
    width1 = max(xa, xb, xc)
    height1 = max(ya, yb, yc)
    

    xd = abs(p5.x - p4.x)
    xe = abs(p6.x - p5.x)
    xf = abs(p6.x - p4.x)

    yd = abs(p5.y - p4.y)
    ye = abs(p6.y - p5.y)
    yf = abs(p6.y - p4.y)
    
    width2 = max(xd, xe, xf)
    height2 = max(yd, ye, yf)
    
    
    # Get one side length of triangle using 3-points ( l1, l2, l3 // l4, l5, l6 )
    # Get angles using 3 side length.  
    l1 = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
    l2 = math.sqrt((p3.x - p2.x)**2 + (p3.y - p2.y)**2)
    l3 = math.sqrt((p3.x - p1.x)**2 + (p3.y - p1.y)**2)
    
    l4 = math.sqrt((p5.x - p4.x)**2 + (p5.y - p4.y)**2)
    l5 = math.sqrt((p6.x - p5.x)**2 + (p6.y - p5.y)**2)
    l6 = math.sqrt((p6.x - p4.x)**2 + (p6.y - p4.y)**2)

    # Angles calculation
    ang1 = math.degrees(math.acos((l1 * l1 + l2 * l2 - l3 * l3)/(2.0 * l1 * l2)))
    ang2 = math.degrees(math.acos((l1 * l1 + l3 * l3 - l2 * l2)/(2.0 * l1 * l3)))
    ang3 = math.degrees(math.acos((l3 * l3 + l2 * l2 - l1 * l1)/(2.0 * l3 * l2)))
    
    ang4 = math.degrees(math.acos((l4 * l4 + l5 * l5 - l6 * l6)/(2.0 * l4 * l5)))
    ang5 = math.degrees(math.acos((l4 * l4 + l6 * l6 - l5 * l5)/(2.0 * l4 * l6)))
    ang6 = math.degrees(math.acos((l6 * l6 + l5 * l5 - l4 * l4)/(2.0 * l6 * l5)))
    #print(ang, ang2, ang3, ang4, ang5, ang6)
    
    degrees1 = []
    degrees2 = []
    degrees1.append(round(ang1,6))
    degrees1.append(round(ang2,6))
    degrees1.append(round(ang3,6))
    degrees2.append(round(ang4,6))
    degrees2.append(round(ang5,6))
    degrees2.append(round(ang6,6))
    degrees1 = sorted(degrees1)
    degrees2 = sorted(degrees2)
    print(degrees1, degrees2)
    
    print(width1, height1, width2, height2)
    
    # Res default is False 
    # Maximum width & height and angle(degree) are same == True
    # Only angles are same == True
    res = False
    if (width1 == width2) & (height1 == height2) & (degrees1 == degrees2) :
        res = True
    else:
        if (degrees1 == degrees2) :
            res = True

    return res


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # Tㅁhese "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
