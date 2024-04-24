import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://tombriches.com/")
    page.get_by_text("providersTopNewJackpotsSlotsMegawaysCrashFruitsBonus gamesDrops & Wins").click()
    page.get_by_role("button", name="providers").click()
    page.get_by_role("button", name="Log in").click()
    page.get_by_placeholder("E-mail").click()
    page.get_by_placeholder("E-mail").fill("samoilenkofluttershy@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("193786Az.")
    page.locator("div").filter(has_text=re.compile(r"^Log inForgot your password\?$")).get_by_role("button").click()
    page.locator(".cursor-pointer").first.click()
    page.get_by_role("button", name="providers").click()
    page.get_by_text("Spribe").click()
    page.locator("div").filter(has_text=re.compile(r"^Spribe$")).click()
    page.get_by_role("button", name="providers").click()
    page.get_by_text("Play'n'Go").click()
    page.locator("div").filter(has_text=re.compile(r"^Play'n'Go$")).click()
    page.get_by_role("button", name="providers").click()
    page.get_by_text("Pragmatic Play Live").click()
    page.locator("div").filter(has_text=re.compile(r"^Pragmatic Play Live$")).click()
    page.get_by_role("button", name="providers").click()
    page.get_by_text("Betsoft", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Betsoft$")).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)




