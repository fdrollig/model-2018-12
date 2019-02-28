class Resource:
    B2B_PRODUCT = "B2B Product"
    B2C_PRODUCT = "B2C Product"
    WAGES_B2B = "Wages for B2B Product"
    WAGES_B2C = "Wages for B2C Product"
    MONEY_FOR_B2B_PRODUCT = "Money for B2B product"
    MONEY_FOR_B2C_PRODUCT = "Money for B2C product"
    B2B_LOAN = "B2B Loan"
    B2C_LOAN = "B2C Loan"
    B2B_LOAN_PAYBACK = "Replayment of B2B loan"
    B2C_LOAN_PAYBACK = "Replayment of B2C loan"
    def __init__(self, name):
        self.name = name
        self.amounts = []
    def findByName(self, lst, name):
        print("findByName: " + name)
        iterator = filter(lambda elem: elem.name == name, lst)
        return next(iterator)

    def addAmount(self, amount):
        try:
            existingAmount = self.findByName(self.amounts, amount.name)
            existingAmount.add(amount)
        except StopIteration:
            self.amounts.append(amount)
    def __str__(self):
        return self.name

