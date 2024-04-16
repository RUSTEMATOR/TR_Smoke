import allure
import time
import re
from playwright.sync_api import Page


class Generator():
    @staticmethod
    # Function to generate a random email
    def generate_random_email():
        import random
        import string
        random_numbers = ''.join(random.choice(string.digits) for _ in range(5))
        random_word = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        automaton = "automaton_"
        return f'{automaton}{random_word}{random_numbers}@kingbilly.xyz'

class Registration():
    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open a site')
    def open_site(self):
        try:
            self.page.goto('https://tombriches.com/')
            allure.attach(self.page.screenshot(), name='Page open', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Page opening failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.press_sign_up_button()

    @allure.step('Press on Sign up button')
    def press_sign_up_button(self):
        sign_up_button = self.page.get_by_role("button", name="Sign up")
        try:
            sign_up_button.click()
            allure.attach(self.page.screenshot(), name='Sign up button pressed', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Sign up button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.check_transf_to_login()

    @allure.step('Check transfer to login tab')
    def check_transf_to_login(self):
        login_tab =  self.page.locator("p").filter(has_text="Log in")

        try:
            login_tab.click()
            allure.attach(self.page.screenshot(), name='Transfer to login tab', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Transfer to login tab failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.back_to_registration()

    @allure.step('Go back to the registration tab')
    def back_to_registration(self):
        reg_tab = self.page.locator("p").filter(has_text=re.compile(r"^Sign up$"))

        try:
            reg_tab.click()
            allure.attach(self.page.screenshot(), name='Go back to registration tab', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Go back to registration tab failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.fill_reg_info()

    @allure.step('Fill registration form')
    def fill_reg_info(self):
        email_field = self.page.get_by_placeholder("E-mail")
        password_field = self.page.get_by_placeholder("Password")
        try:
            email_field.click()
            allure.attach(self.page.screenshot(), name='E-mail field clicked', attachment_type=allure.attachment_type.PNG)
            self.fill_email_field(email_field)
            password_field.click()
            allure.attach(self.page.screenshot(), name='Password field clicked', attachment_type=allure.attachment_type.PNG)
            self.fill_password_field(password_field)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Registration form is not filled', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.check_18_years()

    @allure.step('Fill E-mail field')
    def fill_email_field(self, email_field):
        email_field.fill(Generator.generate_random_email())
        allure.attach(self.page.screenshot(), name='E-mail field filled', attachment_type=allure.attachment_type.PNG)

    @allure.step('Fill Password field')
    def fill_password_field(self, password_field):
        password_field.fill("193786Az()")
        allure.attach(self.page.screenshot(), name='Password field filled', attachment_type=allure.attachment_type.PNG)

    @allure.step('18 years checkbox is checked')
    def check_18_years(self):
        checkbox = self.page.locator("#is18-checkbox")
        try:
            checkbox.click()
            allure.attach(self.page.screenshot(), name='18 years checkbox clicked', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='18 years checkbox is not checked', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.press_final_sign_up_button()

    @allure.step('Press on final Sign up button')
    def press_final_sign_up_button(self):
        sign_up_button = self.page.locator("form").get_by_role("button", name="Sign up")
        try:
            sign_up_button.click()
            allure.attach(self.page.screenshot(), name='Final Sign up button pressed', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Final Sign up button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            time.sleep(10)
            self.refresh_page()

    def refresh_page(self):
        try:
            self.page.reload()
        finally:
           self.enter_account()



    @allure.step('Press on Account button')
    def enter_account(self):
        account_button = self.page.get_by_role("button", name="Account")

        try:
            account_button.click()
            allure.attach(self.page.screenshot(), name='Account button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Account button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.fill_personal_info()

    @allure.step('Fill in personal info')
    def fill_personal_info(self):
        first_name_field = self.page.get_by_placeholder("First name")
        last_name_field = self.page.get_by_placeholder("Last name")
        day_field = self.page.get_by_text("Day")
        month_field = self.page.get_by_text("Month")
        year_field = self.page.get_by_text("Year")
        city_field = self.page.get_by_placeholder("City")
        postcode_field = self.page.get_by_placeholder("Postcode")
        full_address_house_number_field = self.page.get_by_placeholder("Full address (house number,")


        try:
            first_name_field.click()
            allure.attach(self.page.screenshot(), name='First name field clicked', attachment_type=allure.attachment_type.PNG)
            first_name_field.fill("Gregory")
            allure.attach(self.page.screenshot(), name='First name field filled', attachment_type=allure.attachment_type.PNG)


            last_name_field.click()
            allure.attach(self.page.screenshot(), name='Last name field clicked', attachment_type=allure.attachment_type.PNG)
            last_name_field.fill("Giga")
            allure.attach(self.page.screenshot(), name='Last name field filled', attachment_type=allure.attachment_type.PNG)

            day_field.click()
            allure.attach(self.page.screenshot(), name='Day field clicked', attachment_type=allure.attachment_type.PNG)
            self.page.get_by_text("29").click()
            allure.attach(self.page.screenshot(), name='Day field filled', attachment_type=allure.attachment_type.PNG)
            month_field.click()
            allure.attach(self.page.screenshot(), name='Month field clicked', attachment_type=allure.attachment_type.PNG)

            self.page.get_by_text("Mar").click()


            year_field.click()
            allure.attach(self.page.screenshot(), name='Year field clicked', attachment_type=allure.attachment_type.PNG)
            self.page.get_by_text("1996").click()
            allure.attach(self.page.screenshot(), name='Year field filled', attachment_type=allure.attachment_type.PNG)

            city_field.click()
            allure.attach(self.page.screenshot(), name='City field clicked', attachment_type=allure.attachment_type.PNG)
            city_field.fill("Testik")
            allure.attach(self.page.screenshot(), name='City field filled', attachment_type=allure.attachment_type.PNG)

            postcode_field.click()
            allure.attach(self.page.screenshot(), name='Postcode field clicked', attachment_type=allure.attachment_type.PNG)
            postcode_field.fill("12345")
            allure.attach(self.page.screenshot(), name='Postcode field filled', attachment_type=allure.attachment_type.PNG)

            full_address_house_number_field.click()
            allure.attach(self.page.screenshot(), name='Full address (house number, field clicked', attachment_type=allure.attachment_type.PNG)
            full_address_house_number_field.fill("Scripting street 34")

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Personal info is not filled', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.confirm_cookies()
            self.save_personal_info()

    @allure.step('confirm cookies')
    def confirm_cookies(self):
        cookie_popup = self.page.get_by_role("button", name="ok")
        cookie_popup.click()
        allure.attach(self.page.screenshot(), name='Cookies confirmed', attachment_type=allure.attachment_type.PNG)

    @allure.step('Press on Save button')
    def save_personal_info(self):
        save_button = self.page.get_by_role("button", name="Save")
        try:
            save_button.click()
            allure.attach(self.page.screenshot(), name='Save button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Save button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

    def verify_the_data_is_saved(self):

        try:
            save_button = self.page.locator("button[name='Save']")
            if save_button.is_disabled():
                allure.attach(self.page.screenshot(), name='Save button is not clickable',
                              attachment_type=allure.attachment_type.PNG)
                return True
            else:
                allure.attach(self.page.screenshot(), name='Save button is clickable',
                              attachment_type=allure.attachment_type.PNG)
                return False

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Save button is not clickable',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
