from datetime import datetime

employees = []


class Employee:
    def __init__(self, name: str, gender: str, dob: datetime, maritial_status: str, nationality: str):
        self.name = name.lower().strip()
        self.gender = gender.lower().strip()
        self.dob = dob.strftime('%d-%m-%Y')
        self.age = str((datetime.today() - dob)/365).split()[0]
        self.maritial_status = maritial_status.lower().strip()
        self.nationality = nationality.lower().strip()


class Operations:
    @staticmethod
    def register_emp(employee: Employee):
        employees.append(employee)

    @staticmethod
    def get_emp_by_name(emp_name):
        for emp in employees:
            if emp.name == emp_name:
                return emp.__dict__


num = int(input('To add employee enter 0 : '))
while num == 0:
    _name = input("Enter employee's name: ")
    _gender = input("Enter employee's gender: ")
    _dob = datetime.strptime(input("Enter employee's birth date in DD-MM-YYYY format: "), '%d-%m-%Y')
    _maritial_status = input("Enter employee's maritial status: ")
    _nationality = input("Enter employee's nationality: ")
    _emp = Employee(_name, _gender, _dob, _maritial_status, _nationality)
    Operations.register_emp(_emp)
    num = int(input('To add employee enter 0 : '))

print(Operations.get_emp_by_name('maulik'))
