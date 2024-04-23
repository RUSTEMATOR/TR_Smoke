import allure
import pytest
from playwright.sync_api import Page
from Suites.BaseSetUp import BaseSetUp
from Suites.Locators.page_elements import GameSuitLocators


class InputTest(BaseSetUp, GameSuitLocators):
    
    def set_up(self):
        return super().set_up()

    @allure.step

