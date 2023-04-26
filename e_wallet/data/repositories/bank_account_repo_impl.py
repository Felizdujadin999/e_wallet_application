from data.models.account import Account
from data.repositories.bank_account_repository import Bank_account_repo


class account_repo_impl(Bank_account_repo):

    def __init__(self):
        self.__bank_account = Account
        self.__accounts: list[Account] = []
        self.count = 0

    def save(self, bank_account: Account):
        bank_account.set_id(self.count + 1)
        self.__accounts.append(bank_account)
        self.count = self.count + 1
        return bank_account

    def find(self, id):
        for i in self.__accounts:
            if i.get_id() == id:
                return i

    def number_of_account(self):
        return self.count

    def find_by_account_number(self, account_number):
        for i in self.__accounts:
            if i.get_acc_numbers() == account_number:
                return i
            else:
                return "Account does not exit"
