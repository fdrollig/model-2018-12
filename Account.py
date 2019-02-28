class Account:
    ACCOUNTS_RECEIVABLE = "Accounts Receivable" # Other people's debts to me
    ACCOUNTS_PAYABLE = "Accounts payable" # My debts
    CASH = "Cash"
    def __init__(self, name):
        self.creditTxs = []
        self.debitTxs = []
        self.name = name
    def enterCredit(self, tx):
        self.creditTxs.append(tx)
    def enterDebit(self, tx):
        self.debitTxs.append(tx)
