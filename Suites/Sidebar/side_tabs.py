import allure
import time
from playwright.sync_api import expect
from Suites.Locators.page_elements import PageElementsTabs, SearchFunctions
from Suites.Base.BaseSetUp import BaseSetUp


class CasinoSideTabs(SearchFunctions, BaseSetUp):

    def set_up(self):
        try:
            super().set_up()
        except Exception as e:
            raise AssertionError from e

        finally:
            self.open_all_games_tab()

    @allure.step('Open all games tab')
    def open_all_games_tab(self):
        try:
            self.all_games_btn.click()
            allure.attach(self.page.screenshot(), name='All games button pressed',
                          attachment_type=allure.attachment_type.PNG)

            expect(self.game_card_first).to_be_visible()
            expect(self.game_card_second).to_be_visible()
            expect(self.game_card_third).to_be_visible()


        except Exception as e:
            allure.attach(self.page.screenshot(), name='All games button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e




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


    @allure.step('Open promotions tab')
    def open_promotions_tab(self):
        try:
            self.promotions_tab.click()
            allure.attach(self.page.screenshot(), name='Promotions button pressed',
                          attachment_type=allure.attachment_type.PNG)

            time.sleep(3)
            if self.promo_banners_visible():
                allure.attach(self.page.screenshot(), name='Promotions banners are present')
                pass
            else:
                allure.attach(self.page.screenshot(), name='Promotions banners are not present')
                raise AssertionError

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Promotions button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e


    @allure.step('Open tournaments tab')
    def open_tournaments_tab(self):
        try:
            self.tournaments_tab.click()
            allure.attach(self.page.screenshot(), name='Tournaments button pressed',
                          attachment_type=allure.attachment_type.PNG)

            time.sleep(3)
            if self.tournament_banners_visible():
                allure.attach(self.page.screenshot(), name='Banners in the tab are present',
                              attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Banners in the tab are not present',
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Tournaments button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e


    @allure.step('Open loyalty tab')
    def open_vip_tab(self):
        try:
            self.loyalty_tab.click()
            allure.attach(self.page.screenshot(), name='Loyalty button pressed',
                          attachment_type=allure.attachment_type.PNG)

            time.sleep(3)
            if self.loyalty_banners_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present',
                              attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present',
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Loyalty button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e


    @allure.step('Open support tab')
    def open_support_tab(self):
        try:
            self.support_iframe.click()
            allure.attach(self.page.screenshot(), name='Support button pressed',
                          attachment_type=allure.attachment_type.PNG)

            self.page.frame_locator("iframe[name=\"intercom-messenger-frame\"]").get_by_test_id("messages").click()
            self.page.frame_locator("iframe[name=\"intercom-messenger-frame\"]").get_by_test_id("send-a-message-button").click()
            allure.attach(self.page.screenshot(), name='Messages open', attachment_type=allure.attachment_type.PNG)
            expect(self.page.frame_locator("iframe[name=\"intercom-messenger-frame\"]").locator('xpath=//input[@type="email"]')).to_be_visible()
            self.page.frame_locator("iframe[name=\"intercom-messenger-frame\"]").locator('xpath=//input[@type="email"]').fill('whoami@gmail.com')
            expect(self.page.frame_locator("iframe[name=\"intercom-messenger-frame\"]").locator('xpath=//input[@type="email"]')).to_have_value('whoami@gmail.com')

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Support button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
