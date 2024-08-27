from playwright.sync_api import Playwright, sync_playwright, Page, expect
import pytest
import allure
import time
from contextlib import contextmanager
from Suites.Base import BaseSetUp


@contextmanager
def allure_step(name):
    try:
        yield
    except AssertionError as e:
        raise AssertionError(f"{name} failed: {str(e)}")


class TestData():
    # Define the list of test data
    test_data = [
        "plainaddress",
        "#@%^%#$@#$@#.com",
        "@example.com",
        "Joe Smith <email@example.com>",
        "email.example.com",
        "email@example@example.com",
        ".email@example.com",
        "email.@example.com",
        "email..email@example.com",
        "あいうえお@example.com@",
        "email@example.com (Joe Smith)",
        "email@@example.com",
        "email@-example.com",
        "email@example.web",
        "email@111.222.333.44444",
        "email@example..com",
        "Abc..123@example.com"
    ]

    links = [
        "tombriches.com"
    ]


class NegativeReg(TestData):

    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=True,
                                                   proxy={
                                                       'server': 'http://138.197.150.103:8090',
                                                       'username': 'kbc',
                                                       'password': '347SP&Uwqt!2xZ7w',
                                                   }
        )
        self.context = self.browser.new_context()
        self.page = self.context.new_page()


    def handler(self):
        self.page.reload()

    @allure.title("Negative emails_check")
    # Define the test function
    @pytest.mark.parametrize("email", [(e) for e in TestData.test_data], BaseSetUp)
    def test_negative_registration(self, email: str) -> None:
        deposit_button = self.page.locator("xpath=//button[@title='deposit' and contains(@class, 'btn button-primary !min-w-full')]")


        self.page.goto("https://tombriches.com/")
        self.page.get_by_role("button", name="Sign up").click()
        self.page.get_by_placeholder("E-mail").click()
        self.page.get_by_placeholder("E-mail").fill(email)
        self.page.get_by_placeholder("Password").click()
        self.page.get_by_placeholder("Password").fill("193786Az()")
        self.page.locator("#is18-checkbox").check()
        self.page.locator("form").get_by_role("button", name="Sign up").click()

        time.sleep(10)

        if self.page.locator("form").get_by_role("button", name="Sign up").is_visible():
            pass
        else:
            raise AssertionError(f"{email} is registered")

        expect(deposit_button).not_to_be_visible()
