#!/usr/bin/env python
# coding: utf-8

# In[14]:


# create a class
# syntax for class
"""syntax:- class ClassName:  #pascal case 
            statement1
            statement2
            statement3
                .
                .
                .
                .
            statement N-1 
            statement N"""

class SampleClass:
    attribute1 = 10
    attribute2 = 20
    
object1 = SampleClass()
object2 = SampleClass()
object3 = SampleClass()

print(object1.attribute1)
print(object2.attribute1)
print(object3.attribute1)
print(object1.attribute2)
print(object2.attribute2)
print(object3.attribute2)

object1.attribute1 = 100
print(object1.attribute1)
print(object2.attribute1)

print(object3.attribute1)
object2.attribute1 = 200

print(object2.attribute1)


# In[17]:


print(object1.attribute1)
print(object2.attribute1)
print(object3.attribute1)


# In[18]:


# how to create a method

class SampleClass1:
    def SampleMethod(self):
        print("Method created successfully")

newobject1 = SampleClass1()

# accessing the method using class 
newobject1.SampleMethod()


# In[2]:


class check_number:
    attribute1 = 20
    attribute2 = 30
    
objet_n1 = check_number
objet_n2 = check_number
print(objet_n1.attribute1)
print(objet_n2.attribute2)


# In[12]:





# #### create a bank account program :
# 

# In[16]:


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




