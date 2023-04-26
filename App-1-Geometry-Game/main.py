from random import randint
import turtle

class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
  def falls_in_rectangle(self, rectangle):
      if rectangle.point1.x<self.x<rectangle.point2.x \
          and rectangle.point1.y<self.y<rectangle.point2.y:
          return True
      else:
          return False
  
  def distance_from_point(self, point):
    return ((self.x-point.x)**2+
            (self.y-point.y)**2)**.5

class Rectangle:
  def __init__(self, point1, point2):
    self.point1 = point1
    self.point2 = point2
  
  def calculate_area(self):
    return (self.point2.x-self.point1.x)*(self.point2.y-self.point1.y)

class GuiRectangle(Rectangle):
    def draw_in_canvas(self,canvas):
        canvas.penup()
        canvas.goto(self.point1.x,self.point1.y)
        canvas.pendown()

        canvas.forward(self.point2.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)
        
        

class GuiPoint(Point):
  def draw_in_canvas(self, canvas, size=5, color='red'):
    canvas.penup()
    canvas.goto(self.x, self.y)
    canvas.pendown()
    canvas.dot(size, color)
    

#Create Rectangle object instance
rectangle = GuiRectangle(Point(randint(0,400),randint(0,400)),
                    Point(randint(10,400),randint(10,400)))

#print rectangle coords
print(f"""Rectangle Coord: {rectangle.point1.x}, {rectangle.point1.y} and \
{rectangle.point2.x}, {rectangle.point2.y}""")

#get point and area from user
user_point = GuiPoint(float(input("Guess the x: ")),float(input('Guess the y: ')))
user_area = float(input("Guess rectangle area: "))

#calculate and print game results
print("Was your point inside the rectangle?", user_point.falls_in_rectangle(rectangle))
area_result = rectangle.calculate_area() - user_area
print(f'You were off by: {area_result}')

myturtle = turtle.Turtle()
rectangle.draw_in_canvas(canvas=myturtle)
user_point.draw_in_canvas(canvas=myturtle)

turtle.done()