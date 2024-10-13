

class Loan:
    LOAND_ID: int
    LOAN_SUM: float
    LOAN_TERM: int
    LOAN_INTEREST_RATE: float
    def __init__(self, LoanID: int, loanSum:float, LoanTerm: int, LoanRate: float):
        self.LOAND_ID = LoanID
        self.LOAN_SUM = loanSum
        self.LOAN_TERM = LoanTerm
        self.LOAN_INTEREST_RATE = LoanRate
