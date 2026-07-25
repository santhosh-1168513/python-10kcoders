class customer:
    def __init__(self, c_id, c_name, c_age, c_gender,
                 c_address, c_phone, c_email):
        self.c_id = c_id
        self.c_name = c_name
        self.c_age = c_age
        self.c_gender = c_gender
        self.c_address = c_address
        self.c_phone = c_phone
        self.c_email = c_email
    
    def customer_details(self):
        print("------------customer details are displayed---------------")
        print(f"customer_id is {self.c_id}")
        print(f"customer_name is {self.c_name}")
        print(f"customer_age is {self.c_age}")
        print(f"customer_gender is {self.c_gender}")
        print(f"customer_address is {self.c_address}")
        print(f"customer_phone is {self.c_phone}")
        print(f"customer_email is {self.c_email}")
        print("--------customer details are displayed successfully--------")