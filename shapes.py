class Circle:
    
    def __init__(self,r):
        self.r=r
        
    def area(self):
       a=3.14*(self.r**2)
       return a
       
    def circumference(self):
       c=2*(3.14*self.r)
       return c
    
    
class Square:
    def __init__(self,a):
        self.a=a
        
    def area(self):
       a=self.a**2
       return a
        
    def perimeter(self):
        p=4*self.a
        return p
        
class Rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l
    
    def area(self):
        a=self.l*self.w
        return a
        
    def perimeter(self):
       p=2*(self.l+self.w)
       return p

class Sphere:
    def __init__(self,r):
        self.r=r
        
    def surface_area(self):
        a=4*3.142*(self.r**2)
        return a

    def volume(self):
        v=(4/3)*(3.14*(self.r**3))
        return v   
    
    
     
     
        
        