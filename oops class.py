#Create 3 class with objects using oops concepts in python
#class 1:student
class student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def show__details(self):
        print(f"studentname{self.name},roll no:{self.roll_no}")
#class 2:teacher
class teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject = subject
    def show__details(self):
        print(f"teacher name:{self.name},subject:{self.subject}")
#class 3:course
class course:
    def __init__(self,course_name,teacher):
        self.course_name=course_name
        self.teacher=teacher
    def show_course(self):
        print(f"course:{self.course_name},taught by:{self.teacher.name}")
student1=student("madhuri",101)
teacher1=teacher("mr.sharma","python programming")
course1=course("intro to python",teacher1)
student1.show__details()
teacher1.show__details()
course1.show_course()