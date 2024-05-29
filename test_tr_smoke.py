import allure
import time
import pytest
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
    registration.open_site()
    registration.browser.close()


@allure.suite("Negative registration")
@pytest.mark.parametrize("email", [(e) for e in TestData.test_data])
def test_negativereg(playwright, email):
    negative_reg = NegativeReg(playwright)
    negative_reg.test_negative_registration(playwright, email)
    negative_reg.browser.close()

@allure.suite("Login_Signup via registration form")
def test_login(playwright):
    login = LoginRegistration(playwright)
    login.press_sign_up_button()
    login.browser.close()

@allure.suite("Login_Signup via login button")
def test_login_button(playwright):
  login = LoginButton(playwright)
  login.open_site()
  login.browser.close()

@allure.suite("Logout")
def test_logout(playwright):
    logout = Logout(playwright)
    logout.set_up()
    logout.enter_account()
    logout.browser.close()

@allure.suite("Sidebar")
def test_casino_games_side(playwright):
    casino_games_side = CasinoGamesSide(playwright)
    casino_games_side.set_up()
    casino_games_side.open_casino_games_side()
    casino_games_side.browser.close()
    allure.attach(playwright.screenshot(), name='Casino games side opened', attachment_type=allure.attachment_type.PNG)

@allure.suite("Sidebar")
def test_casino_side_tabs(playwright):
    casino_side_tabs = CasinoSideTabs(playwright)
    casino_side_tabs.set_up()
    casino_side_tabs.open_all_games_tab()
    casino_side_tabs.browser.close()
    allure.attach(playwright.screenshot(), name='Casino side tabs opened', attachment_type=allure.attachment_type.PNG)


@allure.suite("Banners test")
def test_banners(playwright):
    banners = BannersZeroDep(playwright)
    banners.set_up()
    banners.check_banners_position()
    banners.browser.close()


@allure.suite("Games suite")
def test_search_input(playwright):
    search = InputTest(playwright)
    search.set_up()
    search.click_on_input_field()
    search.browser.close()

@allure.suite("Games suite")
def test_demo_mode(playwright):
    search = DemoTest(playwright)
    search.set_up()
    search.click_on_input_field()
    search.browser.close()

@allure.suite("Game suite")
def test_providers_dropdown(playwright):
    providers = ProvidersTest(playwright)
    providers.set_up()
    providers.open_provider_dropdown()
    providers.browser.close()

@allure.suite("Users profile suite")
def test_personal_info_verification(playwright):
    personal_info_verification = PersonalInfVer(playwright)
    personal_info_verification.set_up()
    personal_info_verification.enter_user_account()
    personal_info_verification.browser.close()


@allure.suite("Users profile suite")
def test_security_tab(playwright):
    security_tab = Security(playwright)
    security_tab.set_up()
    security_tab.enter_user_account()
    security_tab.browser.close()

@allure.suite("Users profile suite")
def test_wallet_positive(playwright):
    wallet_positive = PositiveWalletTest(playwright)
    wallet_positive.set_up()
    wallet_positive.enter_user_account()
    wallet_positive.browser.close()

@allure.suite("Users profile suite")
def test_wallet_negative(playwright):
    wallet_negative = NegativeWalletTest(playwright)
    wallet_negative.set_up()
    wallet_negative.enter_user_account()
    wallet_negative.browser.close()

