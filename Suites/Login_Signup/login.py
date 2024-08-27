import allure
import time
from playwright.sync_api import Page, Playwright, expect
from Suites.Base.BaseSetUp import BaseSetUp


class LoginRegistration(BaseSetUp):

    def set_up(self):
        try:
            super().set_up_no_login()
            allure.attach(self.page.screenshot(), name='Set up passed', attachment_type=allure.attachment_type.PNG)
        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Set up failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)

    @allure.step('Check transfer to login tab')
    def check_transf_to_login(self):
        login_tab = self.page.locator("p").filter(has_text="Log in")

        try:
            login_tab.click()
            allure.attach(self.page.screenshot(), name='Transfer to login tab',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Transfer to login tab failed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)



    @allure.step("Fill in credentials")
    def fill_email(self):
        try:
            email_field = self.page.get_by_placeholder("E-mail")
            email_field.fill("samoilenkofluttershy@gmail.com")
            allure.attach(self.page.screenshot(), name='Username field filled', attachment_type=allure.attachment_type.PNG)
        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Username field is not filled', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)


    @allure.step("Fill in password")
    def fill_password_field(self):
        try:
            password_field = self.page.get_by_placeholder("Password")
            password_field.fill("193786Az()")
            allure.attach(self.page.screenshot(), name='Password field filled', attachment_type=allure.attachment_type.PNG)
        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Password field is not filled', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)


    @allure.step("Click log in button")
    def click_log_in_button(self):
        try:
            login_button = self.page.locator('xpath=/html/body/div[2]/div/div[2]/div/div/div/div[1]/div[2]/button')
            login_button.click()
            allure.attach(self.page.screenshot(), name='Log in button clicked', attachment_type=allure.attachment_type.PNG)
        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Log in button is not clicked', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)

    @allure.step("Enter account")
    def enter_account(self):
        try:
            account_button = self.page.get_by_role("button", name="Account")
            account_button.click()
            allure.attach(self.page.screenshot(), name='Account button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Account button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)


    @allure.step("Check email")
    def check_email(self):
        welcome_message = self.page.locator(".text-map_welcome")
        expect(welcome_message).to_contain_text('Welcome, samoilenkofluttershy@gmail.com')

        time.sleep(10)



class LoginButton(BaseSetUp):
    def set_up(self):
        try:
            super().set_up_no_login()
            allure.attach(self.page.screenshot(), name='Set up passed', attachment_type=allure.attachment_type.PNG)
        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Set up failed', attachment_type=allure.attachment_type.PNG)


    @allure.step("Press log in button")
    def press_log_in_button(self):
        log_in_button = self.page.get_by_role("button", name="Log in")

        try:
            log_in_button.click()
            allure.attach(self.page.screenshot(), name='Log in button clicked', attachment_type=allure.attachment_type.PNG)
        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Log in button is not clicked', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)


    @allure.step("Fill in credentials")
    def fill_email(self):
        try:
            email_field = self.page.get_by_placeholder("E-mail")
            email_field.fill("samoilenkofluttershy@gmail.com")
            allure.attach(self.page.screenshot(), name='Username field filled',
                          attachment_type=allure.attachment_type.PNG)
        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Username field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)


    @allure.step("Fill in password")
    def fill_password_field(self):
        try:
            password_field = self.page.get_by_placeholder("Password")
            password_field.fill("193786Az()")
            allure.attach(self.page.screenshot(), name='Password field filled',
                          attachment_type=allure.attachment_type.PNG)
        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Password field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)


    @allure.step("Click log in button")
    def click_log_in_button(self):
        try:
            login_button = self.page.locator('xpath=/html/body/div[2]/div/div[2]/div/div/div/div[1]/div[2]/button')
            login_button.click()
            allure.attach(self.page.screenshot(), name='Log in button clicked',
                          attachment_type=allure.attachment_type.PNG)
        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Log in button is not clicked',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)

    @allure.step("Enter account")
    def enter_account(self):
        try:
            account_button = self.page.get_by_role("button", name="Account")
            account_button.click()
            allure.attach(self.page.screenshot(), name='Account button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Account button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)


    @allure.step("Check email")
    def check_email(self):
        welcome_message = self.page.locator(".text-map_welcome")
        expect(welcome_message).to_contain_text('Welcome, samoilenkofluttershy@gmail.com')



