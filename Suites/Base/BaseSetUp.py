import time

import allure
from playwright.sync_api import Page, Playwright, expect
from Suites.Locators.page_elements import PageElementsGames


class BaseSetUp(PageElementsGames):

    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False,
                                                # proxy={
                                                #       'server': 'http://138.197.150.103:8090',
                                                #       'username': 'kbc',
                                                #       'password': '347SP&Uwqt!2xZ7w',
                                                #   }
        )
        self.context = self.browser.new_context()
        self.page = self.context.new_page()


    def handler(self):
        self.page.get_by_title('Cancel').click()
        time.sleep(2)

    def handler_deposit(self):
        self.page.locator('svg.cursor-pointer.z-10 > path').click()

    def handler_deposit_remove(self):
        # self.page.locator('div.flex > svg.cursor-pointer').click()
        self.page.evaluate('''
        () => {
        const depositPopUp = document.querySelector('div > .deposit-card')
        const shadowBackGround = document.querySelector('.bg-m_shadow')
        if (depositPopUp) {
            depositPopUp.remove()}
            
        if (shadowBackGround) {
            shadowBackGround.remove()}
        }
        ''')


    @allure.title("Go to site")
    def open_site(self):
        try:
            self.page.goto('https://tombriches.com/')
            allure.attach(self.page.screenshot(), name='Page open', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Page opening failed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

    @allure.step('Press on Log in button')
    def press_log_in_button(self):
        try:
            self.log_in_button.click()
            allure.attach(self.page.screenshot(), name='Log in button pressed',
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Log in button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

    @allure.step('Enter credentials')
    def enter_credentials(self):
        try:
            self.email_input.fill("samoilenkofluttershy@gmail.com")
            allure.attach(self.page.screenshot(), name='E-mail field filled',
                          attachment_type=allure.attachment_type.PNG)

            self.password_input.fill("193786Az()")
            allure.attach(self.page.screenshot(), name='Password field filled',
                          attachment_type=allure.attachment_type.PNG)

            self.confirm_log_in_button.click()

        except Exception as e:
            allure.attach(self.page.screenshot(), name='E-mail field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.screenshot(), name='Password field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e


    @allure.step('Confirm cookies')
    def confirm_cookies(self):
        try:
            self.cookie_popup.click()
            allure.attach(self.page.screenshot(), name='Cookie popup confirmed',
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Cookie popup is not confirmed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

    def set_up(self):
        self.page.add_locator_handler(self.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'), self.handler)
        self.open_site()
        self.press_log_in_button()
        self.enter_credentials()
        self.confirm_cookies()


    def set_up_no_login(self):
        self.open_site()