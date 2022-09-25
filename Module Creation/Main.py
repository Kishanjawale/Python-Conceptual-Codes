print("Program to demonstrate industrial Programming")

import MarvellousModule

def main():

    print("Enter First Number:")
    no1=int(input())

    print("Enter Second Number")
    no2=int(input())


    iRet = MarvellousModule.Addition(no1,no2)
    print("Addition is :",iRet)

    iRet = MarvellousModule.Substraction(no1,no2)
    print("Substraction is :",iRet)

    iRet = MarvellousModule.Multiplication(no1, no2)
    print("Multiplication is :", iRet)

    iRet = MarvellousModule.Division(no1, no2)
    print("Division is :", iRet)


if __name__ == "__main__":      #starter
    main()
