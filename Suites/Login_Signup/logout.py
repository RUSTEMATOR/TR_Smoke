import allure
import time
from playwright.sync_api import Page
from Suites.Base.BaseSetUp import BaseSetUp



class Logout(BaseSetUp):
    def set_up(self):
        try:
            super().set_up()
            allure.attach(self.page.screenshot(), name='Set up passed', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Set up failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e




    @allure.step("Enter account")
    def enter_account(self):
        try:
            account_button = self.page.get_by_role("button", name="Account")
            account_button.click()
            allure.attach(self.page.screenshot(), name='Account button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Account button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e


    @allure.step("Log out")
    def log_out(self):
        log_out_button = self.page.get_by_label("Log out")
        sign_up_button = self.page.get_by_role("button", name="Sign up").first

        try:
            log_out_button.click()
            allure.attach(self.page.screenshot(), name='Log out button clicked', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Log out button is not clicked', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            sign_up_button.wait_for(state="visible")
            if sign_up_button.is_visible():
                pass
            else:
                raise AssertionError("Sign up button is not visible")

