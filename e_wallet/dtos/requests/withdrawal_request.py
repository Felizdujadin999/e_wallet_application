class withdraw_request:
    def __init__(self):
        self.__Withdraw_pin: str = ""
        self.__Account_Number: str = ""
        self.__amount: float = 0.0

    def set_Withdraw_pin(self, Withdraw_pin) -> None:
        self.__Withdraw_pin = Withdraw_pin

    def get_Withdraw_pin(self) -> str:
        return self.__Withdraw_pin

    def set_Account_Number(self, Account_Number) -> None:
        self.__Account_Number = Account_Number

    def get_Account_Number(self) -> str:
        return self.__Account_Number

    def set_amount(self, amount) -> None:
        self.__amount = amount

    def get_amount(self) -> float:
        return self.__amount
