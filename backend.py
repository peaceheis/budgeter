import uuid
import json


class Account:

    def __init__(self, name, balance):
        self.id = str(uuid.uuid4())
        self.balance = balance
        self.name = name
        self.history = []

    def add_transaction(self, date: int, money_in: bool, amount: int):
        if money_in:
            running_balance = self.balance + amount
            self.balance += amount
        else:
            running_balance = self.balance - amount
            self.balance -= amount
        transaction = {"id": str(uuid.uuid4()), "date": date, "money_in": money_in, "amount": amount,
                       "running_balance": running_balance}
        self.history.append(transaction)

    def __dict__(self):
        account = dict( account_id=self.id, balance=self.balance, history=self.history)
        return account

    def __repr__(self, provide_history=False):
        string = f"Account \"{self.name}\" has a balance of ${self.balance}.\n"
        if provide_history:
            new_string = f"History of {self.name}:"
            for transaction in self.history:
                new_string += f"\nAt time {transaction['date']}, ${transaction['amount']} was "
                if transaction['money_in']:
                    new_string += "deposited into "
                else:
                    new_string += "withdrawn from "
                new_string += f"the account, leaving a balance of ${transaction['running_balance']}."
            string += new_string
        return string

    def write(self, file):
        with open(file, 'w') as account:
            json.dump(self.__dict__(), account, indent="    ")


test = Account("Checking", 0)
test.add_transaction(412, True, 430)
test.add_transaction(200, False, 200)
test.write("test.json")
# print(people)
# print(type(people))
# to_json = json.dumps(people)
# print(to_json)
# print(type(to_json))
