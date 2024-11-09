from UserManagerPackage import Order
from UserManagerPackage import Users
from UserManagerPackage import UsersGenerator



class HandleScenario:

    @staticmethod
    def Execute(Args):
        if(Args.position != None):
            user = Users.Employee(Args.firstname, Args.lastname, Args.telephone, Args.address, Args.position, Args.salary)
            user.writeLog()
        elif(Args.order != None):
            order = Order.Order(Args.order)
            user = Users.Client(Args.firstname, Args.lastname, Args.telephone, Args.address, order)
            user.writeLog()

class AutoScenario:

    @staticmethod
    def Execute(Args):
        user: Users.Employee = UsersGenerator.EmployeeGenerator.Generate()
        user.writeLog()
