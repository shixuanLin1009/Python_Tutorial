# Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
    def __init__(self,name,age,disease,height):
        self.__disease=disease 
        self.name=name
        self.age=age
        self.height=height
    def __str__(self):
        return "Name: "+self.name+" Age: "+str(self.age)
    def older(self):
        self.age+=1
    def greeting(self):
        return "Hello, my name is "+self.name
    def changeName(self,new_name):
        self.name=new_name
        return "Chang name is done!"




    