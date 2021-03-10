'''

Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have?

'''

class Bank:
	def __init__(self,name,age,address,bank_account):
		self.name=name
		self.age=age
		self.address=address
		self.bank_account=bank_account

	def names(self):
		return f'My name is {self.name}'

	def bank_accounts(self):
		return f'My Bank account number is {self.bank_account}'

bank = Bank('Sagar','22','Kathmandu','1587952636952401')
print(bank.names)
print(bank.age)
print(bank.address)
print(bank.bank_account)

print(bank.names())
print(bank.bank_accounts())