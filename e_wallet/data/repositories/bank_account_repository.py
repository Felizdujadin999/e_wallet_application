class Bank_account_repo:
    def save(self, accounts):
        raise NotImplementedError

    def find(self, id):
        raise NotImplementedError

    def number_of_account(self):
        raise NotImplementedError

    def find_by_account_number(self,account_number):
        raise NotImplementedError