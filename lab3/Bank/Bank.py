from Bank._BankEntities import *
from Bank._BankTools import *

from prettytable import PrettyTable;

class Bank:
    BANK_FILLIAL: str
    BANK_LOANS: list[Loan]

    def __init__(self, fillial:str):
        self.BANK_FILLIAL = fillial
        self.BANK_LOANS = []

    def MakeLoan(self, loanSum:float, LoanTerm: int, LoanRate: float):
        NormilizedRate = BankTools.RateNormilizer(LoanRate)
        loan = Loan(len(self.BANK_LOANS), loanSum, LoanTerm, NormilizedRate)
        self.BANK_LOANS.append(loan)
    
    def OutputInConsoleAnnuityPaymentByLoanID(self, LoanID: int) -> None: 
        loan: Loan

        result: PrettyTable = PrettyTable()
        result.field_names = ["№Платежа", "Задолженность", "Начисленные проценты", "Основной долг", "Сумма платежа"]
        result.align["№Платежа"] = "c"
        result.align["Задолженность"] = "r"
        result.align["Начисленные проценты"] = "r"
        result.align["Основной долг"] = "r"
        result.align["Сумма платежа"] = "r"

        for _loan in self.BANK_LOANS:
            if _loan.LOAND_ID == LoanID:
                loan = _loan
                break
        CalculatedPayments = BankTools.CalculateAnnuityPayments(loan)
        for row in CalculatedPayments:
            result.add_row(row)
        print(result)
