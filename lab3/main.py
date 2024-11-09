from Bank import Bank


a = Bank("xlBank")
a.MakeLoan(1000, 12, 20)
a.MakeLoan(10000, 6, 15)
a.MakeLoan(1000000, 24, 0.1)

a.OutputInConsoleAnnuityPaymentByLoanID(0)
a.OutputInConsoleAnnuityPaymentByLoanID(1)
a.OutputInConsoleAnnuityPaymentByLoanID(2)

