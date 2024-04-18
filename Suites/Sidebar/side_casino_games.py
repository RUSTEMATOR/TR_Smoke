import allure
import time
import re
from Suites.Sidebar.page_elements import PageElements


class CasinoGamesSide(PageElements):

    @allure.title("Go to site")
    def open_site(self):
        try:
            self.page.goto('https://tombriches.com/')
            allure.attach(self.page.screenshot(), name='Page open', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Page opening failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.press_log_in_button()


    @allure.step('Press on Log in button')
    def press_log_in_button(self):
        try:
            self.log_in_button.click()
            allure.attach(self.page.screenshot(), name='Log in button pressed', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Log in button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.enter_credentials()

    @allure.step('Enter credentials')
    def enter_credentials(self):
        try:
            self.email_input.fill("samoilenkofluttershy@gmail.com")
            allure.attach(self.page.screenshot(), name='E-mail field filled', attachment_type=allure.attachment_type.PNG)


            self.password_input.fill("193786Az.")
            allure.attach(self.page.screenshot(), name='Password field filled', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='E-mail field is not filled', attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.screenshot(), name='Password field is not filled', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.press_confirm_log_in_button()

    @allure.step('Confirm login')
    def press_confirm_log_in_button(self):
        try:
            self.confirm_log_in_button.click()
            allure.attach(self.page.screenshot(), name='Log in button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Log in button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.page.goto('https://tombriches.com/')
            self.confirm_cookies()

    @allure.step('Confirm cookies')
    def confirm_cookies(self):
        try:
            self.cookie_popup.click()
            allure.attach(self.page.screenshot(), name='Cookie popup confirmed', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Cookie popup is not confirmed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.open_casino_games_side()

    @allure.step('Open casino games side')
    def open_casino_games_side(self):
        try:
            self.casino_games_side.click()
            allure.attach(self.page.screenshot(), name='Casino games side opened', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Casino games side is not opened', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.expect_casino_games_side()

    @allure.step('Expect casino games in sidebar')
    def expect_casino_games_side(self):
        try:
            if (self.top_online_casino_games.is_visible() and
                self.new_casino_games.is_visible() and
                self.slot_casino_games.is_visible() and
                self.megaways_casino_games.is_visible() and
                self.crash_casino_games.is_visible() and
                self.fruit_casino_games.is_visible() and
                self.bonus_games.is_visible()):
                allure.attach(self.page.screenshot(), name='Casino games side is visible', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Casino games side is not visible', attachment_type=allure.attachment_type.PNG)
                raise AssertionError

        finally:
                self.check_top_games()

    @allure.step('Check top games')
    def check_top_games(self):
        try:
            self.top_online_casino_games.click()
            allure.attach(self.page.screenshot(), name='Top online casino games button pressed', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Top online casino games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.check_new_games()

    @allure.step('Check new games')
    def check_new_games(self):
        try:
            self.new_casino_games.click()
            allure.attach(self.page.screenshot(), name='New casino games button pressed', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='New casino games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.check_slot_games()

    @allure.step('Check slot games')
    def check_slot_games(self):
        try:
            self.slot_casino_games.click()
            allure.attach(self.page.screenshot(), name='Slot casino games button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Slot casino games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.check_megaways_games()

    @allure.step('Check megaways games')
    def check_megaways_games(self):
        try:
            self.megaways_casino_games.click()
            allure.attach(self.page.screenshot(), name='Megaways casino games button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Megaways casino games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.check_crash_games()

    @allure.step('Check crash games')
    def check_crash_games(self):
        try:
            self.crash_casino_games.click()
            allure.attach(self.page.screenshot(), name='Crash casino games button pressed', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Crash casino games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.check_fruit_games()

    @allure.step('Check fruit games')
    def check_fruit_games(self):
        try:
            self.fruit_casino_games.click()
            allure.attach(self.page.screenshot(), name='Fruit casino games button pressed', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Fruit casino games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.check_bonus_games()

    @allure.step('Check bonus games')
    def check_bonus_games(self):
        try:
            self.bonus_games.click()
            allure.attach(self.page.screenshot(), name='Bonus games button pressed', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Bonus games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError