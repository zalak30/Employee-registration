from datetime import datetime

employees = []
class Employee:
    def __init__(self, name, gender, dob, maritial_status, nationality):
        self.name = name.lower()
        self.gender = gender.lower()
        self.dob = dob
        self.age = str((datetime.today() - dob)/365).split()[0]
        self.maritial_status = maritial_status.lower()
        self.nationality = nationality.lower()


num = int(input('To add employee enter 0 : '))
while num == 0:
    _name = input("Enter employee's name: ")
    _gender = input("Enter employee's gender: ")
    _dob = datetime.strptime(input("Enter employee's birth date in DD-MM-YYYY format: "), "%d-%m-%Y")
    _maritial_status = input("Enter employee's maritial status: ")
    _nationality = input("Enter employee's nationality: ")
    num = int(input('To add employee enter 0 : '))
    employee = Employee(_name, _gender, _dob, _maritial_status, _nationality)
    employees.append(employee)


print(employees)
