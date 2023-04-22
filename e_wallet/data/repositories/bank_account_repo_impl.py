import random

import self as self

from data.models import account
from data.models.account import Account
from data.models.credit_card import CreditCard
from data.repositories.bank_account_repository import Bank_account_repo


class account_repo_impl(Bank_account_repo):

    def __init__(self):
        self.__bank_account = Account()
        self.__accounts: list[Account] = []
        self.count = 0

    def save(self, bank_account: Account):
        credit_not_saved = bank_account.get_id() == 0
        if credit_not_saved:
            bank_account.set_id(self.count + 1)
            self.__accounts.append(bank_account)
            self.count += 1
        return bank_account

    def find(self, id):
        for i in self.__accounts:
            if i.get_id() == id:
                return i
