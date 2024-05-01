import allure
import time
from Suites.Locators.page_elements import PageElementsTabs, SearchFunctions


class CasinoSideTabs(SearchFunctions):

    @allure.title("Go to site")
    def open_site(self):
        try:
            self.page.goto('https://tombriches.com/')
            allure.attach(self.page.screenshot(), name='Page open', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Page opening failed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.press_log_in_button()

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
        finally:
            self.enter_credentials()

    @allure.step('Enter credentials')
    def enter_credentials(self):
        try:
            self.email_input.fill("samoilenkofluttershy@gmail.com")
            allure.attach(self.page.screenshot(), name='E-mail field filled',
                          attachment_type=allure.attachment_type.PNG)

            self.password_input.fill("193786Az.")
            allure.attach(self.page.screenshot(), name='Password field filled',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='E-mail field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.screenshot(), name='Password field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.press_confirm_log_in_button()

    @allure.step('Confirm login')
    def press_confirm_log_in_button(self):
        try:
            self.confirm_log_in_button.click()
            allure.attach(self.page.screenshot(), name='Log in button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Log in button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(10)
            self.page.goto('https://tombriches.com/')
            self.confirm_cookies()

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
        finally:
            self.open_all_games_tab()

    @allure.step('Open all games tab')
    def open_all_games_tab(self):
        try:
            self.all_games_btn.click()
            allure.attach(self.page.screenshot(), name='All games button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='All games button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present',
                              attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present',
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.open_jackpots_tab()

    @allure.step('Open jackpots tab')
    def open_jackpots_tab(self):
        try:
            self.jackpots_tab.click()
            allure.attach(self.page.screenshot(), name='Jackpots button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Jackpots button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            time.sleep(3)
            if (self.text_on_jackpot_pg_visible() and
                    self.game_cards_visible_jp()):
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present',
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.open_promotions_tab()


    @allure.step('Open promotions tab')
    def open_promotions_tab(self):
        try:
            self.promotions_tab.click()
            allure.attach(self.page.screenshot(), name='Promotions button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Promotions button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(3)
            if self.promo_banners_visible():
                allure.attach(self.page.screenshot(), name='Promotions banners are present')
                pass
            else:
                allure.attach(self.page.screenshot(), name='Promotions banners are not present')
                raise AssertionError

            self.open_tournaments_tab()

    @allure.step('Open tournaments tab')
    def open_tournaments_tab(self):
        try:
            self.tournaments_tab.click()
            allure.attach(self.page.screenshot(), name='Tournaments button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Tournaments button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(3)
            if self.tournament_banners_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present',
                              attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present',
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.open_loyalty_tab()

    @allure.step('Open loyalty tab')
    def open_loyalty_tab(self):
        try:
            self.loyalty_tab.click()
            allure.attach(self.page.screenshot(), name='Loyalty button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Loyalty button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(3)
            if self.loyalty_banners_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present',
                              attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present',
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError

    @allure.step('Open support tab')
    def open_support_tab(self):
        try:
            self.support_tab.click()
            allure.attach(self.page.screenshot(), name='Support button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Support button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.page.frame_locator("iframe[name=\"intercom-messenger-frame\"]").get_by_test_id("messages").click()
            self.page.frame_locator("iframe[name=\"intercom-messenger-frame\"]").get_by_test_id(
                "send-a-message-button").click()

            if (self.page.frame_locator("iframe[name=\"intercom-messenger-frame\"]").get_by_placeholder(
                    "Write your message...").is_visible() and
                    self.page.frame_locator("iframe[name=\"intercom-messenger-frame\"]").get_by_placeholder(
                        "   email@example.com").is_visible()):
                pass
            else:
                allure.attach(self.page.screenshot(), name='Support button is not pressed',
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError
