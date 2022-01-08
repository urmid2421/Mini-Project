#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Account:
    def __init__(self,acnt_no,opening_deposit):
        self.acnt_no = acnt_no
        self.balance=opening_deposit
    def __str__(self):
        return f'${self.balance:.2f}'
    def deposit(self,dep_amt):
        self.balance+=dep_amt
    def withdraw(self,wd_amt):
        if self.balance>=wd_amt:
            self.balance-=wd_amt
        else:
            return 'Funds unavailable'

class Savings(Account):
    def __init__(self,acnt_no,opening_deposit):
        super().__init__(acnt_no,opening_deposit)
    def __str__(self):
        return f'Savings Account' #{self.acct_nbr}\nBalance: {Account.__str__(self)}'


class Checking(Account):
    def __init__(self,acnt_no,opening_deposit):
        super().__init__(acnt_no,opening_deposit)
    def __str__(self):
        return f'Checking Account' #{self.acnt_no}\nBalance:{Account.__str__(self)}


# In[ ]:





# In[ ]:





# In[ ]:




