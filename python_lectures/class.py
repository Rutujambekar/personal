class human:
    name= None
    age= None 
    def get_name(self):
        print("enter your name")
        self.name=input()
    def get_age(self):
        print("enter your age")
        self.age=input()
    def put_name(self):
        print("your name is",self.name)    
    def put_age(self):
        print("your age is", self.age)
person1 = human()
person1.get_name()
person1.get_age()
person1.put_name(), person1.put_age()