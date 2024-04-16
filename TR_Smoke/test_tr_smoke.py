import allure
import pytest
from Suites.registration_suite import Registration
from Suites.test_negative_reg import NegativeReg, TestData


@allure.suite("Registration")
def test_registration(page):
    registration = Registration(page)
    registration.open_site()


@allure.suite("Negative registration")
@pytest.mark.parametrize("email", [(e) for e in TestData.test_data])
def test_negativereg(page, email):
    negative_reg = NegativeReg(page)
    negative_reg.test_negative_registration(page, email)