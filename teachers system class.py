class Teacher:
    def __init__(self,name,level,salary,subject):
        
        if name.isalpha():
            self.name = name
        else:
            print("invalid name")
            self.name = "unknown"
            
        levels = ["primary","secondary","college","university"]
        if level in levels:
            self.level = level
        else:
            print("invalid level")
            self.level = not set
            
        if salary . isdigit():
            self.salary = salary
        else:
            print("invalid salary")
            self. salary = "unknown"
        
        if subject.isalpha():
            self.subject = subject
        else:
            print("invalid subject")
            self.subject ="unknow"
            
    def display(self):
        print("\nTeacher details")
        print("name",self.name)
        print("level",self.level)
        print("salary",self.salary)
        print("subject",self.subject)
        
name = input("enter your name: ")
level = input("enter your level(primary/secondary/college/university): ")
salary = input("enter your slary: ")
subject = input("enter your subject: ")

t1 =Teacher(name,level,salary,subject)
t1.display()

            
        