class Area:
    def __init__(self):
        pass 

    def circle(self, radius):
        return 3.14 * (radius ** 2)
    
    def rectangle(self, height, base):
        return height * base 
    
    def traingle(self, height, base):
        return 0.5 * height * base 
    

if __name__ == '__main__':

    radius = 1
    height = 2
    base = 3

    calc_area = Area()

    print(f'Area of circle with radius {radius}: {calc_area.circle(radius)}')
    print(f'Area of rectagle with height as {height} and base as {base} : {calc_area.rectangle(height, base)}')
    print(f'Area of traingle with height as {height} and base as {base} : {calc_area.traingle(height, base)}')