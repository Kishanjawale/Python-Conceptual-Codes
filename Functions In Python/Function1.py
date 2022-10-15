
#Function which accpepts nothing and returns nothing...
def  Demo1():
    print("Inside Demo1")

#Fucntion Accpets one parameter and returns nothing
def Demo2(No):
    print("Inside Demo2 With Argument ..")

#Fucntion Accepts one parameter and return one parameter
def Demo3(No):
    print("Inside Demo3 with Argument  ",No)
    return No+2 

#Function Accpets two parameter and return one parameter 
def Demo4(No1,No2):
    print("Inside Demo4")
    Add=No1+No2
    return Add

#Function accepte two parameter and return two parameter 
def Demo5(No1,No2):
    print("Inside Demo5")
    Add=No1+No2
    Sub=No1-No2
    return Add,Sub

#Main Function.
def main():
    Demo1()
    
    Demo2(11)

    Ans=Demo3(10)
    print("Return Value of Demo3 is :",Ans)

    Ans=Demo4(10,11)
    print("Return value  is :",Ans)

    Ans1,Ans2=Demo5(11,10)
    print("First retun valu:",Ans1)
    print("Second return value:",Ans2)


#Starter    
if __name__=="__main__":           #__name__ is a special variable
    main()