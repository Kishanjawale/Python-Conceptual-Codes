#This application is to demonostrate accepting 
#the elements from the user and intert into the list

def main():  
    
    Arr=list()          #created an empty list by creating the object of list class
    
    print("Enter the  number of element:") #Accepting the size of list from user
    size =int(input())                         
    
    print("please enter the values") #accepting the values form user 
    
    for i in range (0,size):
        no = int(input()) 
        Arr.append(no)         #Arr.insert(i,no)  ..Another way to do Same task
    
    print(Arr)     #Displaying the List


if __name__ == "__main__" :     #starter
    main()