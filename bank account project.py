### BankAccount creation project

#1.create a customer details 
#2.display customer details
#3.Deposti money
#4.withdraw money
#5.check balance 


# In[27]:


# creating customer details with class:
class BankAccoount:
    def __init__(self,AccountName,AccoutNumber,IFSC,Balance):
        self.AccountName  = AccountName
        self.AccoutNumber = AccoutNumber
        self.IFSC         = IFSC
        self.Balance      = Balance
    def Deposit(self,Amount):
        self.Balance += Amount
    def withdraw(self,Amount):
        self.Balance -= Amount
    def checkBalance(self):
        print(self.Balance)
    
customer1 = BankAccoount("Vamsiram",33243484116,"SBIN0001901",1000)
customer2 = BankAccoount("pavankumar",59251011001306,"SBIN0001901",10000)

customer1.checkBalance()
customer1.Deposit(2000)

customer1.checkBalance()

customer1.withdraw(350)
customer1.checkBalance()



# In[ ]:





# In[ ]:




