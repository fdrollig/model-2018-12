from Inventory import Inventory

class Location:
    B2B_COMPANY = "B2B Company"
    B2C_COMPANY = "B2C Company"
    B2B_WORKER = "B2B worker"
    B2C_WORKER = "B2C worker"
    FS = "Financial System"
    B2B_MARKET = "B2B Market"
    B2C_MARKET = "B2C Market"
        
    def __init__(self, name):
        self.objects = []
        self.name = name
        self.accounts = []
        self.inventory = Inventory()
    def __str__(self):
        return self.name
    def __lt__(self, other):
        return self.name < other.name
