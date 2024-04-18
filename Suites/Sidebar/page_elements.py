
from playwright.sync_api import Page


class PageElements():

    def __init__(self, page: Page):
        self.page = page

    @property
    def log_in_button(self):
        return self.page.get_by_role("button", name="Log in")

    @property
    def email_input(self):
        return self.page.get_by_placeholder("E-mail")

    @property
    def password_input(self):
        return self.page.get_by_placeholder("Password")

    @property
    def confirm_log_in_button(self):
        return self.page.locator("xpath=//button[contains(@class, 'min-w-full') and contains(text(),'Log in')]")

    @property
    def cookie_popup(self):
        return self.page.get_by_role("button", name="ok")

    @property
    def casino_games_side(self):
        return self.page.get_by_text("Casino Games", exact=True)

    @property
    def top_online_casino_games(self):
        return self.page.get_by_label("Top", exact=True)

    @property
    def new_casino_games(self):
        return self.page.get_by_label("New", exact=True)

    @property
    def slot_casino_games(self):
        return self.page.get_by_label("Slots", exact=True)

    @property
    def megaways_casino_games(self):
        return self.page.get_by_label("Megaways", exact=True)

    @property
    def crash_casino_games(self):
        return self.page.get_by_label("Crash", exact=True)

    @property
    def fruit_casino_games(self):
        return self.page.get_by_label("Fruits", exact=True)

    @property
    def bonus_games(self):
        return self.page.get_by_label("Bonus games")

    @property
    def game_card_first(self):
        return self.page.locator("xpath=/html/body/div[2]/div/main/div/div/div[4]/div[1]/div[1]")

    @property
    def game_card_second(self):
        return self.page.locator("xpath=/html/body/div[2]/div/main/div/div/div[4]/div[1]/div[2]")

    @property
    def game_card_third(self):
        return self.page.locator("xpath=/html/body/div[2]/div/main/div/div/div[4]/div[1]/div[3]")


    @property
    def live_games_dropdown(self):
        return self



    #________________________________________________________________

    def game_cards_visible(self):
        return (self.game_card_first.is_visible() and
                self.game_card_second.is_visible() and
                self.game_card_third.is_visible())