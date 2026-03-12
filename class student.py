class student :
    subjects_available =["math","english","kiswahili","history","computer"]
    
    def __init__(self,name,subject,age,fees):
        self.name =name
        self.subject =subject
        self.age = age
        self.fees = fees
    def check_info(self):
        print("\nstudent details")
        print("name",self.name)
        print("subject",self.subject)
        print("age",self.age)
        print("fees",self.fees)
        
students = []

for i in range(50):
    print("enter student details",i+1)
    
    while True:
        name = input("enter your name: ")
        if name.isalpha():
            break
        else:
            print("use letters only")
    while True:
        age = input("enter your age:")
        if age . isdigit():
            break
        else:
            print("must be in numbers")
    while True:
        fees = input("enter your fees: ")
        if fees .isdigit():
            break
        else:
            print("must be numbers")
    while True:
        subject = input("enter your subject: ")
        if subject in student.subjects_available:
            break
        else:
            print("subject not available")
            print("available subjects:",student.subjects_available)
    
student = student(name,subject,age,fees)
student.append(student)

student.check_info()
  
    
    
