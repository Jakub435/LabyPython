class Grade:

    def __init__(self, grade, weight):
        self.grade = grade
        self.weight = weight


class Student:
    grading = []

    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname

    def addgrade(self, grade, weight):
        self.grading.append(Grade(grade, weight))

    def getaverage(self):
        gradesum = 0
        for el in self.grading:
            gradesum += el.grade

        return gradesum/self.grading.count()


    def showgrading(self):
        for el in self.grading:
            print("grade: " + el.grade + "  weight: " + el.weight)
