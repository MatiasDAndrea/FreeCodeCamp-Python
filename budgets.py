##########################################################################################################################################
#
#    budgets:It should be able to instantiate objects based
#    on different budget categories like food, clothing, and entertainment. 
#    When objects are created, they are passed in the name of the category.
#    The class should have an instance variable called ledger that is a list
#
#   Class:
#       Category:
#           Methods:
#               -deposit(amount,reason) : A deposit method that accepts an amount and description.
#                   If no description is given, it should default to an empty string.
#                   The method should append an object to the ledger list in the
#                   form of {"amount": amount, "description": description}.
#
#               -withdraw(amount,reason) : A withdraw method that is similar to the deposit method,
#                    but the amount passed in should be stored in the ledger as a negative number.
#                   If there are not enough funds, nothing should be added to the ledger.
#                   This method should return True if the withdrawal took place, and False otherwise.
#               -get_balance():A get_balance method that returns the current balance of the budget category
#                   based on the deposits and withdrawals that have occurred.
#
#               -transfer(amount,account): A transfer method that accepts an amount and another budget category as arguments.
#                    The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
#                    The method should then add a deposit to the other budget category with the amount and the description "Transfer
#                    from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers.
#                    This method should return True if the transfer took place, and False otherwise.
#
#               -check_funds(amount):A check_funds method that accepts an amount as an argument.
#                    It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
#                    This method should be used by both the withdraw method and transfer method.
#
#   Function: create_spend_chart(list)
#       -Takes a list of categories as an argument. It should return a string that is a bar chart.
#
##########################################################################################################################################

import re

class Category:

    def __init__(self,cat):
        self.name    = cat
        self.ledger  = []
        self.balance = 0
        self.depo    = 0


    def __str__(self):
        
        title_len = 30
        multiplier = (title_len - len(self.name))// 2
        
        title = f"{'*'*multiplier}{self.name}{'*'*multiplier}\n"

        deposit_spaces = title_len - len("initial deposit") - len(str(self.depo))
        body = f"initial deposit{' '*deposit_spaces}{self.depo}\n"

        for x in self.ledger:

            amount      = str(x["amount"])
            description = x["description"]
            spaces = title_len - len(amount) - len(description)

            if int(amount) < 0:

                body += f"{description}{' '*spaces}{amount}\n"

        body += f"Total:{self.balance}"

        return title + body


    def deposit(self,amount,description = ""):
        
        obj = {
            "amount":amount,
            "description":description
        }
        self.balance += amount
        self.depo    += amount
        self.ledger.append(obj)


    def withdraw(self,amount,description=""):

        if self.check_funds(amount):
            obj = {
                "amount":-amount,
                "description":description
            }
            self.balance -= amount
            self.ledger.append(obj)
            return True
        
        else:
            return False


    def get_balance(self):
        
        return self.balance


    def transfer(self,amount,obj):
        
        if self.check_funds(amount):

            self.withdraw(amount,f"Transfer to {obj.name}")
            obj.deposit(amount,f"Transfer from {self.name}")
            return True
        else:
            return False


    def check_funds(self,amount):
        
        if self.balance - amount >=0:
            return True

        else:
            return False


def create_spend_chart(lists=[]):
    
    output_list = []
    total_spent = 0
    for x in lists:
        name   = x.name
        ledger = x.ledger
        money_spent = 0

        for y in ledger: 
            if y["amount"] < 0:
                money_spent += y["amount"]
           
        output_list.append([name,money_spent])
        total_spent += money_spent
    
    number_categories = len(output_list)
    body = ""
    line = ""


    for num in range(100,-10,-10):

        cat = ""
        for _,money_spent in output_list:

            cat += " o " if (money_spent/total_spent)*-100 <= -num else "   "

        spaces = 3-len(str(num))
        line += f"{' '*spaces}{num}|{cat}\n"

    #############
    # FooterLine.
    footer_space = 4*' '
    slash_space  = "-"*(number_categories*3 + 1)
    footer = f"{footer_space}{slash_space}\n"

    ##########
    # Names

    decode_name_list = []

    for name,_ in output_list:

        decode_name_list.append(list(name.capitalize()))

    max_letters = max([len(x) for x in decode_name_list])
    result_str = ""

    for index in range(max_letters):

        cat_names = "    "
        for word in decode_name_list:

            if len(word)>0:
                letter = word.pop(0)

            else:
                letter = " "

            cat_names += f" {letter} "

        result_str += f"{cat_names}\n"

    print(f"{line}{footer}{result_str}")



########
# Tests.
food = Category("food")
food.deposit(500,"Deposit")
food.deposit(200,"deposit")
food.deposit(400)
food.withdraw(400,"Apples")
food.withdraw(250,"Oranges")
food.withdraw(150,"Tomatoes")
print(food)

games = Category("games")
games.deposit(500,"Game Deposit")
games.deposit(200,"Game Deposit")
games.deposit(400)
games.withdraw(400,"GTA V")
games.withdraw(250,"Call of Duty")
games.withdraw(150,"Burnout Paradise")
games.transfer(50,food)
print(games)

market = Category("market")
market.deposit(5000,"Deposit")
market.deposit(200,"Deposit")
market.deposit(400)
market.withdraw(400,"Electrical Equipment")
market.withdraw(2500,"Microwave")
market.withdraw(1500,"Vegetables")
market.transfer(50,food)
print(market)


create_spend_chart([food,games,market])
