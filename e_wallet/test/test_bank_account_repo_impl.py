from unittest import TestCase

from data.models.account import Account

from data.repositories.bank_account_repo_impl import account_repo_impl


class Test_bank_account(TestCase):

    def setUp(self) -> None:
        self.bank_account = Account()
        self.bank_account.set_first_name("felix")
        self.bank_account.set_last_name("ezeike")
        self.bank_account.set_dob("2023-02-12")
        self.bank_account.set_gender("Female")
        self.bank_account.set_bvn("687907086e08")
        self.bank_account.set_nin("74875908")
        self.bank_account.set_address("19 owokoniran")
        self.bank_account.set_balance(5000.00)
        self.bank_creation = account_repo_impl()

    def test_save(self):
        self.bank_creation.save(self.bank_account)
        self.assertEqual(1, self.bank_creation.number_of_account())
        self.assertEqual(1, self.bank_account.get_id())

    def test_repo_can_save_more_than_one(self):
        self.bank_creation.save(self.bank_account)
        self.assertEqual(1, self.bank_creation.number_of_account())
        self.assertEqual(1, self.bank_account.get_id())
        self.bank_account2 = Account()
        self.bank_account2.set_first_name("felix2")
        self.bank_account2.set_last_name("ezeike2")
        self.bank_account2.set_dob("2023-02-12")
        self.bank_account2.set_gender("Female")
        self.bank_account2.set_bvn("687907086e08")
        self.bank_account2.set_nin("74875908")
        self.bank_account2.set_address("19 owokoniran")
        self.bank_account2.set_balance(2000.00)
        self.bank_creation.save(self.bank_account2)
        self.assertEqual(2, self.bank_creation.number_of_account())
        self.assertEqual(2, self.bank_account2.get_id())
        print(self.bank_account2)
