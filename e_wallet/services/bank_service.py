from dtos.requests.register_bank_account_request import register_bank_request


class Bank_service:

    def create_account(self: register_bank_request):
        raise NotImplementedError

    def withdrawal(self, amount, password):
        raise NotImplementedError

    def transfer(self, amount, password):
        raise NotImplementedError

    def check_balance(self):
        raise NotImplementedError
