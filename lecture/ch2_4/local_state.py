def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Balance is not enough!"
        balance = balance - amount
        return balance

    return withdraw
