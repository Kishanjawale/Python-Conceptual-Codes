from re import S


def Add(*Values):
    print(type(Values))
    print("Number of arguments are:",len(Values))
    
    sum=0
    for no in Values:
        sum=sum+no
    return sum


def main():
    Ans=Add(10,11,1,232,4343,54,4)
    print("Addition is :",Ans)

if __name__=="__main__":
    main()