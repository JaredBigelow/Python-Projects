#Class Definitions

class Quadratic:
    def __init__(self,a=0,b=0,c=0):
        self.a = a
        self.b = b
        self.c = c
        
class Pixel:
    def __init__(self,x,y,colour,brightness):
        self.x = x
        self.y = y
        self.colour = colour
        self.brightness = brightness
#Main
        
a = 1
b = 2
c = 3

myFirstQuadratic = Quadratic (a,b,c)
mySecondQuadratic = Quadratic (c,b,a)

myPixel = Pixel (0,0,"Blue",0)

print (myPixel.x,myPixel.y,myPixel.colour,myPixel.brightness)

myPixel.x = 5
myPixel.y = 8
myPixel.colour = "Red"
myPixel.brightness = 10

print (myPixel.x,myPixel.y,myPixel.colour,myPixel.brightness)
