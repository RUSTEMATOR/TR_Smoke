import allure
import time
import re
from playwright.sync_api import Page



class Login():
    def __init__(self, page: Page):
        self.page = page




    @allure.title("Go to site")
    def open_site(self):
        try:
            self.page.goto('https://tombriches.com/')
            allure.attach(self.page.screenshot(), name='Page open', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Page opening failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.press_sign_up_button()


    def press_sign_up_button(self):
        try:
            sign_up_button = self.page.get_by_role("button", name="Sign up")
            sign_up_button.click()
            allure.attach(self.page.screenshot(), name='Sign up button clicked', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Sign up button is not clicked', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.
