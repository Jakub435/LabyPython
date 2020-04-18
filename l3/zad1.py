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

        return gradesum/len(self.grading)

    def showgrading(self):
        for el in self.grading:
            print("grade: " + str(el.grade) + "  weight: " + str(el.weight))


class Gradebook:
    students = []

    def loadstudents(self, students):
        self.students = students

    def addstudent(self, firstname, lastname):
        self.students.append(Student(firstname, lastname))

    def getstudent(self, firstname, lastname):
        for el in self.students:
            if(el.firstName == firstname and el.lastName == lastname):
                return el

    def addgrade(self, firstname, lastname, grade, weight):
        self.getstudent(firstname, lastname).addgrade(grade, weight)

    def getstudentaveragegrade(self, firstname, lastname):
        return self.getstudent(firstname, lastname).getaverage()

    def showstudentgrades(self, firstname, lastname):
        self.getstudent(firstname, lastname).showgrading()


def main():
    gradebook = Gradebook()
    gradebook.addstudent("Jan", "Kowalski")
    gradebook.addgrade("Jan", "Kowalski", 5, 1)
    gradebook.addgrade("Jan", "Kowalski", 4, 1)
    gradebook.addgrade("Jan", "Kowalski", 3, 1)  # average = 3
    gradebook.addgrade("Jan", "Kowalski", 2, 1)
    gradebook.addgrade("Jan", "Kowalski", 1, 1)

    print(gradebook.getstudentaveragegrade("Jan", "Kowalski"))
    gradebook.showstudentgrades("Jan", "Kowalski")


if __name__ == '__main__':
    main()
