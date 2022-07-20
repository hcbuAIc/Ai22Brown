import numpy as np
import random
def normalDistributedGrade():
    return np.random.normal(0.85,1,10)[random.randint(0,10)]

class Course():

    def __init__(self,name,subject,teacher):
        self.teacher = teacher
        self.name = name
        self.subject = subject
        #students are contained in a list like this [example_student,grade ex. 0.88]
        self.students = []
        self.period = 0
    
    def Cancel(self):
        pass
    def Enroll(self,student):
        self.students.append([student,"A"])
        student.Classes.appen(self)
    def UnEnroll(self,student):
        for i in range(len(self.students)):
            if (self.students[i][0] == student):
                studentClassIndex = self.students[i][0].Classes.index(self)
                if (studentClassIndex != -1):
                    self.students[i][0].Classes.pop(studentClassIndex)

                self.students.pop(i)
                break
    def gradeStudents(self):
        for student in self.students:
            student[1] = normalDistributedGrade()
        