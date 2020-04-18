from enum import Enum

class EmployeeType(Enum):
    Q_AND_A = 1
    MANAGER = 2
    DIRECTOR = 3


class Employee:

    def __init__(self):
        self.isBusy = False

class CallCenter:
    employee = {
        EmployeeType.MANAGER.value: [],
        EmployeeType.DIRECTOR.value: [],
        EmployeeType.Q_AND_A.value: []
    }

    def __init__(self):
        for i in range(0, 20):
            if(i%5==0):
                self.employee[EmployeeType.MANAGER.value].append(Employee())
            elif(i%11==0):
                self.employee[EmployeeType.DIRECTOR.value].append(Employee())
            else:
                self.employee[EmployeeType.Q_AND_A.value].append(Employee())


    def getFirstNotBusyByLevel(self, level):
        for emp in self.employee[level]:
            if(not emp.isBusy):
                emp.isBusy = True
                return emp
        return None


    def dipathCall(self):
        level = EmployeeType.Q_AND_A.value
        emp = None
        while(level <= EmployeeType.DIRECTOR.value):
            emp = self.getFirstNotBusyByLevel(level)
            if(emp != None):
                break
            level += 1

        if(emp==None):
            print("All employee are busy now")
        else:
            print("Connected with level: " + str(level))


def main():
    call = CallCenter()
    for i in range(0, 35):
        call.dipathCall()


if __name__ == '__main__':
    main()
