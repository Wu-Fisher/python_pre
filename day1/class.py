# numbers= [1,2,3]
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def move(self):
#         print("move")
    
#     def draw(self):
#         print("draw")

# po1=Point(1,2)
# po1.draw()
# print(po1.x)

class Person:
    def __init__(self,name) :
        self.name=name
    def talk(self):
        print(f"HI i m {self.name}")

john = Person("John Smith")
john.talk()
