import time

import allure

from Suites.Base.BaseSetUp import BaseSetUp
from Suites.Locators.page_elements import GameSuitLocators


class ProvidersTest(BaseSetUp, GameSuitLocators):

    def set_up(self):
        try:
            super().set_up()
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Set up failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

    @allure.step("Open Provider dropdown")
    def open_provider_dropdown(self):
        try:
            self.providers_dropdown.click()
            allure.attach(self.page.screenshot(), name='Provider dropdown opened', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Provider dropdown is not opened', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(4)
            self.check_providers()


    @allure.step('Check providers')
    def check_providers(self):

        expected_providers = ["Spribe", "Pragmatic Play Live", "Betsoft"]
        invisible_providers = []

        try:
            for provider_name in expected_providers:
                provider_selector = f"xpath=//p[contains(@class, 'text-[16px]') and contains(text(), '{provider_name}')]"
                if not self.page.locator(provider_selector).is_visible():
                    # If the provider is not visible, add it to the list of invisible providers
                    invisible_providers.append(provider_name)
                    allure.attach(self.page.screenshot(), name=f'{provider_name} is not visible',
                                  attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            # Instead of raising an exception immediately, add the provider to a list of failures
            invisible_providers.append(provider_name)
            allure.attach(self.page.screenshot(), name=f'{provider_name} is not visible',
                          attachment_type=allure.attachment_type.PNG)

        if invisible_providers:
            raise AssertionError(f"Providers not visible: {', '.join(invisible_providers)}")

