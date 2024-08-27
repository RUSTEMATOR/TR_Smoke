import allure
from playwright.sync_api import expect
from Suites.Base.BaseSetUp import BaseSetUp
from Suites.Locators.page_elements import MainSuiteLocators


class PersonalInfVer(BaseSetUp, MainSuiteLocators):

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
            allure.attach(self.page.screenshot(), name='Account button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Account button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e



    @allure.step("Check filled inputs")
    def check_filled_inputs(self):
        try:
            expect(self.first_name_input and
            self.last_name_input and
            self.day_dropdown and
            self.month_dropdown and
            self.year_dropdown and
            self.city_input and
            self.postcode_input and
            self.full_address_house_number_input and
            self.country_dropdown).to_be_disabled()
            # Log success
            allure.attach("All inputs are correctly disabled.", name='Inputs check passed',
                          attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            # Attach the error message to the Allure report
            error_message = f"Error checking filled inputs: {str(e)}"
            allure.attach(error_message, name='Error checking filled inputs',
                          attachment_type=allure.attachment_type.TEXT)

            # Optionally, attach a screenshot for visual context
            allure.attach(self.page.screenshot(), name='Error during check filled inputs',
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.screenshot(), name='Error during check filled inputs',
                          attachment_type=allure.attachment_type.PNG)

            # Reraise the exception to ensure the test framework can handle it
            raise AssertionError from e

    @allure.step("Check email copy")
    def check_email_copy(self):
        try:
            self.user_email.click()
            expect(self.coping_success_popup).to_be_visible()
            # Log success
            allure.attach("Email copy check successful.", name='Email copy check passed',
                          attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            # Attach the error message to the Allure report
            error_message = f"Error checking email copy: {str(e)}"
            allure.attach(error_message, name='Error checking email copy',
                          attachment_type=allure.attachment_type.TEXT)

            # Optionally, attach a screenshot for visual context
            allure.attach(self.page.screenshot(), name='Error during check email copy',
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.screenshot(), name='Error during check email copy',
                          attachment_type=allure.attachment_type.PNG)

            # Reraise the exception to ensure the test framework can handle it
            raise AssertionError from e


    @allure.step("Change gender")
    def check_gender_change(self):
        try:
            self.male_radio_button.click()
            allure.attach(self.page.screenshot(), name='Male radio button pressed', attachment_type=allure.attachment_type.PNG)

            self.save_button.click()
            allure.attach(self.page.screenshot(), name='Save button pressed', attachment_type=allure.attachment_type.PNG)

            expect(self.confirmation_popup).to_be_visible()

            self.female_radio_button.click()
            allure.attach(self.page.screenshot(), name='Female radio button pressed', attachment_type=allure.attachment_type.PNG)

            self.save_button.click()
            allure.attach(self.page.screenshot(), name='Save button pressed', attachment_type=allure.attachment_type.PNG)

            expect(self.confirmation_popup).to_be_visible()
            # Log success
            allure.attach("Gender change check successful.", name='Gender change check passed',
                          attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            # Attach the error message to the Allure report
            error_message = f"Error changing gender: {str(e)}"
            allure.attach(error_message, name='Error changing gender',
                          attachment_type=allure.attachment_type.TEXT)

            # Optionally, attach a screenshot for visual context
            allure.attach(self.page.screenshot(), name='Error during changing gender',
                          attachment_type=allure.attachment_type.PNG)



    @allure.step("Switch to Verification tab")
    def switch_to_verification_tab(self):
        try:
            self.verification_tab.click()
            allure.attach(self.page.screenshot(), name='Verification tab pressed', attachment_type=allure.attachment_type.PNG)
            # Log success
            allure.attach("Switch to Verification tab successful.", name='Verification tab switch passed',
                          attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            # Attach the error message to the Allure report
            error_message = f"Error switching to verification tab: {str(e)}"
            allure.attach(error_message, name='Error switching to verification tab',
                          attachment_type=allure.attachment_type.TEXT)

            # Optionally, attach a screenshot for visual context
            allure.attach(self.page.screenshot(), name='Error during switching to verification tab',
                          attachment_type=allure.attachment_type.PNG)



    @allure.step("Check the page")
    def check_the_page(self):
        try:
            expect(self.title_uploading_documents and
                   self.title_proof_address and
                   self.title_proof_of_identity and
                   self.title_proof_deposit).to_be_visible()
            allure.attach(self.page.screenshot(), name='Page is visible', attachment_type=allure.attachment_type.PNG)
            # Log success
            allure.attach("Page check successful.", name='Page check passed',
                          attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            # Attach the error message to the Allure report
            error_message = f"Error checking the page: {str(e)}"
            allure.attach(error_message, name='Error checking the page',
                          attachment_type=allure.attachment_type.TEXT)

            # Optionally, attach a screenshot for visual context
            allure.attach(self.page.screenshot(), name='Error during checking the page',
                          attachment_type=allure.attachment_type.PNG)



