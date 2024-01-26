

class Point:
    
    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        return self._x_coord
    def get_y_coord(self):
        return self._y_coord
    
    def distance_to(self, point):
        return (((self.get_x_coord() - point.get_x_coord()) ** 2) + ((self.get_y_coord() - point.get_y_coord()) ** 2)) ** 0.5
    

class LineSegment:

    def __init__(self, point_obj1, point_obj2):
        self._point_obj1 = point_obj1
        self._point_obj2 = point_obj2

    def get_point_obj1(self):
        return self._point_obj1
    def get_point_obj2(self):
        return self._point_obj2
    
    def length(self):
       return self.get_point_obj1().distance_to(self.get_point_obj2())
    
    def slope(self):
       slope_ans = ((self.get_point_obj1().get_y_coord())- (self.get_point_obj2().get_y_coord())) /  ((self.get_point_obj1().get_x_coord()) - (self.get_point_obj2().get_x_coord()))
       return slope_ans

    def is_parallel_to(self, other_line):
        if abs((self.slope()) - (other_line.slope())) < 0.00001:
            return True
        return False
        
point_1 = Point(7,4)
point_2 = Point(-6,18)
print(f'this is the distance to {point_1.distance_to(point_2)}')
line_seg_1 = LineSegment(point_1,point_2)
print(f'this is the length {line_seg_1.length()}')
print(f'this is the slope {line_seg_1.slope()}')

point_3 = Point(-2,2)
point_4 = Point(24, 12)
line_seg_2 = LineSegment(point_3,point_4)
print(f'parallel to?: {line_seg_1.is_parallel_to(line_seg_2)}')


    
