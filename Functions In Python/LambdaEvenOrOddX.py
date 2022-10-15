#Check Even Or Odd (Normal Fuction)
def CheckEven(No):
    if No%2==0:
        return True
    else:
        return False


#Check Even Or Odd (Normal but Compact Fuction)
def CheckEvenX(No):
    return(No   %   2   ==  X)

CheckEvenXX=lambda No: No%2==0

#Main Functions
def main():
    Ret=CheckEvenXX(20)

    if Ret==True:
        print("its Even")
    else:
        print("its Odd")

#Starter
if __name__=="__main__":
    main()