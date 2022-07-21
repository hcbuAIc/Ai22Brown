#feel free to mess with it I didn't get to finish beacuse we started linear algebra
import random,Student,Course

names = ["Tim","Susan","Joan","Dave","Bill","Amy","Jan"]
middleInitials = list("qwertyuiopasdfghjklzxcvbnm")
surnames = ["Wilson","Brandt","Conzuela","Marco","Smith","Doe","Martin"]
nameExtensions = ["Jr","II","III"]

studentRegistry = []
courseRegistry = [[],[],[],[],[],[],[],[],[],[],[],[]]

#grades 1-12 each nested list is a grade
classes = [
["counting,math","reading,english","science,science","spanish,spanish","social studies,history"], #1st grade
["math,math","writing,english","science,science","spanish,spanish","social studies,history"], #2nd grade
["math,math","writing,english","science,science","spanish,spanish","social studies,history"], #3rd grade
["math,math","writing,english","science,science","spanish,spanish","social studies,history"], #4th grade
["math,math","writing,english","science,science","spanish,spanish","social studies,history"], #5th grade
["math,math","english,english","science,science","spanish,spanish","history,history"], #6th grade
["pre-algebra,math","literature,english","cience,science","spanish,spanish","history,history"], #7th grade
["algebra,math","literature,english","cience,science","spanish,spanish","history,history"], #8th grade
["geometry,math","creative writing,enlgish","science,science","spanish,spanish","history,history"], #9th grade
["algebra II,math","american literature,english","science,science","spanish,spanish","history,history"], #10th grade
["pre-calculus,math","english II,english","science,science","spanish,spanish","history,history"], #11th grade
["calculus,math","english III,english","science,science","spanish,spanish","history,history"]] #12th grade

for c in classes:
    courseRegistry.append([])
    for i in range(5):
        name = c[i].split(",")[0]
        subject = c[i].split(",")[1]
        
        newClass = Course.Course(name,subject,random.choice(surnames))
        courseRegistry[-1].append(newClass)

def Populate(grade,numStudents):

    for i in range(numStudents):
        newStudent = Student.Student()
        spacer = " "
        extension = ""
        if (random.randint(0,100) < 80):
            spacer = " " + random.choice(middleInitials).upper()+ " "
        if (random.randint(0,100) < 5):
            extension = " " + random.choice(nameExtensions)
        newStudent.name= random.choice(names)+spacer+random.choice(surnames)+extension

        studentRegistry.append(newStudent)
        for course in courseRegistry[grade-1]:
            course.Enroll(studentRegistry[-1])


Populate(9,5)

 