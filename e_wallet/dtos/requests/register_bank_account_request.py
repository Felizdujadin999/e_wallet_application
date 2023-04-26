from datetime import date

from dateutil.relativedelta import relativedelta


class register_bank_request:

    def __init__(self):
        self.gender = str
        self.BVN = int
        self.NIN = int
        self.email = str
        self.address = str
        self.last_name = str
        self.first_name = str
        self.dob = str
        self.acc_number = int
        self.card_number = int
        self.cvv = int
        self.expiry_date = date
        self.pin = int
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

    def set_acc_numbers(self, acc_number):
        self.acc_number = acc_number

    def get_acc_numbers(self):
        return self.acc_number

    def set_card_number(self, value):
        self.card_number = value

    def get_card_number(self):
        return self.card_number

    def set_cvv(self, value):
        self.cvv = value

    def get_cvv(self):
        return self.cvv

    def set_pin(self, value):
        self.pin = value

    def get_pin(self):
        return self.pin

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_expiry_date(self):
        current_date = date.today()
        future_date = current_date + relativedelta(years=3)
        self.expiry_date = future_date

    def get_expiry_date(self):
        return self.expiry_date

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
                    card_number:{self.get_card_number()}
                    cvv:{self.get_cvv()}
                    expiry date:{self.get_expiry_date()}
                    balance:{self.get_balance()}
                    ==========
                    """
