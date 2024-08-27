import allure
import time
from Suites.Base.BaseSetUp import BaseSetUp
from Suites.Locators.page_elements import BannersLocatorsZeroDep


class Locators(BannersLocatorsZeroDep):
    def banner_zero_dep(self):
        return [
            self.first_welcome_banner,
            self.second_cashback_banner,
            self.third_up_to_100_fs_banner,
            self.fourth_tomb_treasure_banner,
            self.fifth_jackpot_banner,
            self.sixth_first_loyalty_banner,
            self.seventh_winners_banner,
            self.eighth_tournament_banner,
            self.ninth_tournament_banner
        ]


class BannersZeroDep(BaseSetUp, Locators):
    @allure.step('Set up')
    def set_up_func(self):
        try:
            super().set_up()
            time.sleep(20)
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Set up failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e

    @allure.step('Check banners position')
    def check_banners_position(self):
        banners = [
            ("first_welcome_banner", self.first_welcome_banner),
            ("second_cashback_banner", self.second_cashback_banner),
            ("third_up_to_100_fs_banner", self.third_up_to_100_fs_banner),
            ("fourth_tomb_treasure_banner", self.fourth_tomb_treasure_banner),
            ("fifth_jackpot_banner", self.fifth_jackpot_banner),
            ("sixth_first_loyalty_banner", self.sixth_first_loyalty_banner),
            ("seventh_winners_banner", self.seventh_winners_banner),
            ("eighth_tournament_banner", self.eighth_tournament_banner),
            ("ninth_tournament_banner", self.ninth_tournament_banner)
        ]
        visible_banners = []
        for name, banner in banners:
            if banner.is_visible():
                visible_banners.append(name)
                allure.attach(f"{name} is visible", name=f"{name} visibility",
                              attachment_type=allure.attachment_type.TEXT)
                allure.attach(self.page.screenshot(), name=f"{name} screenshot", attachment_type=allure.attachment_type.PNG)
                allure.attach(self.page.screenshot(), name=f"{name} screenshot",)
            else:
                allure.attach(f"{name} is not visible", name=f"{name} visibility",
                              attachment_type=allure.attachment_type.TEXT)
                allure.attach(self.page.screenshot(), name=f"{name} screenshot", attachment_type=allure.attachment_type.PNG)

        if len(visible_banners) == len(banners):
            return True
            allure.attach(f"Visible banners: {visible_banners}", name="Visible banners", attachment_type=allure.attachment_type.PNG)
        else:
            visible_banners_str = ", ".join(visible_banners)
            allure.attach(f"Visible banners: {visible_banners_str}", name="Visible banners summary",
                          attachment_type=allure.attachment_type.TEXT)
            raise AssertionError(f"Not all banners are visible. Visible banners: {visible_banners_str}")
            allure.attach(self.page.screenshot(), name='Check banners position', attachment_type=allure.attachment_type.PNG)
    def teardown(self):
        try:
            super().teardown()
        except Exception as e:
            allure.attach(self.page.screenshot(), name='Tear down failed', attachment_type=allure.attachment_type.PNG)
            raise AssertionError from e


