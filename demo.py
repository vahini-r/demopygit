class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calc_area(self):
        return self.length*self.breadth
    def calc_peri(self):
        return 2*(self.length + self.breadth)
rect=Rectangle(13,7)
print(rect.calc_area())
print(rect.calc_peri())
