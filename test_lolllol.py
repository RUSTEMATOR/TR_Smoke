import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://tombriches.com/")
    page.get_by_role("button", name="Log in").click()
    page.get_by_placeholder("E-mail").click()
    page.get_by_placeholder("E-mail").fill("automaton_agircpvill11560@kingbilly.xyz")
    page.locator(".flex > div > .relative").first.click()
    page.get_by_placeholder("Password").fill("193786Az()")
    page.get_by_placeholder("Password").press("Enter")
    page.locator("div").filter(has_text=re.compile(r"^Log inForgot your password\?$")).get_by_role("button").click()
    page.locator("path").first.click()
    page.get_by_role("heading", name="Welcome Pack").click()
    page.get_by_role("heading", name="CASHBACK UP TO 15%").click()
    page.get_by_role("heading", name="UP TO 100 FS").click()
    page.locator(".swiper-pagination > span:nth-child(2)").first.click()
    page.locator(".swiper-pagination > span:nth-child(3)").first.click()
    page.locator("span:nth-child(4)").first.click()
    page.get_by_role("heading", name="TOMB TREASURE!").click()
    page.get_by_role("heading", name="LOYALTY PROGRAM", exact=True).click()
    page.get_by_role("button", name="get jackpot").click()
    page.locator(".swiper-pagination").first.click()
    page.locator("span:nth-child(5)").first.click()
    page.locator("span:nth-child(6)").first.click()
    page.locator("span:nth-child(7)").first.click()
    page.locator("div:nth-child(7) > div > div").first.click()
    page.locator("div").filter(has_text=re.compile(r"^PLAY NOW$")).nth(1).click()
    page.locator("div").filter(has_text=re.compile(r"^PLAY NOW$")).nth(3).click()
    page.locator(".swiper-button-next").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
