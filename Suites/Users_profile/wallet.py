import time
import pdb
import allure
from playwright.sync_api import expect, Page
from Suites.Base.BaseSetUp import BaseSetUp
from Suites.Locators.page_elements import WalletLocators


class PositiveWalletTest(BaseSetUp, WalletLocators):

    def set_up(self):
        try:
            super().set_up()
            allure.attach(self.page.screenshot(), name='Set up passed', attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Set up failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e


    @allure.step("Enter the user's account")
    def enter_user_account(self):
        try:
            self.account_button.click()
            allure.attach(self.page.screenshot(), name='Account button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Account button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.click_on_wallet_tab()



    @allure.step("Click on the wallet tab")
    def click_on_wallet_tab(self):
        try:
            self.wallet_tab.click()
            allure.attach(self.page.screenshot(), name='Wallet button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Wallet button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.enter_deposit_tab()

    @allure.step("Enter the deposit tab")
    def enter_deposit_tab(self):
        try:
            self.deposit_tab.click()
            allure.attach(self.page.screenshot(), name='Deposit button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Deposit button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.choose_mastercard_deposit_method()



    @allure.step("Choose jeton deposit method")
    def choose_mastercard_deposit_method(self):
        try:
            self.mastercard_button.click()
            allure.attach(self.page.screenshot(), name='Jeton deposit method button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Jeton deposit method button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.press_deposit_button()


    @allure.step("Press deposit button")
    def press_deposit_button(self):
        try:
            self.deposit_button.click()
            allure.attach(self.page.screenshot(), name='Deposit button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Deposit button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            time.sleep(30)
            self.expect_mastercard_page()

    @allure.step("Expect mastercard page")
    def expect_mastercard_page(self):
        try:
            expect(self.order_window).to_be_visible(timeout=3000)
            allure.attach(self.page.screenshot(), name='Order window is visible',)
            allure.attach("Order window check successful.", name='Order window check passed', attachment_type=allure.attachment_type.TEXT)
            allure.attach("Order window check successful.", name='Order window check passed', attachment_type=allure.attachment_type.HTML)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Order window is not visible',)
            allure.attach("Order window check failed.", name='Order window check failed', attachment_type=allure.attachment_type.TEXT)
            allure.attach("Order window check failed.", name='Order window check failed', attachment_type=allure.attachment_type.HTML)
            raise AssertionError from e

        finally:
            self.enter_withdrawal_tab()


    @allure.step("Enter withdrawal tab")
    def enter_withdrawal_tab(self):
        try:
            self.page.goto("https://tombriches.com/account/wallet/deposit")
            self.withdrawal_tab.click()
            allure.attach(self.page.screenshot(), name='Withdrawal button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Withdrawal button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.choose_mifinity_withdrawal_method()

    @allure.step("Choose mifinity withdrawal method")
    def choose_mifinity_withdrawal_method(self):
        try:
            self.withdrawal_mifinity_button.click()
            allure.attach(self.page.screenshot(), name='Mifinity withdrawal method button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Mifinity withdrawal method button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.enter_account_name()


    @allure.step("Enter account name")
    def enter_account_name(self):
        try:
            self.account_input.fill("fhawifwaef@gmail.com")
            allure.attach(self.page.screenshot(), name='Account name field filled',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Account name field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.enter_amount()

    @allure.step("Enter amount")
    def enter_amount(self):
        try:
            self.amount_input.fill("230")
            allure.attach(self.page.screenshot(), name='Amount field filled',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Amount field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.press_send_button()


    @allure.step("Press send button")
    def press_send_button(self):
        try:
            self.send_button.click()
            allure.attach(self.page.screenshot(), name='Send button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Send button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.expect_balance_tab_to_appear()


    @allure.step("Expect deposit tab to appear")
    def expect_balance_tab_to_appear(self):
        try:
            expect(self.page.get_by_text("You can have several accounts")).to_be_visible()
            allure.attach(self.page.screenshot(), name='Balance tab is visible',
                          attachment_type=allure.attachment_type.PNG)
            allure.attach("https://tombriches.com/account/wallet/balance", name='Balance tab', attachment_type=allure.attachment_type.TEXT)
            allure.attach("https://tombriches.com/account/wallet/balance", name='Balance tab', attachment_type=allure.attachment_type.HTML)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Balance tab is not visible',
                          attachment_type=allure.attachment_type.PNG)
            allure.attach("https://tombriches.com/account/wallet/balance", name='Balance tab', attachment_type=allure.attachment_type.TEXT)
            allure.attach("https://tombriches.com/account/wallet/balance", name='Balance tab', attachment_type=allure.attachment_type.HTML)
            raise AssertionError from e

        finally:
            self.open_transhistory_tab()


    @allure.step("Open transaction history tab")
    def open_transhistory_tab(self):
        try:
            self.transaction_history_tab.click()
            allure.attach(self.page.screenshot(), name='Transaction history tab pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Transaction history tab is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.expect_transaction_history_to_appear()


    @allure.step("Expect transaction history to appear")
    def expect_transaction_history_to_appear(self):
        try:
            expect(self.cancel_button).to_be_visible()
            allure.attach(self.page.screenshot(), name='Transaction history is visible',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Transaction history is not visible',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.cancel_withdrawal()

    @allure.step("Cancel withdrawal")
    def cancel_withdrawal(self):
        try:
            self.cancel_button.click()
            allure.attach(self.page.screenshot(), name='Cancel button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Cancel button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            expect(self.cancel_button).not_to_be_visible()
            allure.attach(self.page.screenshot(), name='Cancel button is not visible',
                          attachment_type=allure.attachment_type.PNG)


class NegativeWalletTest(BaseSetUp, WalletLocators):

    def __init__(self, page: Page):
        self.page = page

    @allure.title("Go to site")
    def open_site(self):
        try:
            self.page.goto('https://tombriches.com/')
            allure.attach(self.page.screenshot(), name='Page open', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Page opening failed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

    @allure.step('Press on Log in button')
    def press_log_in_button(self):
        try:
            self.log_in_button.click()
            allure.attach(self.page.screenshot(), name='Log in button pressed',
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Log in button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

    @allure.step('Enter credentials')
    def enter_credentials(self):
        try:
            self.email_input.fill("automaton_kprplchzqe09977@kingbilly.xyz")
            allure.attach(self.page.screenshot(), name='E-mail field filled',
                          attachment_type=allure.attachment_type.PNG)

            self.password_input.fill("193786Az()")
            allure.attach(self.page.screenshot(), name='Password field filled',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='E-mail field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.screenshot(), name='Password field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

    @allure.step('Confirm login')
    def press_confirm_log_in_button(self):
        try:
            self.confirm_log_in_button.click()
            time.sleep(5)
            allure.attach(self.page.screenshot(), name='Log in button pressed',
                          attachment_type=allure.attachment_type.PNG)
            self.page.goto('https://tombriches.com/')

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Log in button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

    @allure.step('Confirm cookies')
    def confirm_cookies(self):
        try:
            self.cookie_popup.click()
            allure.attach(self.page.screenshot(), name='Cookie popup confirmed',
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Cookie popup is not confirmed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

    @allure.step("Enter the user's account")
    def enter_user_account(self):
        try:
            self.account_button.click()
            allure.attach(self.page.screenshot(), name='Account button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Account button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.click_on_wallet_tab()

    @allure.step("Click on the wallet tab")
    def click_on_wallet_tab(self):
        try:
            self.wallet_tab.click()
            allure.attach(self.page.screenshot(), name='Wallet button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Wallet button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.enter_withdrawal_tab()

    @allure.step("Enter withdrawal tab")
    def enter_withdrawal_tab(self):
        try:
            self.withdrawal_tab.click()
            allure.attach(self.page.screenshot(), name='Withdrawal button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Withdrawal button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.choose_skrill_withdrawal_method()

    @allure.step("Choose mifinity withdrawal method")
    def choose_skrill_withdrawal_method(self):
        try:
            self.withdrawal_skrill_button.click()
            allure.attach(self.page.screenshot(), name='Mifinity withdrawal method button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Mifinity withdrawal method button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.enter_account_name()

    @allure.step("Enter account name")
    def enter_account_name(self):
        try:
            self.account_input.fill("fhawifwaef@gmail.com")
            allure.attach(self.page.screenshot(), name='Account name field filled',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Account name field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.enter_amount()

    @allure.step("Enter amount")
    def enter_amount(self):
        try:
            self.amount_input.fill("230")
            allure.attach(self.page.screenshot(), name='Amount field filled',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Amount field is not filled',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.press_send_button()

    @allure.step("Press send button")
    def press_send_button(self):
        try:
            self.send_button.click()
            allure.attach(self.page.screenshot(), name='Send button pressed',
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Send button is not pressed',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

        finally:
            self.expect_error_message()

    @allure.step("Expect error message")
    def expect_error_message(self):
        try:
            expect(self.error_message).to_be_visible()
            allure.attach(self.page.screenshot(), name='Error message is visible',
                          attachment_type=allure.attachment_type.PNG)
            allure.attach("https://tombriches.com/account/wallet/deposit", name='Error message', attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            allure.attach(self.page.screenshot(), name='Error message is not visible',
                          attachment_type=allure.attachment_type.PNG)
            allure.attach("https://tombriches.com/account/wallet/deposit", name='Error message', attachment_type=allure.attachment_type.TEXT)
            raise AssertionError from e






