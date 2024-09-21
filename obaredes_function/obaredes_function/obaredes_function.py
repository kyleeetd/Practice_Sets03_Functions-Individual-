import math

a = 5
b = 7
c = 4

def triangle_area(a, b, c):
   
    s = (a + b + c) / 2
    
    a = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return a



print(f"Area of the triangle: {a}")

