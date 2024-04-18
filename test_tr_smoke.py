import allure
import pytest
from Suites.registration_suite import Registration
from Suites.test_negative_reg import NegativeReg, TestData
from Suites.login import LoginRegistration, LoginButton
from Suites.logout import Logout
from Suites.Sidebar.page_elements import PageElements
from Suites.Sidebar.side_casino_games import CasinoGamesSide

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
# @allure.suite("Login via registration form")
# def test_login(page):
#     login = LoginRegistration(page)
#     login.open_site()
#
# @allure.suite("Login via login button")
# def test_login_button(page):
#   login = LoginButton(page)
#   login.open_site()
#
# @allure.suite("Logout")
# def test_logout(page):
#     logout = Logout(page)
#     logout.open_site()

@allure.suite("Sidebar")
def test_casino_games_side(page):
    casino_games_side = CasinoGamesSide(page)
    casino_games_side.open_site()
    allure.attach(page.screenshot(), name='Casino games side opened', attachment_type=allure.attachment_type.PNG)