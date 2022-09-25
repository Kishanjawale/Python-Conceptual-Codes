print("Program to demonstrate industrial Programming")

import MarvellousModule

def main():

    print("Enter First Number:")
    no1=int(input())

    print("Enter Second Number")
    no2=int(input())

    iRet = MarvellousModule.Addition(no1,no2)

    print("Addition is :",iRet)

if __name__ == "__main__":      #starter
    main()