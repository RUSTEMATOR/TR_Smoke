import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://tombriches.com/")
    page.get_by_text("Live Games", exact=True)
    page.get_by_label("Blackjack").click()
    page.get_by_label("Bj League").click()
    page.get_by_label("Baccarat", exact=True).click()
    page.get_by_label("Poker", exact=True).click()
    page.get_by_label("Roulette", exact=True).click()
    page.get_by_label("Live Dealer Shows").click()
    page.locator("div:nth-child(3) > .flex > .ml-2\\.5").click()
    page.get_by_label("Max").click()
    page.get_by_label("Mid", exact=True).click()
    page.get_by_label("Mini", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
