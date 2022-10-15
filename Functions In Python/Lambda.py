#Normal Function / Named Function
def Add(No1,No2):
    return No1+No2


#Lambda Function /Unnamed Function
#Lambda Parameters : body
AddFunction= lambda A,B:A+B

#Main Function
def main():
    Ans1=Add(10,11)

    Ans2=AddFunction(10,11)

    print("Addition Using Normal Function:",Ans1)
    print("Addition Using Lambda Function:",Ans2)
    print(type(AddFunction))

#Starter
if __name__=="__main__":
    main()