try:
    result=10/0    #Exception prone Code 

#Handling a specific exception.
except ZeroDivisionError as e:
    print(f"Error:{e}")

#For Handling a generic Exception
except Exception as e:
    print(f"Unexpected Error Occured:{e}")

#Code which will execute if no exception is raised
else:
    print("No Excpetion Occured")

#Code to be executed reagardless of whether an exception is occured or not
finally:
    print("Fianlly Block:This is always executed")