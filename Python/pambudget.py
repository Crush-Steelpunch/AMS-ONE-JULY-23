# Goal: “Create a Budget class that can instantiate objects based on 
# different budget categories like food, clothing, and entertainment. These objects should allow for depositing and withdrawing funds from each category, as well computing category balances and transferring balance amounts between categories”
# Written by Pamela Swiderska

class Budget:

    def __init__(self, funds):
        self.funds = float(funds)

    def print_balance(self):
        return self.funds
    
    def withdrawing(self, amount):
        self.funds=float(self.funds) - float(amount)
        return self.funds
    
    def depositing(self, amount):
        self.funds=float(self.funds) + float(amount)
        return self.funds

    def transferring(self, target_budget, amount):
        if amount < self.funds:
            self.withdrawing(amount)
            target_budget.depositing(amount)
            return self.funds
    
food = Budget(100)
clothing = Budget(100)
entertainment = Budget( 100)


breakpoint()

# testing
# print(f"clothing balance: {clothing.print_balance()}")
# print(clothing.withdrawing(20))
# print(clothing.depositing(60))
print(food.transferring(clothing,30))
# print(clothing.funds)

