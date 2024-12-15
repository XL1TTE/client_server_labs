import argparse

from UserManagerPackage import Scenaries

class UserManagerArgParser:

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Argument parser.')
        self.parser.add_argument(
            "-mode",
            type=str,
            choices=["auto", "handle"],
            help="Interaction mode",
            default="auto"
        )
        self.parser.add_argument(
            "-firstname",
            type=str,
            help="User's first name."
        )
        self.parser.add_argument(
            "-lastname",
            type=str,
            help="User's last name."
        )
        self.parser.add_argument(
            "-telephone",
            type=str,
            help="User's telephone number."
        )

        self.parser.add_argument(
            "-address",
            type=str,
            help="User's address."
        )
        
        self.parser.add_argument(
            "-position",
            type=str,
            help="Employee's position."
        )
        self.parser.add_argument(
            "-salary",
            type=str,  
            help="Employee's salary."
        )
        self.parser.add_argument(
            "-order",
            type=str,  
            help="Client's order number."
        )
        


    def Start(self):
        self.args = self.parser.parse_args()
        
        if self.args.mode == 'auto':
            print("Executed in auto mode.")
            Scenaries.AutoScenario.Execute(self.args)
        elif self.args.mode == 'handle':
            if not all([self.args.firstname, self.args.lastname, self.args.telephone]):
                print("Error: First name, last name, and telephone are required in handle mode.")
                return
            print("Executed in handle mode.")
            Scenaries.HandleScenario.Execute(self.args)
        else:
            print("Error")
    
    def GetArgs(self):
        return self.args
