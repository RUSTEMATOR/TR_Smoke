import allure
import time
from Suites.Base.BaseSetUp import BaseSetUp
from Suites.Locators.page_elements import GameSuitLocators


class DemoTest(BaseSetUp, GameSuitLocators):

    def set_up(self):
        try:
            super().set_up()
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Set up failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

    @allure.step("Click on the input field")
    def click_on_input_field(self):
        try:
            self.search_field.click()
            allure.attach(self.page.screenshot(), name='Input field clicked',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Input field is not clicked',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.enter_game_name()

    @allure.step("Enter game name")
    def enter_game_name(self):
        try:
            self.search_field.fill("Aztec Spell - 10 Lines")
            time.sleep(3)
            allure.attach(self.page.screenshot(), name='Game name entered', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Game name is not entered',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.press_game_banner()

    @allure.step("Press game banner")
    def press_game_banner(self):
        try:
            self.first_game_card.click()
            allure.attach(self.page.screenshot(), name='Game banner pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Game banner is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.press_demo_button()

    @allure.step("Press play button")
    def press_demo_button(self):
        try:
            self.demo_button.click()
            allure.attach(self.page.screenshot(), name='Play button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Play button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(8)
            self.change_sum()

    @allure.step("Change deposit sum in the deposit modal")
    def change_sum(self):
        try:
            self.seven_five_zero_button.click()
            allure.attach(self.page.screenshot(), name='Deposit sum changed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Deposit sum is not changed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.check_deposit_modal()

    @allure.step("Close ingame modal window")
    def check_deposit_modal(self):
        try:
            if self.balance_text.is_visible():
                pass

            else:
                allure.attach(self.page.screenshot(), name='Deposit modal window is not visible',
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Deposit modal window is not visible',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

