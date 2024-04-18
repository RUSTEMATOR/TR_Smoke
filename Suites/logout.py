import allure
import time
from playwright.sync_api import Page



class Logout():
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
            self.check_transf_to_login()

    @allure.step('Check transfer to login tab')
    def check_transf_to_login(self):
        login_tab = self.page.locator("p").filter(has_text="Log in")

        try:
            login_tab.click()
            allure.attach(self.page.screenshot(), name='Transfer to login tab',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Transfer to login tab failed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.fill_email()


    @allure.step("Fill in credentials")
    def fill_email(self):
        try:
            email_field = self.page.get_by_placeholder("E-mail")
            email_field.fill("samoilenkofluttershy@gmail.com")
            allure.attach(self.page.screenshot(), name='Username field filled', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Username field is not filled', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.fill_password_field()

    @allure.step("Fill in password")
    def fill_password_field(self):
        try:
            password_field = self.page.get_by_placeholder("Password")
            password_field.fill("193786Az.")
            allure.attach(self.page.screenshot(), name='Password field filled', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Password field is not filled', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.click_log_in_button()

    @allure.step("Click log in button")
    def click_log_in_button(self):
        try:
            login_button = self.page.locator('xpath=/html/body/div[2]/div/div[2]/div/div/div/div[1]/div[2]/button')
            login_button.click()
            allure.attach(self.page.screenshot(), name='Log in button clicked', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Log in button is not clicked', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            time.sleep(5)
            self.page.reload()
            self.enter_account()
    @allure.step("Enter account")
    def enter_account(self):
        try:
            account_button = self.page.get_by_role("button", name="Account")
            account_button.click()
            allure.attach(self.page.screenshot(), name='Account button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Account button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.log_out()


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