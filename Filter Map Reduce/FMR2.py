#
def CheckEven(No):
    return (No % 2 == 0 )

def FilterX(Helper_Function,Data):
    Result=[]
    for No in Data:
        if  (Helper_Function(No)== True):
            Result.append(No)
    return Result

def main():
    print("Enter the number of elements you want to enter:")
    isize=int(input())
    Data_input = []
    
    print("Please Enter the data:")
    for icnt in range(0,isize,1):
        Value=int(input())
        Data_input.append(Value)
    

    print("Data is :",Data_input)

    Data_Filter=FilterX(CheckEven,Data_input)

    print("Data After Filter is :",Data_Filter)

    
#Starter
if __name__=="__main__":
    main()