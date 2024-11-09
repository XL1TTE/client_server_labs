from . import Users
from random import randint

class EmployeeGenerator:

    FIRST_NAMES = ["Андрей", "Артем", "Максим", "Владимир", "Виктор"]
    LAST_NAMES = ["Кошечкин", "Собачкин", "Одноразов", "Многоразов"]
    TELEPHONES = ["+489325346634", "+54353623623", "+367877653", "+5989999340"]
    ADDRESSES = ["", "Пушкина дом 1", "Киренского дом 2", "Ничегошенского дом 10", ""]
    POSSITIONS = ["Главный инженер", "Программист", "Менеджер продаж", "Маркетолог"]
    SALARIES = [1000, 2400, 4350, 10000, 203104, 534534, 412314]

    @staticmethod
    def Generate() -> Users.Employee:
        employee = Users.Employee(
            firstname=EmployeeGenerator.FIRST_NAMES[randint(0, len(EmployeeGenerator.FIRST_NAMES)-1)],
            lastname=EmployeeGenerator.LAST_NAMES[randint(0,  len(EmployeeGenerator.LAST_NAMES)-1)],
            telephone=EmployeeGenerator.TELEPHONES[randint(0,  len(EmployeeGenerator.TELEPHONES)-1)],
            address=EmployeeGenerator.ADDRESSES[randint(0,  len(EmployeeGenerator.ADDRESSES)-1)],
            position=EmployeeGenerator.POSSITIONS[randint(0,  len(EmployeeGenerator.POSSITIONS)-1)],
            salary=EmployeeGenerator.SALARIES[randint(0,  len(EmployeeGenerator.SALARIES)-1)],    
        )

        return employee
