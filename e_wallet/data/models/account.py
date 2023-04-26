from data.models.credit_card import CreditCard


class Account(CreditCard):

    def __init__(self):
        super().__init__()
        self.id = int
        self.gender = str
        self.BVN = int
        self.NIN = int
        self.email = str
        self.address = str
        self.last_name = str
        self.first_name = str
        self.dob = str
        self.acc_number = int
        self.balance = float

    def set_gender(self, value):
        self.gender = value

    def get_gender(self):
        return self.gender

    def set_bvn(self, value):
        self.BVN = value

    def get_bvn(self):
        return self.BVN

    def set_nin(self, value):
        self.NIN = value

    def get_nin(self):
        return self.NIN

    def set_email(self, value):
        self.email = value

    def get_email(self):
        return self.email

    def set_address(self, value):
        self.address = value

    def get_address(self):
        return self.address

    def set_last_name(self, value):
        self.last_name = value

    def get_last_name(self):
        return self.last_name

    def set_first_name(self, value):
        self.first_name = value

    def get_first_name(self):
        return self.first_name

    def set_dob(self, value):
        self.dob = value

    def get_dob(self):
        return self.dob

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_acc_number(self, acc_number):
        self.acc_number = acc_number

    def get_acc_number(self):
        return self.acc_number

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"""
                    ==========
                    id:{self.id}
                    gender: {self.gender}
                    BVN : {self.BVN}
                    NIN: {self.NIN}
                    email:{self.email}
                    address:{self.address}
                    last_name:{self.last_name}
                    first_name:{self.first_name}
                    dob:{self.dob}
                    account_number:{self.acc_number}
                    card_number:{self.get_card_number()}
                    cvv:{self.get_cvv()}
                    expiry date:{self.get_expiry_date()}
                    ==========
                    """
