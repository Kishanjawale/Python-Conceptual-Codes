#Pi= 3.14     is a defalut Argument 
def Area(Radius,Pi=3.14):
    Result=(Pi*(Radius*Radius))
    return Result


def main():
    Rvalue=10.5
    PIvalue=3.14

#Using Positional Arguments.
    Ans=Area(Rvalue,PIvalue)    # Internally it will be called as : Ans= Area(10.5,3.14)   
    print("Area of circle is :",Ans)


#Using Keyword Argument.
    Ans=Area(Pi=PIvalue,Radius= Rvalue)   # Internally it will be called as : Ans = Area(PIvalue=3.14,Rvalue=10.5) 
    print("Area of circle is :",Ans)


#Using Defalut Argument 
    Ans=Area(10.5)   # Internally it will be called as : Ans = Area(Radius=10.5) 
    print("Area of circle is :",Ans)



#Using keyword and Default Argument at one time
    Ans=Area(Radius=10.5)   # Internally it will be called as : Ans = Area(Radius=10.5) 
    print("Area of circle is :",Ans)

# Using Keyword argument ...which replaced radius 3.14 to 7.10
    Ans=Area(Pi=7.10,Radius=10.5) 
    print("Area of circle is :",Ans)


if __name__ == "__main__":
    main()