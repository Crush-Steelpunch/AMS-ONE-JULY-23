# Goal: “Create a Budget class that can instantiate objects based on
# different budget categories like food, clothing, and entertainment.
# These objects should allow for depositing and withdrawing funds 
# from each category, as well computing category balances 
# and transferring balance amounts between categories”

# decomposition - breaking down a complex problem or system into smaller, more manageable parts
# pattern recognition – looking for similarities among and within problems
# abstraction – focusing on the important information only, ignoring irrelevant detail
# algorithms - developing a step-by-step solution to the problem, or the rules to follow to solve the problem


# 1. Write a class, call it Budget
# 2. Depositing         
# 3. Withdrawing
# 4. Balance Storage
# 5. Transfering

# Pattern Recognition
# Depositng and withdrawing are maths problems, adding and subtracting
# Transfering is both adding and subtracting

# Algorithms

# 1. Write a class
# 2. Three functions for Dep, With & Transfering
# 3. attribute
# 4. attribute should be set up with an __init__ function


class Budget:
    def __init__(self, startbalance):
        self.balance = startbalance

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def transfer(self, amount, otherobject):
        self.withdraw(amount)
        otherobject.deposit(amount)

    
food = Budget(20)
clothing = Budget(200)
entertainment = Budget(90)
breakpoint()

food.withdraw(5)
print(food.balance)
food.deposit(5)
print(food.balance)
print(clothing.balance)
food.transfer(20,clothing)

print(food.balance)
print(clothing.balance)
    
        



