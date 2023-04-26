from typing import Optional

from dtos.requests.register_bank_account_request import register_bank_request


class Bank_service:

    def create_account(self: register_bank_request):
        raise NotImplementedError

    def withdrawal(self, amount, password):
        if self.__balance >= amount:
            self.__balance -= amount
            return self.__balance
        else:
            print("Insufficient funds.")
            return None

    def transfer(self, transfer_request) -> Optional[float]:
        if transfer_request.get_senders_pin() == "1234":
            amount = transfer_request.get_amount()
            if self.__balance >= amount:
                self.__balance -= amount
                return self.__balance
            else:
                print("Insufficient funds.")
                return None
        else:
            print("Invalid PIN.")
            return None

    def transfer(self, amount, password):
        raise NotImplementedError

    def check_balance(self):
        raise NotImplementedError
