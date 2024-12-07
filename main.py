class NameString:
    def __set_name__(self, owner, name):
        self.name='_'+name
    def __set__(self,instance,value:str):
        if type(value) is str:
            if value.isalpha():
                instance.__dict__[self.name]=value
            else:
                print("ismni togri kiriting!!!!!!!!1")
        else:
            print("ismni togri kiriting!!")
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Age:
    def __set__(self, age):
        self.Age=Age
    def __set__(self,instance,value:int):
        if type(value) is int:
            if value.isdigit():
                instance.__dict__[self.age]=value
            else:
                print("yoshni togri kiriting!!!!!!!!")
        else:
            print("yoshni togri kiriting!!")
    def __get__(self, instance, owner):
        return instance.__dict__[self.Age]
    def __delete__(self, instance):
        del instance.__dict__[self.Age]



class Person:
    ism=NameString()
    familiya=NameString()
    age = Age()
    def __init__(self,ism,familiya,age):
        self.age=age
        self.ism=ism
        self.familiya=familiya
p1=Person("toxir","toxirov",32)
print(p1.__dict__)
p1.name="zokir"
print(p1.name)
p1.age = "dfs"
print(p1.age)


































