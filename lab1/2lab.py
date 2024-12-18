import random;

class Encrypter:
    SYMB_DICT:dict = {" ": -1, "-": -5}
    def __init__(self) -> None:
        pass

    def Encrypt(self, INPUT_TEXT:str):
        ENCRYPTED_LIST: list
        INPUT_TEXT = INPUT_TEXT.lower()

        SUM_LIST: list

        ENCRYPTING_KEY = list(set(input("Введите последовательность различных символов до 8: ")))

        self.__Dict_Writer(ENCRYPTING_KEY);

        ENCRYPTED_LIST = self.__FisrtStepOutput(INPUT_TEXT)

        SUMMA = self.__Summator(ENCRYPTED_LIST)

        self.__MinAndMaxOutput(SUMMA)
        print(self.__Decrypting(SUMMA))

        for i, j in self.SYMB_DICT.items():
            print(i, j)

    def __Dict_Writer(self, ENCRYPTING_KEY: str):
        for i in range(0, len(ENCRYPTING_KEY)):
            self.SYMB_DICT[ENCRYPTING_KEY[i]] = i;
    
    def __FisrtStepOutput(self, INPUT_TEXT:str) -> list:
        RESULT: list = []
        for i in INPUT_TEXT:
            if(i in self.SYMB_DICT.keys()):
                RESULT.append(f"{self.SYMB_DICT[i]}")
            else: RESULT.append("-5")
        print(RESULT, INPUT_TEXT)
        return RESULT;
    
    def __Summator(self, ENCRYPTED_LIST: list) -> list:
        RESULT: list = []
        first = int(ENCRYPTED_LIST[-1]) + int(ENCRYPTED_LIST[1])
        if(first >= 10 or first <= -10):
            
            RESULT += self.__Separator(first)
        else: RESULT.append(first)
        
        for i in range(1, len(ENCRYPTED_LIST)-1):
            number = int(ENCRYPTED_LIST[i-1]) + int(ENCRYPTED_LIST[i+1])
            if(number >= 10 or number <= -10):
                RESULT += self.__Separator(number)
            else: RESULT.append(number)

        last = int(ENCRYPTED_LIST[-2]) + int(ENCRYPTED_LIST[0])
        if(last >= 10 or last <= -10):
            RESULT += self.__Separator(last)
        else: RESULT.append(last)

        return RESULT
    
    def __Separator(self, a:int) -> list:
        result = []
        if(a > 0):
            first = str(a)[0]
            second = str(a)[1]
            result.append(int(first))
            result.append(int(second))
        elif(a<0):
            first = str(a)[:2]
            second = str(a)[2:]
            result.append(int(first))
            result.append(int(second))
        return result

    def __MinAndMaxOutput(self, a:list) -> None:
        print(a)
        print(f"Минимум - {min(a)} Максимум - {max(a)} Среднее - {sum(a)/len(a)}")
    
    def __Decrypting(self, a:list) -> str:
        result: str = ""
        for i in a:
            for k, v in self.SYMB_DICT.items():
                if v == i:

                    result += k
                    break
            
            else:
                result += "*"
        return result;        
test = Encrypter();

test.Encrypt("тест тестировка тестировочка")
