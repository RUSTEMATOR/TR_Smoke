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

# @allure.suite("Registration")
# def test_registration(page):
#     registration = Registration(page)
#     registration.open_site()
#
#
# @allure.suite("Negative registration")
# @pytest.mark.parametrize("email", [(e) for e in TestData.test_data])
# def test_negativereg(page, email):
#     negative_reg = NegativeReg(page)
#     negative_reg.test_negative_registration(page, email)
#
# @allure.suite("Login_Signup via registration form")
# def test_login(page):
#     login = LoginRegistration(page)
#     login.open_site()
#
# @allure.suite("Login_Signup via login button")
# def test_login_button(page):
#   login = LoginButton(page)
#   login.open_site()
#
# @allure.suite("Logout")
# def test_logout(page):
#     logout = Logout(page)
#     logout.open_site()
#
# @allure.suite("Sidebar")
# def test_casino_games_side(page):
#     casino_games_side = CasinoGamesSide(page)
#     casino_games_side.open_site()
#     allure.attach(page.screenshot(), name='Casino games side opened', attachment_type=allure.attachment_type.PNG)
#
# @allure.suite("Sidebar")
# def test_casino_side_tabs(page):
#     casino_side_tabs = CasinoSideTabs(page)
#     casino_side_tabs.open_site()
#     allure.attach(page.screenshot(), name='Casino side tabs opened', attachment_type=allure.attachment_type.PNG)
#
#
# @allure.suite("Banners test")
# def test_banners(page):
#     banners = BannersZeroDep(page)
#     banners.set_up()
#     banners.check_banners_position()
#
#
# @allure.suite("Games suite")
# def test_search_input(page):
#     search = InputTest(page)
#     search.set_up()
#     search.click_on_input_field()
#
# @allure.suite("Games suite")
# def test_demo_mode(page):
#     search = DemoTest(page)
#     search.set_up()
#     search.click_on_input_field()

# @allure.suite("Game suite")
# def test_providers_dropdown(page):
#     providers = ProvidersTest(page)
#     providers.set_up()
#     providers.open_provider_dropdown()

@allure.suite("Users profile suite")
def test_personal_info_verification(page):
    personal_info_verification = PersonalInfVer(page)
    personal_info_verification.set_up()
    personal_info_verification.enter_user_account()