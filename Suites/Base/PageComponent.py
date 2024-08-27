from abc import ABC, abstractmethod
from playwright.sync_api import Page, Playwright


class PageComponent(ABC):
    @abstractmethod
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False,
                                                  proxy={
                                                      'server': 'http://138.197.150.103:8090',
                                                      'username': 'kbc',
                                                      'password': '347SP&Uwqt!2xZ7w',
                                                  })
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
