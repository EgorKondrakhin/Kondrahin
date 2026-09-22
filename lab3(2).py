import math 
a = -0.5
b = 0.7 
def calc_y(x):
    return math.sqrt(3*(2+x**2)/ (1-2*x**2)) + (math.cos(x)**2 / (1- math.sin(x)**2))
print(round(calc_y(a), 5))
print(round(calc_y(b), 5))