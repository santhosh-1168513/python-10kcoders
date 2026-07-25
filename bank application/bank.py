class bank:
    def __init__(self, bankid, bankname, branchmanger, ifsccode, bankaddress, 
                 bankcontact):
        self.bankid = bankid
        self.bankname = bankname
        self.branchmanger = branchmanger
        self.ifsccode = ifsccode
        self.bankaddress = bankaddress
        self.bankcontact = bankcontact
    
    def bank_details(self):
        print("------------bank details are displayed---------------")
        print(f"bank_id is {self.bankid}")
        print(f"bank_name is {self.bankname}")
        print(f"branch_manager is {self.branchmanger}")
        print(f"ifsc_code is {self.ifsccode}")
        print(f"bank_address is {self.bankaddress}")
        print(f"bank_contact is {self.bankcontact}")
        print("--------bank details are displayed successfully--------")