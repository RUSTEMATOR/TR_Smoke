import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://tombriches.com/")
    page.get_by_role("button", name="Log in").click()
    page.get_by_placeholder("E-mail").click()
    page.get_by_placeholder("E-mail").fill("samoilenkofluttershy@gmail.com")
    page.locator(".flex > div > .relative").first.click()
    page.get_by_placeholder("Password").fill("193786Az.")
    page.locator("path").first.click()
    page.get_by_role("button", name="Account").click()


    page.locator("div").filter(has_text=re.compile(r"^Сountry$")).locator("div").nth(2).click()
    page.locator("div").filter(has_text=re.compile(r"^Female$")).get_by_role("radio").check()
    page.locator("div").filter(has_text=re.compile(r"^Male$")).get_by_role("radio").check()
    page.get_by_role("button", name="ok").click()
    page.get_by_role("button", name="Save").click()
    page.locator("div").filter(has_text=re.compile(r"^Female$")).get_by_role("radio").check()
    page.get_by_role("button", name="Save").click()
    page.locator("div").filter(has_text=re.compile(r"^Email verification$")).locator("div").click()
    page.locator("div").filter(has_text=re.compile(r"^Male$")).get_by_role("radio").check()
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Profile data updated").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



