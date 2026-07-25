class account:
    def __init__(self, account_id, account_name, account_type, balance, branch_name, ifsc_code):
        self.account_id = account_id
        self.account_name = account_name
        self.account_type = account_type
        self.balance = balance
        self.branch_name = branch_name
        self.ifsc_code = ifsc_code
    
    def account_details(self):
        print("------------account details are displayed---------------")
        print(f"account_id is {self.account_id}")
        print(f"account_name is {self.account_name}")
        print(f"account_type is {self.account_type}")
        print(f"balance is {self.balance}")
        print(f"branch_name is {self.branch_name}")
        print(f"ifsc_code is {self.ifsc_code}")
        print("--------account details are displayed successfully--------")