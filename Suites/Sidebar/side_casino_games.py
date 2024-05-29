import allure
import time
from Suites.Locators.page_elements import PageElementsGames, SearchFunctions
from Suites.Base.BaseSetUp import BaseSetUp


class CasinoGamesSide(SearchFunctions, BaseSetUp):

    def set_up(self):
        try:
            super().set_up()
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Set up failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

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

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Casino games side is not visible', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

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

            self.open_live_games_dropdown()

    @allure.step('Open Live games dropdown')
    def open_live_games_dropdown(self):
        try:
            self.live_games_dropdown.click()
            allure.attach(self.page.screenshot(), name='Live games dropdown opened', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Live games dropdown is not opened', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.check_blackjack_games()

    @allure.step('Check Blackjack games')
    def check_blackjack_games(self):
        try:
            self.blackjack_games.click()
            allure.attach(self.page.screenshot(), name='Blackjack games button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Blackjack games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.check_bj_league_games()

    @allure.step('Check BJ league games')
    def check_bj_league_games(self):
        try:
            self.bj_league_games.click()
            allure.attach(self.page.screenshot(), name='BJ league games button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='BJ league games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.check_baccarat_games()

    @allure.step('Check Baccarat games')
    def check_baccarat_games(self):
        try:
            self.baccarat_games.click()
            allure.attach(self.page.screenshot(), name='Baccarat games button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Baccarat games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.check_poker_games()

    @allure.step('Check Poker games')
    def check_poker_games(self):
        try:
            self.poker_games.click()
            allure.attach(self.page.screenshot(), name='Poker games button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Poker games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.check_roulette_games()

    @allure.step('Check Roulette games')
    def check_roulette_games(self):
        try:
            self.roulette_games.click()
            allure.attach(self.page.screenshot(), name='Roulette games button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Roulette games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.check_live_dealer_games()

    @allure.step('Check Live Dealer games')
    def check_live_dealer_games(self):
        try:
            self.live_dealer_games.click()
            allure.attach(self.page.screenshot(), name='Live Dealer games button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Live Dealer games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError


    @allure.step('Open Jackpot dropdown')
    def check_all_games(self):
        try:
            self.jackpot_dropdown.click()
            allure.attach(self.page.screenshot(), name='Jackpot dropdown opened', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Jackpot dropdown is not opened', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e
        finally:
            self.check_max_games()

    @allure.step('Check Max games')
    def check_max_games(self):
        try:
            self.max_games.click()
            allure.attach(self.page.screenshot(), name='Max games button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Max games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.check_mid_games()

    @allure.step('Check Mid games')
    def check_mid_games(self):
        try:
            self.mid_games.click()
            allure.attach(self.page.screenshot(), name='Mid games button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Mid games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError

            self.check_min_games()

    @allure.step('Check Mini games')
    def check_min_games(self):
        try:
            self.min_games.click()
            allure.attach(self.page.screenshot(), name='Mini games button pressed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Mini games button is not pressed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(2)
            if self.game_cards_visible():
                allure.attach(self.page.screenshot(), name='Games in the category are present', attachment_type=allure.attachment_type.PNG)
                pass
            else:
                allure.attach(self.page.screenshot(), name='Games in the category are not present', attachment_type=allure.attachment_type.PNG)
                raise AssertionError
