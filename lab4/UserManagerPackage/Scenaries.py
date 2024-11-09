from UserManagerPackage import Order
from UserManagerPackage import Users
from UserManagerPackage import UsersGenerator



class HandleScenario:

    @staticmethod
    def Execute(Args):
        if(Args.possition != None):
            user = Users.Employee(Args.firstname, Args.lastname, Args.telephone, Args.address, Args.possition, Args.salary)
            user.writeLog()

class AutoScenario:

    @staticmethod
    def Execute(Args):
        user: Users.Employee = UsersGenerator.EmployeeGenerator.Generate()
        user.writeLog()
