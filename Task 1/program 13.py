from abc import ABC, abstractmethod
class shape(ABC):
    def col(self,c):
        self.color=c
    def get_color(self):
        return self.color
    @abstractmethod
    def get_area(self):
        pass
class square(shape):
    def col(self,c,side):
        super().col(c)
        self.s=side
    def get_color(self):
        return self.color
    def get_area(self):
        area=self.s*self.s
        return area
c=input("enter color")
side=int(input("enter side"))
s=square()
s.col(c,side)
print("color:",s.get_color())
print("Area:",s.get_area())

    
    
    
