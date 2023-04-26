from data.models.account import Account
from data.models.wallet import EWallet
from dtos.requests import register_bank_account_request
from dtos.requests.register_request import Register_request
from dtos.requests.transfer_request import TransferRequest
from services.bank_service_impl import bank_service_impl


class Mapper:

    @staticmethod
    def map(request: Register_request):
        EWallet.set_last_name(request.get_last_name())
        EWallet.set_first_name(request.get_first_name())
        EWallet.set_userName(request.get_user_name())
        EWallet.set_password(request.get_password())
        return EWallet

    def map_account(self: Account, bank_request: register_bank_account_request):
        Account.set_gender(self, bank_request.get_gender())
        Account.set_bvn(self, bank_request.get_bvn())
        Account.set_nin(self, bank_request.get_nin())
        Account.set_email(self, bank_request.get_email())
        Account.set_address(self, bank_request.get_address())
        Account.set_last_name(self, bank_request.get_last_name())
        Account.set_first_name(self, bank_request.get_first_name())
        Account.set_dob(self, bank_request.get_dob())
        Account.set_pin(self, bank_request.get_pin())
        Account.set_acc_numbers(self, bank_service_impl.generate_account_number(self))
        Account.set_card_number(self, bank_service_impl.generate_card_number(self))
        Account.set_cvv(self, bank_service_impl.generate_cvv(self))

    @staticmethod
    def map_to_transfer_request(self, transfer_data) -> TransferRequest:
        transfer_request = TransferRequest()
        transfer_request.set_senders_name(transfer_data["senders_name"])
        transfer_request.set_senders_pin(transfer_data["senders_pin"])
        transfer_request.set_receivers_wallet_id(transfer_data["receivers_wallet_id"])
        transfer_request.set_amount(transfer_data["amount"])
        return transfer_request
