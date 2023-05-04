
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return f"Point{self.x, self.y}"
    
    def __mul__(self, m):
        return f"Point{self.x*m, self.y*m}"
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    
class Polygon:
    def __init__(self):
        self.points = []
    
    def add_point(self, point: Point):
        self.points.append(point)
        
    def __str__(self):
        strp = ", ".join(str(p) for p in self.points)
        return f"Polygon[{strp}]"
    
    def __getitem__(self, item) -> int|slice:
        try: 
            return self.points[item]
        except TypeError:
            return f"Nie jest to ani int, ani slice"
        
        
print(Point())
print(Point(1,2))
print(Point(1,2)*10)
print(Point(1,2) == Point(1,2))
print(Point(1,2) == Point(2,1))

polygon=Polygon()
polygon.add_point(Point(3,4))
polygon.add_point(Point(5,6))
polygon.add_point(Point(7,8))
print(polygon)
print(polygon[Point()])