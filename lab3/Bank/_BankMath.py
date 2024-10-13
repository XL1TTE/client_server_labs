class BankMath:
    @staticmethod
    def Round(value, decimals=2):
        factor = 10 ** decimals
        return round(value * factor) / factor
