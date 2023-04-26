class TransferRequest:

    def __init__(self):
        self.__senders_name = None
        self.__senders_pin: str = ""
        self.__receivers_wallet_id: int = 0
        self.__amount: float = 0.0

    def set_senders_name(self, senders_name) -> None:
        self.__senders_name = senders_name

    def get_sender_name(self) -> str:
        return self.__senders_name

    def set_senders_pin(self, senders_pin) -> None:
        self.__senders_pin = senders_pin

    def get_senders_pin(self) -> str:
        return self.__senders_pin

    def set_receivers_wallet_id(self, receivers_wallet_id) -> None:
        self.__receivers_wallet_id = receivers_wallet_id

    def get_receivers_wallet_id(self) -> int:
        return self.__receivers_wallet_id

    def set_amount(self, amount) -> None:
        self.__amount = amount

    def get_amount(self) -> float:
        return self.__amount
