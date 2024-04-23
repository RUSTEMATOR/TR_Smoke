
from playwright.sync_api import Page
from Suites.BaseSetUp import BaseSetUp




class PageElementsGames:

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

    # ________________________________________________________________

    @property
    def live_games_dropdown(self):
        return self.page.get_by_text("Live Games", exact=True)
    @property
    def blackjack_games(self):
        return self.page.get_by_label("Blackjack")

    @property
    def bj_league_games(self):
        return self.page.get_by_label("Bj League")

    @property
    def baccarat_games(self):
        return self.page.get_by_label("Baccarat", exact=True)

    @property
    def poker_games(self):
        return self.page.get_by_label("Poker", exact=True)

    @property
    def roulette_games(self):
        return self.page.get_by_label("Roulette", exact=True)

    @property
    def live_dealer_games(self):
        return self.page.get_by_label("Live Dealer Shows")

    @property
    def jackpot_dropdown(self):
        return self.page.get_by_text("Jackpot Games")

    @property
    def max_games(self):
        return self.page.get_by_label("Max")

    @property
    def mid_games(self):
        return self.page.get_by_label("Mid", exact=True)

    @property
    def mini_games(self):
        return self.page.get_by_label("Mini", exact=True)



class PageElementsTabs(PageElementsGames):

    @property
    def all_games_btn(self):
        return self.page.get_by_label("All games")

    @property
    def jackpots_tab(self):
        return self.page.get_by_label("Jackpots", exact=True)

    @property
    def live_tab(self):
        return self.page.get_by_label("Live")

    @property
    def promotions_tab(self):
        return self.page.get_by_label("Promotions")

    @property
    def tournaments_tab(self):
        return self.page.get_by_label("Tournaments")

    @property
    def loyalty_tab(self):
        return self.page.get_by_label("Loyalty program")

    @property
    def support_iframe(self):
        return self.page.get_by_text("Support", exact=True)

    @property
    def game_card_first_jp(self):
        return self.page.locator('xpath=//*[@id="Tombriches"]/main/div/div/div[2]/div[1]/div/div[1]/div[1]/img')

    @property
    def game_card_second_jp(self):
        return self.page.locator('xpath=//*[@id="Tombriches"]/main/div/div/div[2]/div[2]/div/div[1]/div[1]/img')

    @property
    def game_card_third_jp(self):
        return self.page.locator('xpath=//*[@id="Tombriches"]/main/div/div/div[2]/div[3]/div/div[1]/div[1]/img')

class SearchFunctions(BaseSetUp, PageElementsTabs):

    def game_cards_visible_jp(self):
        return (self.game_card_first_jp.is_visible() and
                self.game_card_second_jp.is_visible() and
                self.game_card_third_jp.is_visible())

    def game_cards_visible(self):
        return (self.game_card_first.is_visible() and
                self.game_card_second.is_visible() and
                self.game_card_third.is_visible())

    def promo_banners_visible(self):
        return (self.page.get_by_text("Welcome Pack€/$2000 + 200").is_visible() and
                self.page.get_by_text("Cashback up to 15%Get from 10").is_visible() and
                self.page.get_by_text("1st Deposit Bonus100% up to").is_visible() and
                self.page.get_by_text("2nd Deposit Bonus50% up to").is_visible() and
                self.page.get_by_text("3rd Deposit Bonus25% up to").is_visible() and
                self.page.get_by_text("4th Deposit Bonus25% up to").is_visible() and
                self.page.get_by_text("Pharaoh’s Fortune Spins!Up to").is_visible() and
                self.page.get_by_text("Tomb Treasure!50% up to €/$").is_visible())

    def text_on_jackpot_pg_visible(self):
        return (self.page.get_by_text("How to win Jackpots?").is_visible() and
                self.page.get_by_text("Сhoose your game").is_visible() and
                self.page.get_by_text("all games qualify").is_visible() and
                self.page.get_by_text("Be online").is_visible() and
                self.page.get_by_text("just play your favorite games").is_visible() and
                self.page.get_by_text("Make a fortune").is_visible() and
                self.page.get_by_text("every bet can be the winning").is_visible() and
                self.page.get_by_text("How can I participate?").is_visible() and
                self.page.get_by_text("No extra effort required,").is_visible() and
                self.page.get_by_text("How do I get the jackpot?").is_visible() and
                self.page.get_by_text("Jackpots are drawn randomly").is_visible() and
                self.page.get_by_text("The winner is selected").is_visible() and
                self.page.get_by_text("mini: 500-1500 euro,").is_visible() and
                self.page.get_by_text("mid: 7000-10000 euro,").is_visible() and
                self.page.get_by_text("max: 35000-45000 euro.").is_visible() and
                self.page.get_by_text("You can keep track of Jackpot").is_visible() and
                self.page.get_by_text("How to increase the chances").is_visible() and
                self.page.get_by_text("The most important thing is").is_visible() and
                self.page.get_by_text("1) Confirm your email in").is_visible() and
                self.page.get_by_text("2) Install the TombRiches app").is_visible() and
                self.page.get_by_role("button", name="deposit & play").is_visible())

    def tournament_banners_visible(self):
        return (self.page.locator("div:nth-child(1) > .aspect-\\[40\\/29\\]").is_visible() and
                self.page.locator("div:nth-child(2) > .aspect-\\[40\\/29\\]").is_visible() and
                self.page.locator("div:nth-child(3) > .aspect-\\[40\\/29\\]").is_visible())

    def loyalty_banners_visible(self):
        return (self.page.locator(".border-").first.is_visible() and
                self.page.locator(".max-w-\\[1100px\\] > div:nth-child(2)").is_visible() and
                self.page.locator(".max-w-\\[1100px\\] > div:nth-child(3)").is_visible() and
                self.page.locator(".max-w-\\[1100px\\] > div:nth-child(4)").is_visible() and
                self.page.locator(".max-w-\\[1100px\\] > div:nth-child(5)").is_visible() and
                self.page.locator(".max-w-\\[1100px\\] > div:nth-child(6)").is_visible() and
                self.page.locator(".max-w-\\[1100px\\] > div:nth-child(7)").is_visible() and
                self.page.locator(".max-w-\\[1100px\\] > div:nth-child(8)").is_visible() and
                self.page.locator('xpath=//*[@id="Tombriches"]/main/div/div/div[3]/div/div[9]').is_visible())

