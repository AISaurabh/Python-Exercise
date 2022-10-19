#Example No. 1
class Bank_Account:
    def __init__(self,Name_of_the_Depositor,Account_Number,Type_of_Account,Balance_Amount):
        self.Name_of_the_Depositor = Name_of_the_Depositor
        self.Account_Number = Account_Number
        self.Type_of_Account = Type_of_Account
        self.Balance_Amount = Balance_Amount
    def Deposit(self,Amount_Added):
        self.Amount_Added = Amount_Added
        self.Added = self.Balance_Amount + self.Amount_Added
        print("The available balance is :", self.Added)
    def Withdrawal(self,Amount_Withdrawal):
        self.Amount_Withdrawal = Amount_Withdrawal
        if (self.Amount_Withdrawal > self.Balance_Amount):
            print("Sorry!Insufficient funds to withdrawal")
            return
        self.Withdrawal = self.Added - self.Amount_Withdrawal
        print("The available balance is :", self.Withdrawal)
    def Display(self):
        print(self.Name_of_the_Depositor)
        print(self.Withdrawal)
Name_of_the_Depositor = input("Enter the name of depositor :")
Account_Number = input("Enter the account number :")
Type_of_Account = input("Enter the type of account :")
Balance_Amount =int(input("Enter the balance amount :"))
B = Bank_Account(Name_of_the_Depositor,Account_Number,Type_of_Account,Balance_Amount)
print("1.New customer","\n","2.Deposit","\n","3.Withdrawal","\n","4.Display","\n","5.Exit")
x=0
while x!=5:
    x=int(input("Enter your choice :"))
    if x==1:
        print("Welcome!",B.Name_of_the_Depositor,"\n",B.Account_Number,"\n",B.Type_of_Account)
    elif x==2:
        Amount_Added = int(input("Enter the deposite amount :"))
        B.Deposit(Amount_Added)
    elif x==3:
        Amount_Withdrawal = int(input("Enter the withdrawal amount :"))
        B. Withdrawal(Amount_Withdrawal)
    elif x==4:
        B.Display()
else:
    print("Thank you!",B.Name_of_the_Depositor,"for banking with us!","\n"," EXIT ")
        
        
        
        
        
