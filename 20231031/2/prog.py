from math import sqrt, isclose
class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.a = sqrt((point2[0] - point3[0])**2 + (point2[1] - point3[1])**2)
        self.b = sqrt((point1[0] - point3[0])**2 + (point1[1] - point3[1])**2)
        self.c = sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

    def __bool__(self):
        return abs(self) != 0
    
    def __abs__(self):
        side1, side2, side3 = sorted([self.a, self.b, self.c])
        if not ((side1 > 0 and side2 > 0 and side3 > 0) and (side3 < side1 + side2)):
            return 0
        x1, y1 = self.point1
        x2, y2 = self.point2
        x3, y3 = self.point3
        return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    
    def __lt__(self, obj):
        return abs(self) < abs(obj)

    def is_point_in_triangle(self, point):
        x0 = self.point1[0]
        y0 = self.point1[1]
        x1 = self.point2[0]
        y1 = self.point2[1]
        x2 = self.point3[0]
        y2 = self.point3[1]
        x = point[0]
        y = point[1]
        q1 = (x0-x)*(y1-y)-(x1-x)*(y0-y)
        q2 = (x1-x)*(y2-y)-(x2-x)*(y1-y)
        q3 = (x2-x)*(y0-y)-(x0-x)*(y2-y)
        return (q1 >= 0 and q2 >= 0 and q3 >= 0) or (q1 <= 0 and q2 <= 0 and q3 <= 0)

    def __contains__(self, obj):
        if isclose(abs(obj), 0):
            return True
        if isclose(abs(self), 0):
            return False
        return self.is_point_in_triangle(obj.point1) and \
            self.is_point_in_triangle(obj.point2) and self.is_point_in_triangle(obj.point3)

    def __and__(self, obj):
        if isclose(abs(obj), 0) or isclose(abs(self), 0):
            return False
        if self in obj or obj in self:
            return True
        self_edges = [(self.point1, self.point2), (self.point2, self.point3), (self.point3, self.point1)]
        obj_edges = [(obj.point1, obj.point2), (obj.point2, obj.point3), (obj.point3, obj.point1)]

        intersection = Intersection()
        for edge1 in self_edges:
            for edge2 in obj_edges:
                if intersection.do_segments_intersect(edge1[0], edge1[1], edge2[0], edge2[1]):
                    return True
        return False


class Intersection:
    def orientation(self, point1, point2, point3):
            tmp = (point2[1] - point1[1]) * (point3[0] - point2[0]) - (point2[0] - point1[0]) * (point3[1] - point2[1])
            if tmp == 0:
                return 0  
            return 1 if tmp > 0 else 2 
    
    def is_point_on_segment(self, first, point, second):
            return (point[0] <= max(first[0], second[0]) and point[0] >= min(first[0], second[0]) and
                    point[1] <= max(first[1], second[1]) and point[1] >= min(first[1], second[1]))

    def do_segments_intersect(self, A, B, C, D):
        o1 = self.orientation(A, B, C)
        o2 = self.orientation(A, B, D)
        o3 = self.orientation(C, D, A)
        o4 = self.orientation(C, D, B)

        if o1 != o2 and o3 != o4:
            return True

        if (o1 == 0 and self.is_point_on_segment(A, C, B)) or (o2 == 0 and self.is_point_on_segment(A, D, B)) \
                or (o3 == 0 and self.is_point_on_segment(C, A, D)) or (o4 == 0 and self.is_point_on_segment(C, B, D)):
            return True

        return False


import sys
exec(sys.stdin.read())
