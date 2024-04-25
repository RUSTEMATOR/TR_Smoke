import allure
from playwright.sync_api import expect
from Suites.Base.BaseSetUp import BaseSetUp
from Suites.Locators.page_elements import MainSuiteLocators


class Wallet(BaseSetUp, MainSuiteLocators):

    def set_up(self):
        try:
            super().set_up()
            allure.attach(self.page.screenshot(), name='Set up passed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Set up failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e


    @allure.step("Enter the user's account")
    def enter_user_account(self):
        try:
            self.account_button.click()
            allure.attach(self.page.screenshot(), name='Account button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Account button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e


