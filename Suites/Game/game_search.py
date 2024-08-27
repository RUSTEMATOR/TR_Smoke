import allure
import time
from Suites.Base.BaseSetUp import BaseSetUp
from Suites.Locators.page_elements import GameSuitLocators


class InputTest(BaseSetUp, GameSuitLocators):
    
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
            allure.attach(self.page.screenshot(), name='Input field clicked', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Input field is not clicked', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e



    @allure.step("Enter game name")
    def enter_game_name(self):
        try:
            self.search_field.fill("Aztec Temple")
            time.sleep(3)
            allure.attach(self.page.screenshot(), name='Game name entered', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Game name is not entered', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.press_game_banner()

    @allure.step("Press game banner")
    def press_game_banner(self):
        try:
            self.first_game_card.click()
            allure.attach(self.page.screenshot(), name='Game banner pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Game banner is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e



    @allure.step("Press play button")
    def press_play_button(self):
        try:
            self.play_button.click()
            allure.attach(self.page.screenshot(), name='Play button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Play button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e


    @allure.step("Close ingame modal window")
    def close_ingame_modal(self):
        try:
            self.ingame_close_button.click()
            allure.attach(self.page.screenshot(), name='Ingame modal window closed', attachment_type=allure.attachment_type.PNG)
            time.sleep(10)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Ingame modal window is not closed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e







