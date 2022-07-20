class Student():

    def __init__(self):
        
        self.name = ""
        self.age = 0
        self.grade = 0
        self.Classes = []
        self.address = ""
        self.GPA = 0.0

    def __str__(self):
        return "name:"+self.name + "\n" + "age:"+str(self.age) + "\n" + "grade:"+str(self.grade) + "\n" + "GPA:"+str(self.GPA)+ "\n"
    