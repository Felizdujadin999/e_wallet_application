import random

from data.repositories.bank_account_repository import Bank_account_repo
from dtos.requests.register_bank_account_request import register_bank_request
from services.bank_service import Bank_service


class bank_service_impl(Bank_service):

    def __init__(self):
        self.__bank_account = Bank_account_repo
        self.__acc_numbers: list[int] = []
        self.__cvv: list[int] = []
        self.__card_numbers: list[int] = []
        self.account_number = 0
        self.card_number = 0
        self.cvv = 0

    def create_account(self: register_bank_request):

        pass

    def withdrawal(self, amount, password):
        pass

    def transfer(self, amount, password):
        pass

    def check_balance(self):
        pass

    def validate_acc_num(self, account_numbers) -> bool:
        for i in self.__acc_numbers:
            if i == account_numbers:
                return True
            return False

    def validate_card_num(self, card_numbers) -> bool:
        for i in self.__card_numbers:
            if i == card_numbers:
                return True
            return False

    def validate_cvv(self, cvv) -> bool:
        for i in self.__cvv:
            if i == cvv:
                return True
            return False

    @staticmethod
    def generate_account_number(self) -> int:
        self.account_number = random.randint(1000000000, 9999999999)
        if self.validate_acc_num(self):
            self.generate_account_number()
        else:
            self.__acc_numbers.append(self.account_number)
        return self.account_number

    @staticmethod
    def generate_card_number(self) -> int:
        self.card_number = random.randint(1000000000000, 9999999999999)
        if self.validate_card_num(self):
            self.generate_card_number()
        else:
            self.__card_numbers.append(self.card_number)
        return self.card_number

    @staticmethod
    def generate_cvv(self) -> int:
        self.cvv = random.randint(100, 999)
        if self.validate_cvv(self):
            self.generate_cvv()
        else:
            self.__cvv.append(self.cvv)
        return self.cvv
