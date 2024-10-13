class Bank:
    def __init__(self,name) -> None:
        self.name = name
        self.user_list = {}
        self.admin_list = {}
        self.vault = 0
        self.total_loan = 0
        self.loan_enabled = True

