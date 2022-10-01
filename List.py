#This application demonstarate the concept of List
print("Program to demonstrate the concept of list ")


def main():
    list1=[11,21,51,101]   #Creating a List 

    print("Elements in the list are:",list1)
    print( "Type of List is :",type(list1))
    print("Lenghth of List1 ",len(list1))

  
  #Accessing the element of the list using index 
  
    print(list1[0])
    print(list1[1])
    print(list1[2])
    print(list1[3])

    list1.append(151)         #insert element in list at the end  
    print(list1)    

    list1.remove(51)          #Remove a specific element from list
    print(list1)
    
    print(type(list1[1]))     #Print the datatypes of Specific elements from the list  

    list1.append(19.89)       #inserting heterogeneous element in list
    print(list1)

    
    list1.insert(2,111)      #inserting element at a specific position.
                             #insert(Index_position , value_to_be_inserted)
    print(list1)


if __name__ == "__main__":   #starter
    main()

