from datetime import date
from dateutil.relativedelta import relativedelta


class CreditCard:
    def __init__(self):
        self.card_number = int
        self.cvv = int
        self.expiry_date = date

    def set_card_number(self, value):
        self.card_number = value

    def get_card_number(self):
        return self.card_number

    def set_cvv(self, value):
        self.balance = value

    def get_cvv(self):
        return self.cvv

    def set_expiry_date(self):
        current_date = date.today()
        future_date = current_date + relativedelta(years=3)
        self.expiry_date = future_date

    def get_expiry_date(self):
        return self.expiry_date

    def __str__(self):
        return f"""
                    ==========
                    card_number: {self.card_number}
                    cvv:{self.cvv}
                    expiry_date:{self.expiry_date}
                    ==========
                    """
