import math
class Figure:
    sides_count = 0
    filled = False
    def __init__(self,__color=(0,0,0), *__sides):
        if self.__is_valid_sides(*__sides):
            self.__sides = list(__sides)
        if self.__is_valid_color(*__color) :
            self.__color =list (__color)
        else:
            self.__color=[0,0,0]
    def get_color(self):
        return self.__color
    def __is_valid_color(self,r,g,b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))
    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color=[r,g,b]
        self.filled=True
    def  __is_valid_sides(self,*__sides):
         for s in self.__sides:
             if isinstance(s,int) and s > 0:
                 continue
         if len(self.__sides) == self.sides_count:
              return True
    def get_sides(self):
        if self.__is_valid_sides():
         return  self.__sides
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
         self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self,__color=(0,0,0),*__sides):
       super().__init__(__color,*__sides)
       if len(self.get_sides()) != self.sides_count:
           self.__sides = 1
    def __radius(self):
        self.__radius =  self.get_sides()  / (2 * math.pi)
        return self.__radius
    def get_square(self):
        return  self.__radius** 2 *math.pi
class Triangle (Figure):
    sides_count = 3
    def __init__ (self,__color=(0,0,0),*sides):
        super().__init__(__color,*sides)
        if len(self.get_sides()) != self.sides_count:
            self.__sides = [1] * self.sides_count
    def get_square(self):
        pp=sum(self.get_sides())/2
        return math.sqrt(pp*(pp-self.get_sides()[0])*(pp-self.get_sides()[1])*(pp-self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12
    def __init__(self,__color=(0,0,0),*sides ):
        super().__init__(__color, *sides)
        if len(sides) == 1:
           self.__sides = self.get_sides() * self.sides_count
        if len(self.get_sides()) != self.sides_count:
            self.__sides = [1] * self.sides_count

    def get_volume(self):
         return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