class BannersLocatorsZeroDep(BaseSetUp):



    @property
    def first_welcome_banner(self):
        return self.page.locator("xpath=//h3[contains(@class, 'text-mp_banner_vip_title') "
                                 "and contains(text(), 'Welcome Pack')]")

    @property
    def second_cashback_banner(self):
        return self.page.get_by_role("heading", name="CASHBACK UP TO 15%")

    @property
    def third_up_to_100_fs_banner(self):
        return self.page.get_by_role("heading", name="UP TO 100 FS")

    @property
    def fourth_tomb_treasure_banner(self):
        return self.page.get_by_role("heading", name="TOMB TREASURE!")

    @property
    def fifth_jackpot_banner(self):
        return self.page.get_by_role("button", name="get jackpot")

    @property
    def sixth_first_loyalty_banner(self):
        return self.page.locator("xpath=//div[contains(@class, 'swiper-slide') and contains(@class, '!flex')][6]")

    @property
    def seventh_winners_banner(self):
        return self.page.locator("xpath=//div[contains(@class, 'swiper-slide') and contains(@class, '!flex')][7]")

    @property
    def eighth_tournament_banner(self):
        return self.page.locator("xpath=//div[contains(@class, 'swiper-slide') and contains(@class, '!flex')][8]")

    @property
    def ninth_tournament_banner(self):
        return self.page.locator("xpath=//div[contains(@class, 'swiper-slide') and contains(@class, '!flex')][9]")


class GameSuitLocators(BaseSetUp):
    
    @property
    def search_field(self):
        return self.page.locator("xpath=//input[@placeholder='Enter game name']")
    
    @property
    def first_game_card(self):
        return self.page.locator("xpath=//div[contains(@class, 'game-card') and contains(@class, 'z-0')][1]").first
    
    @property
    def play_button(self):
        return self.page.locator("xpath=//button[@title = 'play' and contains(@class, 'btn') and contains(@class, 'button-primary')][1]").first
    
    @property
    def ingame_close_button(self):
        return self.page.locator("xpath=//button[@title='close' and contains(@class, 'btn button-secondary max-w-[150px]') and text()='close']")
    
    @property
    def sound_no_button(self):
        return self.page.locator("xpath=//div[contains(@class, 'button no')]")
    
    @property
    def spin_button(self):
        return self.page.frame_locator("#game-iframe").frame_locator("iframe").locator("#btn-spinDesktop canvas").nth(1).click(position={"x":56,"y":52})
    
    @property
    def warning(self):
        return self.page.locator("xpath=//div[@id = 'modal_window']")