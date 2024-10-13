from abc import ABC
from bank import Bank
from datetime import datetime
class Persons(ABC):
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address
class Users(Persons): 
    def __init__(self, name, email, address, account_type) -> None:
        super().__init__(name, email, address)
        self.account_type = account_type
        self.balance = 0
        self.transaction_history = []
        self.account_number = None
        self.loan_number =0

    def create_account(self, bank):
        if self.account_type.lower() == 'savings':
            self.account_number = 10001+len(bank.user_list)
        else:
            self.account_number = 20001+len(bank.user_list)
        bank.user_list[self.name] = self
        print(f'\t\tDear {self.name}, Congratulations! Your account with no {self.account_number} is created successfully!')

    def deposit_cash(self,bank,amount):
        if amount > 0:
            self.balance+=amount
            bank.vault+=amount
            self.transaction_history.append(f'Credit TK. {amount} at {datetime.now().strftime('%Y-%m-%d')}')
            print(f'\t\tTk {amount} has been deposited to your {self.account_type} account number {self.account_number}')
        else:
            print('\t\tInsufficiant amount to deposit!')

    def withdraw_cash(self, bank,amount):
        if amount<self.balance and amount < bank.vault:
            self.balance-= amount
            bank.vault-=amount
            self.transaction_history.append(f'\t\tDebit TK. {amount} at {datetime.now().strftime('%Y-%m-%d')}')
            print(f'\t\tTk {amount} has been debitted from your {self.account_type} account number {self.account_number}')
        elif amount> bank.vault and amount < self.balance:
            print('\t\tSorry! This bank is bankrupt!')    
        else:
            print(f'\t\tInsufficient balance to withdraw Tk {amount} from your account {self.account_number}') 

    def show_balance(self):
        print(f'\t\tDear {self.name}! Your current balance is Tk.{self.balance}')

    def show_transaction_history(self):
        print(f'\t\tTransaction History of Mr {self.name}:')
        for transaction in self.transaction_history:
            print(f'\t\t{transaction}') 

    def take_loan(self, bank, amount):
        if not bank.loan_enabled:
            print('\t\tLoan feature of this bank is currently off now!')
            return
        else:    
            if self.loan_number<2 and amount<bank.vault:
                bank.vault-=amount
                bank.total_loan+=amount
                self.loan_number+=1
                print(f'\t\tTk. {amount} has been given as cash to {self.name} as loan!')
            else:
                print('\t\tYou have already taken loan two times!')

    def transfer_money(self, bank, amount, account_number):
        receiver = None
        for user in bank.user_list.values():
            if user.account_number == account_number:
                receiver = user
                break
        if receiver:
            if amount <= self.balance:
                self.balance-= amount
                receiver.balance+= amount
                self.transaction_history.append(f'Tk {amount} has been transferred to  {receiver.account_number}')
                print(f'\t\tTk {amount} has been transferred from {self.account_number} to {receiver.account_number}')
        else:
            print('\t\tYour desired account number does not exist!')

class Admins(Persons):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)

    def create_account(self,bank):
        bank.admin_list[self.name] = self
        print(f'\t\tDear {self.name}, Congratulations! Your admin account has been created successfully!') 

    def delete_user_account(self, bank, user_account_number):
        for name, user in list(bank.user_list.items()):
            if user.account_number == user_account_number:
                del bank.user_list[name]
                print(f"\t\tUser with account number {user_account_number} has been deleted.")
                return
        print(f"\t\tNo user found with account number {user_account_number}.")                                                                   

    def show_accounts(self,bank):
        for item in bank.user_list.values():
            print(f'\t\tAccount Name: {item.name}, Account Number : {item.account_number}, Available Balance: {item.balance}') 
    def show_vault(self,bank):
        print(f'\t\tAvailable Taka in the vault of the bank is {bank.vault}') 
    def show_loan(self,bank):
        print(f'\t\tTotal given loan amount of the bank is {bank.total_loan}')  

    def enable_loan(self,bank):
        bank.loan_enabled = True
        print(f'\t\tLoan feature of the bank is on now!')

    def disable_loan(self,bank):
        bank.loan_enabled = False
        print(f'\t\tLoan feature of the bank is off now!') 

# bank = Bank('SIBL')
# user1 = Users('Lokman', 'munna@gmail.com','Mirpur', 'savings')
# user2 = Users('Hosen', 'hosen@gmail.com','Shewrapara', 'current')
# user3 = Users('Noman', 'tanna@gmail.com','Noakhali', 'savings')
# user4 = Users('Toman', 'kanna@gmail.com','Patuakhali', 'savings') 
# user1.create_account(bank)
# user2.create_account(bank)
# user3.create_account(bank)
# user4.create_account(bank) 
# user1.deposit_cash(bank,5000)                   
# user2.deposit_cash(bank,56000)                   
# user3.deposit_cash(bank,10000)
# user1.withdraw_cash(bank,6000)                   
# user2.withdraw_cash(bank,6000)
# user1.show_balance()
# user2.show_balance()
# user3.show_balance()
# user2.show_transaction_history()
# user2.take_loan(bank,500) 
# user1.transfer_money(bank,100,20002)
# admin = Admins('Lokman', 'shohagh@gmail.com', 'Mirpur')
# admin.create_account(bank)
# print(admin.address) 
# admin.show_accounts(bank)
# admin.show_vault(bank)
# admin.show_loan(bank)
# admin.disable_loan(bank)
# user2.take_loan(bank,500) 
          