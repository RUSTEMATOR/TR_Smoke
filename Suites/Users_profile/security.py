import allure
from playwright.sync_api import expect
from Suites.Base.BaseSetUp import BaseSetUp
from Suites.Locators.page_elements import MainSuiteLocators


class Security(BaseSetUp, MainSuiteLocators):

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



    @allure.step("Switch to security tab")
    def switch_to_security_tab(self):
        try:
            self.security_tab.click()
            allure.attach(self.page.screenshot(), name='Security tab pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Security tab is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e


    @allure.step("Negative Test Enter old password")
    def negative_enter_old_password(self):
        try:
            self.oldpass_input.click()
            self.oldpass_input.fill("562387562Az.")
            allure.attach(self.page.screenshot(), name='Old password field filled',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Old password field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e


    @allure.step("Negative Test enter new password")
    def negative_enter_new_password(self):
        try:
            self.newpass_input.click()
            self.newpass_input.fill("123456789Az")
            allure.attach(self.page.screenshot(), name='New password field filled',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='New password field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e



    @allure.step("Negative Test enter confirm password")
    def negative_enter_confirm_password(self):
        try:
            self.repeat_newpass.click()
            self.repeat_newpass.fill("123456789Az")
            allure.attach(self.page.screenshot(), name='Confirm password field filled',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Confirm password field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e


    @allure.step("Negative Test click save button")
    def negative_click_save_button(self):
        try:
            self.save_button.click()
            allure.attach(self.page.screenshot(), name='Save button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Save button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e


    @allure.step("Expect error popup")
    def expect_error_popup(self):
        try:
            expect(self.wrong_oldpassword_popup).to_be_visible()
            allure.attach(self.page.screenshot(), name='Error popup is visible',
                          attachment_type=allure.attachment_type.PNG)
            allure.attach("Error popup check successful.", name='Error popup check passed', attachment_type=allure.attachment_type.TEXT)
            self.page.reload()

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Error popup is not visible',
                          attachment_type=allure.attachment_type.PNG)
            allure.attach("Error popup check failed.", name='Error popup check failed', attachment_type=allure.attachment_type.TEXT)
            raise AssertionError from e

    @allure.step("Negative Test wrong repeated new password")
    def negative_wrong_repeated_newpassword(self):
        try:
            self.oldpass_input.fill("193786Az.")
            self.newpass_input.fill("12345678Az.")
            self.repeat_newpass.fill("123456jjjjbh")

            allure.attach(self.page.screenshot(), name='Old password field filled',
                          attachment_type=allure.attachment_type.PNG)

            if self.save_button.get_attribute("disabled") is not None:
                allure.attach(self.page.screenshot(), name='Save button is not clickable',
                              attachment_type=allure.attachment_type.PNG)
                self.page.reload()
                return True
            else:
                allure.attach(self.page.screenshot(), name='Save button is clickable',
                              attachment_type=allure.attachment_type.PNG)
                self.page.reload()
                return False

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Save button is not disabled',
                          attachment_type=allure.attachment_type.PNG)
            allure.attach("Save button check failed.", name='Save button check failed', attachment_type=allure.attachment_type.TEXT)
            raise AssertionError from e

    @allure.step("Positive Test change password")
    def positive_change_password(self):
        try:
            self.oldpass_input.fill("193786Az()")
            self.newpass_input.fill("193786Az.")
            self.repeat_newpass.fill("193786Az.")
            self.save_button.click()
            allure.attach(self.page.screenshot(), name='Old password field filled',
                          attachment_type=allure.attachment_type.PNG)

            expect(self.password_changed_success_popup).to_be_visible()
            self.page.reload()

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Password changed success popup is not visible',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

    def cleanup(self):
        self.oldpass_input.fill("193786Az.")
        self.newpass_input.fill("193786Az()")
        self.repeat_newpass.fill("193786Az()")
        self.save_button.click()


