from data.models.account import Account
from data.repositories.bank_repository import bank_repo


class bank_repo_impl(bank_repo):
    def find(self, cardNumber) -> Account:
        pass

    def number_of_accounts(self) -> int:
        pass
