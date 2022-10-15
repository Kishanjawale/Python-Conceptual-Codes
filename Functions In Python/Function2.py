#positional Arguments  /  Position Argument 

def Add(No1,No2):
    print("Value of No1",No1)
    print("value of No2",No2)
    return No1+No2

def Sub1(No1,No2):
    print("Value of No1",No1)
    print("value of No2",No2)
    return No1-No2

#Main Function
def main():
    Ans= Add(10,11)
    print("Addition is :",Ans)
    
    Ans=Sub1(No2=10,No1=11)
    print("Subtraction is :",Ans)

    Ans=Sub1(No1=10,No2=11)
    print("Subtraction is :",Ans)

#Starter
if __name__=="__main__":
    main()