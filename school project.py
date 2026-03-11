class Teacher :
    def __init__(self,name,salary,age):
        self.name = name
        self.salary =salary
        self.age = age
    def check_info(self):
        print("\nTeacher details")
        print("name:",self.name)
        print("salary:",self.salary)
        print("age:",self.age)
        
class Student:
    def __init__(self,name,age,fees):
        self.name =name
        self.age = age
        self.fees = fees
    def check_info(self):
        print("\nStudent details")
        print("name:",self.name)
        print("age:",self.age)
        print("fees:",self.fees)
        
class Workers:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def check_info(self):
        print("\nWorkers details")
        print("age:",self.age)
        print("salary:",self.salary)
        
for i in range(50):
    print("\nschool program")
    print("1.enter Teacher")
    print("2.enter Student")
    print("3.enter worker")
    print("4.exit")
    
    choice = input("choose option(1-4) ")
    
    if choice == "1":
        name =input("enter your name: ")
        
        salary = input("enter your salary: ")
        if not salary .isdigit():
            print("salary must be numbers")
            continue
        age = input("enter your age: ")
        if not age.isdigit():
            print("age must be numbers")
        t = Teacher(name,age,salary)
        t .check_info()
        
    elif choice == "2":
        name = input("enter your name: ")
        
        age = input("enter your age: ")
        if not age. isdigit():
            print("age must be in numbers")
            continue
        fees = input("enter your fees: ")
        if not fees.isdigit():
            print("fess must be numbers")
            continue
        s =Student(name,age,fees)
        s.check_info()
        
    elif choice == "3":
        name = input("enter your name: ")
        
        age = input("enter your age: ")
        if not age . isdigit():
            print("age must be numbers")
            continue
        salary =input("enter your salary: ")
        if not salary . isdigit():
            print("salary must be numbers")
            continue
        w1 = Workers (name,age,salary)
        w1. check_info()
        
    elif choice == "4":
        print("the end")
        break
    else:
        print("wrong choice")
        
    
     






