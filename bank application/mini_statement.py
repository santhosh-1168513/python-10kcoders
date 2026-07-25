class Statement:
    def __init__(self):
        self.statement = []

    def add_transaction(self, transaction):
        self.statement.append(transaction)
    
    def display_statement(self):
        print("------------mini statement is displayed---------------")
        for transaction in self.statement:
            print(transaction)
        print("--------mini statement is displayed successfully--------")
        if len(self.statement) == 0:
            print("No transactions found.")
        else:
            for transaction in self.statement:
                print(transaction)
        print("--------mini statement is displayed successfully--------")
