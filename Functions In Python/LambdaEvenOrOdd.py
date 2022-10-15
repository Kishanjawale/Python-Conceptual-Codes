
#Check Even Or Odd (Normal Fuction)
from re import X


def CheckEven(No):
    if No%2==0:
        return True
    else:
        return False

def CheckEvenX(No):
    return(No%2==X)

#Main Functions
def main():
    Ret=CheckEvenX(15)

    if Ret==True:
        print("Even")
    else:
        print("Odd")

#Starter
if __name__=="__main__":
    main()