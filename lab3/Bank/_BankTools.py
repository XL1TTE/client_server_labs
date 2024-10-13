from Bank._BankEntities import Loan
from Bank._BankMath import BankMath

class BankTools:
    @staticmethod
    def RateNormilizer(LoanRate: float) -> float:
        if( 0 < LoanRate <= 1):
            return LoanRate
        else:
            if(0 < abs(LoanRate) <= 100):
                return abs(LoanRate) / 100
            else:
                raise ValueError("Передано некоректное значение.")
    
    @staticmethod
    def CalculateAnnuityPayments(loan: Loan) -> list[tuple[str, float, float, float, float]]:
        Result = []

        loan_sum_temp = loan.LOAN_SUM
        LOAN_INTEREST_RATE_TEMP = loan.LOAN_INTEREST_RATE / 12
        LOAN_TERM_TEMP = loan.LOAN_TERM

        Bank_Win_Result: float = 0
        Loan_result: float = 0
        Loan_payment_result: float = 0


        AnnuityPayment : float = loan_sum_temp * (LOAN_INTEREST_RATE_TEMP / (1 - (1+LOAN_INTEREST_RATE_TEMP)**-LOAN_TERM_TEMP))
        for payment in range(1, LOAN_TERM_TEMP+1):
            ProcentLoanBody = LOAN_INTEREST_RATE_TEMP * loan_sum_temp
            MainLoanBody = AnnuityPayment - ProcentLoanBody

            Bank_Win_Result += ProcentLoanBody
            Loan_result += MainLoanBody
            Loan_payment_result += AnnuityPayment

            Result.append((str(payment), BankMath.Round(loan_sum_temp,2), BankMath.Round(ProcentLoanBody,2), BankMath.Round(MainLoanBody,2), BankMath.Round(AnnuityPayment)))
            loan_sum_temp -= MainLoanBody
        Result.append(("Итого", BankMath.Round(loan_sum_temp, 2), BankMath.Round(Bank_Win_Result, 2), BankMath.Round(Loan_result, 2), BankMath.Round(Loan_payment_result, 2)))
        return Result
        

