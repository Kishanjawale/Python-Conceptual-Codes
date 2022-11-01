#This application demonstrate  all the concept of Object Oriented Programming
#using the Banking class

#Class Bank_Account
from __future__ import print_function
from cgi import print_arguments


class Bank_Account:

    Bank_Name ="HDFC BANK PVT LTD"
    ROI_On_FD= 6.7

    #Constructor
    def __init__(self):
        self.Name = ""
        self.Ammount= 0.0
        self.Account_Number=0
        self.Address=""
    
    def Create_Account(self):
        print("Enter Your Name:")
        self.Name=input()
        
        print("Enter Your Account Number:")
        self.Account_Number=int(input())
        
        print("Enter Your Initial Ammount:")
        self.Ammount=input()

        print("Enter Your Address:")
        self.Address=input()

    #Display Account Detail Method
    def Display_Account_Details(self):
        print("************Account Details************")
        
        print("Name of Account Holder  :",self.Name)

        print("Account Number :",self.Account_Number)
        
        print("Current Amount in Account :",self.Ammount)
        
        print("Address of Account Holder  :",self.Address)
        
        print("****************************************")    

    
    def Display_Rate_Of_Interest(self):
        print("Rate Of Interest is ",Bank_Account.ROI_On_FD)

    
    @classmethod
    def Display_Bank_information(cls):
        print("Welcome To Banking Console")
        print("Name of our bank is :",cls.Bank_Name)
        print("Rate Of Interest we offfer on fixed Deposite is :",cls.ROI_On_FD)

    @staticmethod
    def Display_KYC():
        print("Please Consider Below KYC Information")
        print("According to the rules of Government of India You have to submit Below Document")
        print("1 : Clear and Recent Passport Size Photo")
        print("2 : Photo Of Aadhar Card")
        print("3 : Photo Of PAN Card")
        

    def Withdraw(self,Value):
        self.Ammount = self.Ammount - Value
        
    def Deposite(self,Value):
        self.Ammount=self.Ammount+ Value


#Main Method
def main(): 
    #Calling Class Methods without Creating Object 
    Bank_Account.Display_KYC()
    Bank_Account.Display_Bank_information()
    
    #Creating object of Bank_Account Class
    User1=Bank_Account()
    User2=Bank_Account()
    
    print("------------------------------------------")
    print("Creating The First Account:")
    User1.Create_Account()    

    print("------------------------------------------")
    print("Creating The Second Account:")
    User2.Create_Account()

    User1.Display_Account_Details()    
    User2.Display_Account_Details()
    
    User1.Deposite(1500)
    User2.Deposite(1111)

    print("Ammount of User1 After Deposite:",User1.Ammount)
    print("Ammount of User2 After Deposite:",User2.Ammount)



    User1.Withdraw(int(1000))
    User2.Withdraw(int(500))

    print("Ammount of User1 After Withdrawal:",User1.Ammount)    
    print("Ammount of User2 After Withdrawal:",User2.Ammount)


#Starter
if __name__=="__main__":
    main()