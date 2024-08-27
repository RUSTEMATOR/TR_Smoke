import allure
from playwright.sync_api import expect
import pytest
import time
from Suites.Login_Signup.login import LoginButton, LoginRegistration
from Suites.Login_Signup.logout import Logout
from Suites.Login_Signup.registration_suite import Registration
from Suites.Login_Signup.test_negative_reg import NegativeReg, TestData
from Suites.Sidebar.side_casino_games import CasinoGamesSide
from Suites.Sidebar.side_tabs import CasinoSideTabs
from Suites.Banners.banners import BannersZeroDep
from Suites.Game.game_search import InputTest
from Suites.Game.demo_mode import DemoTest
from Suites.Game.providers_test import ProvidersTest
from Suites.Users_profile.users_profile import PersonalInfVer
from Suites.Users_profile.security import Security
from Suites.Users_profile.wallet import PositiveWalletTest, NegativeWalletTest



@allure.suite("Registration")
def test_registration(playwright):
    registration = Registration(playwright)
    try:
        registration.page.add_locator_handler(registration.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'), registration.handler)

        registration.set_up()
        registration.press_sign_up_button()
        registration.fill_email_field()
        registration.fill_password_field()
        registration.check_18_years()
        registration.press_final_sign_up_button()
        time.sleep(10)
        registration.browser.close()
    except:
        registration.browser.close()
        raise AssertionError("Test failed")


@allure.suite("Negative registration")
@pytest.mark.parametrize("email", [(e) for e in TestData.test_data])
def test_negativereg(playwright, email):
    negative_reg = NegativeReg(playwright)
    try:
        negative_reg.page.add_locator_handler(negative_reg.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'), negative_reg.handler)
        negative_reg.test_negative_registration(email)
        negative_reg.browser.close()
    except:
        negative_reg.browser.close()
        raise AssertionError("Test failed")

@allure.suite("Login_Signup via registration form")
def test_login(playwright):
    login = LoginRegistration(playwright)
    try:
        login.page.add_locator_handler(login.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'), login.handler)
        login.page.add_locator_handler(login.page.locator('div > .deposit-card'), login.handler_deposit_remove)

        login.set_up()
        login.press_log_in_button()
        login.fill_email()
        login.fill_password_field()
        login.click_log_in_button()
        login.enter_account()
        login.check_email()
        login.browser.close()
    except:
        login.browser.close()
        raise AssertionError("Test failed")

@allure.suite("Login_Signup via login button")
def test_login_button(playwright):
    login = LoginButton(playwright)
    try:
        login.page.add_locator_handler(login.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'),login.handler)
        login.page.add_locator_handler(login.page.locator('xpath=//*[@id="depositPromocode"]'),login.handler)
        login.page.add_locator_handler(login.page.locator('div > .deposit-card'), login.handler_deposit_remove)

        login.set_up()
        login.press_log_in_button()
        login.fill_email()
        login.fill_password_field()
        login.click_log_in_button()
        login.enter_account()
        login.check_email()
        login.browser.close()
    except:
        login.browser.close()
        raise AssertionError("Test failed")
# #
@allure.suite("Logout")
def test_logout(playwright):
    logout = Logout(playwright)
    try:
        logout.page.add_locator_handler(logout.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'),logout.handler)
        logout.page.add_locator_handler(logout.page.locator('div > .deposit-card'), logout.handler_deposit_remove)
        logout.set_up()
        logout.enter_account()

        logout.log_out()
    except:
        logout.browser.close()
        raise AssertionError("Test failed")

@allure.suite("Sidebar")
def test_casino_games_side(playwright):
    casino_games_side = CasinoGamesSide(playwright)
    try:
        casino_games_side.page.add_locator_handler(casino_games_side.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'),casino_games_side.handler)
        casino_games_side.page.add_locator_handler(casino_games_side.page.locator('div > .deposit-card'), casino_games_side.handler_deposit_remove)
        casino_games_side.set_up()


        casino_games_side.open_casino_games_side()
        casino_games_side.expect_casino_games_side()

        casino_games_side.check_top_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.check_new_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.check_slot_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.check_megaways_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.check_crash_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.check_fruit_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.check_bonus_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.open_live_games_dropdown()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.check_blackjack_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        # casino_games_side.check_bj_league_games()
        casino_games_side.check_baccarat_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.check_poker_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.check_roulette_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.check_live_dealer_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.check_all_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.check_max_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.check_mid_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

        casino_games_side.check_min_games()
        expect(casino_games_side.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()

    except:
        casino_games_side.browser.close()
        raise AssertionError("Test failed")

@allure.suite("Sidebar")
def test_casino_side_tabs(playwright):
    casino_side_tabs = CasinoSideTabs(playwright)
    try:
        casino_side_tabs.page.add_locator_handler(casino_side_tabs.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'),casino_side_tabs.handler)
        casino_side_tabs.page.add_locator_handler(casino_side_tabs.page.locator('div > .deposit-card'), casino_side_tabs.handler_deposit_remove)
        casino_side_tabs.set_up()


        casino_side_tabs.open_all_games_tab()
        expect(casino_side_tabs.page.locator("xpath=//div//div[contains(@class, 'game-card')][position()=1]").first).to_be_visible()
        casino_side_tabs.open_jackpots_tab()
        time.sleep(3)


        casino_side_tabs.open_promotions_tab()
        casino_side_tabs.open_tournaments_tab()
        casino_side_tabs.open_vip_tab()



        casino_side_tabs.open_support_tab()
        casino_side_tabs.browser.close()
    except:
        casino_side_tabs.browser.close()
        raise AssertionError("Test failed")


@allure.suite("Banners test")
def test_banners(playwright):
    banners = BannersZeroDep(playwright)
    try:
        banners.page.add_locator_handler(banners.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'),banners.handler)
        banners.page.add_locator_handler(banners.page.locator('div > .deposit-card'), banners.handler_deposit_remove)
        banners.set_up()

        # expect(banners.first_welcome_banner).to_be_visible()
        expect(banners.second_cashback_banner).to_be_visible()
        expect(banners.third_up_to_100_fs_banner).to_be_visible()
        expect(banners.fourth_tomb_treasure_banner).to_be_visible()
        expect(banners.fifth_jackpot_banner).to_be_visible()
        expect(banners.sixth_first_loyalty_banner).to_be_visible()
        expect(banners.seventh_winners_banner).to_be_visible()
        expect(banners.eighth_tournament_banner).to_be_visible()
        expect(banners.ninth_tournament_banner).to_be_visible()
        banners.browser.close()
    except:
        banners.browser.close()
        raise AssertionError("Test failed")


@allure.suite("Games suite")
def test_search_input(playwright):
    search = InputTest(playwright)
    try:
        search.page.add_locator_handler(search.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'),search.handler)
        search.page.add_locator_handler(search.page.locator('div > .deposit-card'), search.handler_deposit_remove)
        search.set_up()

        search.click_on_input_field()
        search.enter_game_name()
        search.press_game_banner()
        search.press_play_button()
        search.close_ingame_modal()
        search.browser.close()
    except:
        search.browser.close()
        raise AssertionError("Test failed")

@allure.suite("Games suite")
def test_demo_mode(playwright):
    search = DemoTest(playwright)
    try:
        search.page.add_locator_handler(search.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'), search.handler)
        search.page.add_locator_handler(search.page.locator('div > .deposit-card'), search.handler_deposit_remove)
        search.set_up()

        search.click_on_input_field()
        search.click_on_input_field()
        search.enter_game_name()
        search.press_game_banner()
        search.browser.close()
    except:
        search.browser.close()
        raise AssertionError("Test failed")

@allure.suite("Game suite")
def test_providers_dropdown(playwright):
    providers = ProvidersTest(playwright)
    try:
        providers.page.add_locator_handler(providers.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'), providers.handler)
        providers.page.add_locator_handler(providers.page.locator('div > .deposit-card'), providers.handler_deposit_remove())
        providers.set_up()
        providers.open_provider_dropdown()
        providers.check_providers()
        providers.browser.close()
    except:
        providers.browser.close()
        raise AssertionError("Test failed")

@allure.suite("Users profile suite")
def test_personal_info_verification(playwright):
    personal_info_verification = PersonalInfVer(playwright)
    try:
        personal_info_verification.page.add_locator_handler(personal_info_verification.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'), personal_info_verification.handler)
        personal_info_verification.page.add_locator_handler(personal_info_verification.page.locator('div > .deposit-card'), personal_info_verification.handler_deposit)
        personal_info_verification.set_up()
        personal_info_verification.enter_user_account()
        personal_info_verification.check_filled_inputs()
        personal_info_verification.check_email_copy()
        personal_info_verification.check_gender_change()
        personal_info_verification.switch_to_verification_tab()
        personal_info_verification.check_the_page()
        personal_info_verification.browser.close()
    except:
        personal_info_verification.browser.close()
        raise AssertionError("Test failed")


@allure.suite("Users profile suite")
def test_security_tab(playwright):
    security_tab = Security(playwright)
    try:
        security_tab.page.add_locator_handler(security_tab.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'), security_tab.handler)
        security_tab.page.add_locator_handler(security_tab.page.locator('div > .deposit-card'), security_tab.handler_deposit)
        security_tab.set_up()
        security_tab.enter_user_account()
        security_tab.switch_to_security_tab()
        security_tab.negative_enter_old_password()
        security_tab.negative_enter_new_password()
        security_tab.negative_enter_confirm_password()
        security_tab.negative_click_save_button()
        security_tab.expect_error_popup()
        security_tab.negative_wrong_repeated_newpassword()
        security_tab.positive_change_password()
        security_tab.cleanup()
        security_tab.browser.close()
    except:
        security_tab.browser.close()
        raise AssertionError("Test failed")

@allure.suite("Users profile suite")
def test_wallet_positive(playwright):
    wallet_positive = PositiveWalletTest(playwright)
    try:
        wallet_positive.page.add_locator_handler(wallet_positive.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'), wallet_positive.handler)
        wallet_positive.set_up()
        wallet_positive.enter_user_account()
        wallet_positive.click_on_wallet_tab()
        wallet_positive.enter_deposit_tab()
        wallet_positive.check_deposit_methods()
        wallet_positive.page.pause()
        # wallet_positive.expect_transfer_to_banking()
        wallet_positive.check_withdrawal_methods()
        wallet_positive.browser.close()
    except:
        wallet_positive.browser.close()
        raise AssertionError("Test failed")

# @allure.suite("Users profile suite")
# def test_wallet_negative(playwright):
#     wallet_negative = NegativeWalletTest(playwright)
#     try:
#         wallet_negative.page.add_locator_handler(wallet_negative.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'), wallet_negative.handler)
#         wallet_negative.page.add_locator_handler(wallet_negative.page.locator('div > .deposit-card'),wallet_negative.handler_deposit)
#         wallet_negative.set_up()
#         wallet_negative.enter_user_account()
#         wallet_negative.click_on_wallet_tab()
#         wallet_negative.enter_withdrawal_tab()
#         wallet_negative.choose_skrill_withdrawal_method()
#         wallet_negative.enter_account_name()
#         wallet_negative.enter_amount()
#         wallet_negative.press_send_button()
#         wallet_negative.expect_error_message()
#         wallet_negative.browser.close()
#     except:
#         wallet_negative.browser.close()
#         raise AssertionError("Test failed")
# #
