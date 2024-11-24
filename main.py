class Point:
def init_(self, x=0, y=0):
self.x = x
self.y = y
str_(self):
return "({0}, {1})".format(self.x, self.y)
p1 = Point(2, 3)
print(p1)
def _str_(self):
return "({0}, {1})".format(self.x, self.y)

# Create Object
p1 = Point(2, 3)
print(p1)