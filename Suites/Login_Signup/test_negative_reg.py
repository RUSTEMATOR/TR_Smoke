from playwright.sync_api import Playwright, sync_playwright, Page
import pytest
import allure
import time
from contextlib import contextmanager



@contextmanager
def allure_step(name, page):
    try:
        yield
    except AssertionError as e:
        raise AssertionError(f"{name} failed: {str(e)}")


class TestData():
    from playwright.sync_api import Page
    # Define the list of test data
    test_data = [
        "example#kbc.pp.ua",
        "example@kbc.pp-ua",
        "example@kbc.pp_ua",
        "example@kbc.pp..ua",
        "",  # Empty value
        "exämple@kbc.pp.ua",
        "example@softs_wis..com",
        "example.softswis.com",
        "example@@softswis.com",
        "example@soft swis.com",
        "example@softswis..com",
        "example@"
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
                                                  })
        self.context = self.browser.new_context()
        self.page = self.context.new_page()


    @allure.title("Negative emails_check")
    # Define the test function
    @pytest.mark.parametrize("email", [(e) for e in TestData.test_data])
    def test_negative_registration(self, page: Page, email: str) -> None:
        self.page.goto("https://tombriches.com/")
        self.page.get_by_role("button", name="Sign up").click()
        self.page.get_by_placeholder("E-mail").click()
        self.page.get_by_placeholder("E-mail").fill(email)
        self.page.get_by_placeholder("Password").click()
        self.page.get_by_placeholder("Password").fill("193786Az()")
        self.page.locator("#is18-checkbox").check()
        self.page.locator("form").get_by_role("button", name="Sign up").click()

        time.sleep(5)

        if self.page.locator("form").get_by_role("button", name="Sign up").is_visible():
            pass
        else:
            raise AssertionError(f"{email} is registered")

