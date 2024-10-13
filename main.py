from bank import Bank
from person import Users, Admins

bank = Bank('Bangladesh Krishi Bank')

def user_interface():
	name = input('\tEnter Your Name: ')
	email = input('\tEnter Your Email: ')
	address = input('\tEnter Your Address: ')
	account_type = input('\tAccount Type: Savings/Current: ')
	user = Users(name, email, address, account_type)
	print(f'\n\tWelcome Mr. {user.name} to {bank.name}!\n')
    
	while True:
		print(f'\tDear {user.name}, Please choose your options!\n')
		print('\t\tOption 1 : Create Account')
		print('\t\tOption 2 : Deposit Money')
		print('\t\tOption 3 : Withdraw Money')
		print('\t\tOption 4 : Check Available Balance')
		print('\t\tOption 5 : View Transaction History')
		print('\t\tOption 6 : Take Loan')
		print('\t\tOption 7 : Transfer Money')
		print('\t\tOption 8 : Exit\n')
		choice = int(input('\tPlease Enter Your Option: '))
        
		if choice == 1:
			user.create_account(bank)
		elif choice == 2:
			amount = int(input('\tPlease Enter Your Amount to Deposit: '))
			user.deposit_cash(bank, amount)
		elif choice == 3:
			amount = int(input('\tPlease Enter Your Amount to Withdraw: '))
			user.withdraw_cash(bank, amount)
		elif choice == 4:
			user.show_balance()
		elif choice == 5:
			user.show_transaction_history()
		elif choice == 6:
			amount = int(input('\tPlease Enter Your Amount to Borrow: '))
			user.take_loan(bank, amount)    
		elif choice == 7:
			amount = int(input('\tPlease Enter Your Amount to Transfer: '))
			account_number = int(input('\tPlease Enter Receiver Account Number: '))
			user.transfer_money(bank, amount, account_number)
		elif choice == 8:
			break        
		else:
			print('\tInvalid Entry!\n')

def admin_interface():
	name = input('\tEnter Your Name: ')
	email = input('\tEnter Your Email: ')
	address = input('\tEnter Your Address: ')
	admin = Admins(name, email, address)
	print(f'\n\tWelcome Mr. {admin.name} to {bank.name}!\n')
    
	while True:
		print(f'\tDear {admin.name}, Please choose your options!\n')
		print('\t\tOption 1 : Create Account')
		print('\t\tOption 2 : Delete Account')
		print('\t\tOption 3 : Show Accounts List')
		print('\t\tOption 4 : Check Vault Money')
		print('\t\tOption 5 : Show Total Loan Amount')
		print('\t\tOption 6 : Enable Loan Feature')
		print('\t\tOption 7 : Disable Loan Feature')
		print('\t\tOption 8 : Exit\n')
		choice = int(input('\tPlease Enter Your Option: '))
        
		if choice == 1:
			admin.create_account(bank)
		elif choice == 2:
			account_number = int(input('\tPlease Enter Your Desired Account Number: '))
			admin.delete_user_account(bank, account_number)
		elif choice == 3:
			admin.show_accounts(bank)
		elif choice == 4:
			admin.show_vault(bank)
		elif choice == 5:
			admin.show_loan(bank)
		elif choice == 6:
			admin.enable_loan(bank)    
		elif choice == 7:
			admin.disable_loan(bank)
		elif choice == 8:
			break        
		else:
			print('\tInvalid Entry!\n')

while True:
	print(f'\nWelcome to {bank.name}!\n')
	print('\tChoose Your Status:\n')
	print('\t\t1. Customer')
	print('\t\t2. Admin')
	print('\t\t3. Exit\n')
	option = int(input('\tEnter Your Option: '))
    
	if option == 1:
		user_interface()
	elif option == 2:
		admin_interface()
	elif option == 3:
		break
	else:
		print('\tInvalid Input!\n')


