import allure
import time
import re
from playwright.sync_api import sync_playwright, Playwright, expect
from Suites.Base.BaseSetUp import BaseSetUp

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



class Registration(BaseSetUp):
    def set_up(self):
        try:
            super().set_up_no_login()
            allure.attach(self.page.screenshot(), name='Set up passed', attachment_type=allure.attachment_type.PNG)

        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Set up failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)

    @allure.step('Press on Sign up button')
    def press_sign_up_button(self):
        try:
            self.sign_up_button.click()
            allure.attach(self.page.screenshot(), name='Sign up button pressed', attachment_type=allure.attachment_type.PNG)
            expect(self.sign_up_button).to_be_visible()

        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Sign up button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)


    @allure.step('Fill E-mail field')
    def fill_email_field(self):
        email_field = self.page.locator("#email-input")
        random_email = Generator.generate_random_email()
        try:
            email_field.fill(random_email)
            allure.attach(self.page.screenshot(), name='E-mail field filled', attachment_type=allure.attachment_type.PNG)
            expect(email_field).to_have_value(random_email)
        except Exception as exc:
            allure.attach(self.page.screenshot(), name='E-mail field is not filled', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)

    @allure.step('Fill Password field')
    def fill_password_field(self):
        password_field = self.page.locator("#password-input")
        try:
            password_field.fill("193786Az()")
            allure.attach(self.page.screenshot(), name='Password field filled', attachment_type=allure.attachment_type.PNG)
            expect(password_field).to_have_value("193786Az()")
        except Exception as exc:
            allure.attach(self.page.screenshot(), name='Password field is not filled', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)

    @allure.step('18 years checkbox is checked')
    def check_18_years(self):
        checkbox = self.page.locator("#is18-checkbox")
        try:
            checkbox.click()
            allure.attach(self.page.screenshot(), name='18 years checkbox clicked', attachment_type=allure.attachment_type.PNG)
        except Exception as exc :
            allure.attach(self.page.screenshot(), name='18 years checkbox is not checked', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)


    @allure.step('Press on final Sign up button')
    def press_final_sign_up_button(self):
        sign_up_button = self.page.locator("form").get_by_role("button", name="Sign up")
        try:
            sign_up_button.click()
            allure.attach(self.page.screenshot(), name='Final Sign up button pressed', attachment_type=allure.attachment_type.PNG)
            expect(self.deposit_button).to_be_visible(timeout=10000_0000)
        except Exception as exc :
            allure.attach(self.page.screenshot(), name='Final Sign up button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)


    def refresh_page(self):
        self.page.reload()



    @allure.step('Press on Account button')
    def enter_account(self):
        account_button = self.page.get_by_role("button", name="Account")

        try:
            account_button.click()
            allure.attach(self.page.screenshot(), name='Account button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as exc :
            allure.attach(self.page.screenshot(), name='Account button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)


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
        phone_number_field = self.page.get_by_placeholder("Phone number")


        try:
            first_name_field.click()
            allure.attach(self.page.screenshot(), name='First name field clicked', attachment_type=allure.attachment_type.PNG)
            first_name_field.fill("Gregory")
            allure.attach(self.page.screenshot(), name='First name field filled', attachment_type=allure.attachment_type.PNG)
            expect(first_name_field).to_have_value("Gregory")

            last_name_field.click()
            allure.attach(self.page.screenshot(), name='Last name field clicked', attachment_type=allure.attachment_type.PNG)
            last_name_field.fill("Giga")
            allure.attach(self.page.screenshot(), name='Last name field filled', attachment_type=allure.attachment_type.PNG)
            expect(last_name_field).to_have_value("Giga")

            day_field.click()
            allure.attach(self.page.screenshot(), name='Day field clicked', attachment_type=allure.attachment_type.PNG)
            self.page.get_by_text("29").click()
            allure.attach(self.page.screenshot(), name='Day field filled', attachment_type=allure.attachment_type.PNG)
            expect(day_field).to_have_value("29")
            month_field.click()
            allure.attach(self.page.screenshot(), name='Month field clicked', attachment_type=allure.attachment_type.PNG)

            self.page.get_by_text("Mar").click()
            allure.attach(self.page.screenshot(), name='Month field filled', attachment_type=allure.attachment_type.PNG)
            expect(month_field).to_have_value("Mar")


            year_field.click()
            allure.attach(self.page.screenshot(), name='Year field clicked', attachment_type=allure.attachment_type.PNG)
            self.page.get_by_text("1996").click()
            allure.attach(self.page.screenshot(), name='Year field filled', attachment_type=allure.attachment_type.PNG)
            expect(year_field).to_have_value("1996")

            city_field.click()
            allure.attach(self.page.screenshot(), name='City field clicked', attachment_type=allure.attachment_type.PNG)
            city_field.fill("Testik")
            allure.attach(self.page.screenshot(), name='City field filled', attachment_type=allure.attachment_type.PNG)
            expect(city_field).to_have_value("Testik")

            postcode_field.click()
            allure.attach(self.page.screenshot(), name='Postcode field clicked', attachment_type=allure.attachment_type.PNG)
            postcode_field.fill("12345")
            allure.attach(self.page.screenshot(), name='Postcode field filled', attachment_type=allure.attachment_type.PNG)
            expect(postcode_field).to_have_value("12345")

            full_address_house_number_field.click()
            allure.attach(self.page.screenshot(), name='Full address (house number, field clicked', attachment_type=allure.attachment_type.PNG)
            full_address_house_number_field.fill("Scripting street 34")
            allure.attach(self.page.screenshot(), name='Full address (house number, field filled', attachment_type=allure.attachment_type.PNG)
            expect(full_address_house_number_field).to_have_value("Scripting street 34")

            phone_number_field.click()
            allure.attach(self.page.screenshot(), name='Phone number field clicked', attachment_type=allure.attachment_type.PNG)
            phone_number_field.fill("418-691-2020")
            allure.attach(self.page.screenshot(), name='Phone number field filled', attachment_type=allure.attachment_type.PNG)
            expect(phone_number_field).to_have_value("418-691-2020")

        except Exception as exc :
            allure.attach(self.page.screenshot(), name='Personal info is not filled', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)


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

        except Exception as exc :
            allure.attach(self.page.screenshot(), name='Save button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)

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

        except Exception as exc :
            allure.attach(self.page.screenshot(), name='Save button is not clickable',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(exc)


