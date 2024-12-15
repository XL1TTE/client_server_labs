from FileManager.Managers import FileManager
from UserManagerPackage import Order

from abc import ABC, abstractmethod


class User(ABC):
    firstname: str
    lastname: str
    telephone: str
    address: str
    def __init__(self, firstname: str, lastname: str, telephone: str, address: str):
        self.firstname = firstname
        self.lastname = lastname
        self.telephone = telephone
        self.address = address

    @abstractmethod
    def writeLog(self):
        line = f"firstname: {self.firstname}, lastname: {self.lastname}, telephone: {self.telephone}, address: {self.address}"
        output = FileManager(output_path="Employee.txt")
        output.WriteOneLine(line=line)

class Employee(User):
    position: str
    salary: str
    def __init__(self, firstname:str, lastname:str, telephone:str, address:str, position:str, salary: str):
        super().__init__(firstname, lastname, telephone, address)
        self.position = position
        self.salary = salary  

    def writeLog(self):
        log = f"firstname: {self.firstname}, lastname: {self.lastname}, telephone: {self.telephone}, address: {self.address}, position: {self.position}, salary: {self.salary}"
        output = FileManager(output_path="Employee.txt")
        output.WriteOneLine(line=log)
        
class Client(User):
    order: Order
    def __init__(self, firstname:str, lastname:str, telephone:str, address:str, Order:Order):
        super().__init__(firstname, lastname, telephone, address)
        self.order = Order

    def writeLog(self):
        output = FileManager(output_path="Clients.txt")
        output.WriteOneLine(
            line=f"firstname: {self.firstname}, lastname: {self.lastname}, telephone: {self.telephone}, address: {self.address}, order: {self.order.number}")
