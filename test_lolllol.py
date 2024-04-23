from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://tombriches.com/")
    page.get_by_role("button", name="Log in").click()
    page.locator(".modal-wrapper > div > .relative").first.click()
    page.get_by_placeholder("E-mail").fill("samoilenkofluttershy@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("193786Az.")
    page.get_by_placeholder("Password").press("Enter")
    page.locator("div").filter(has_text=re.compile(r"^Log inForgot your password\?$")).get_by_role("button").click()
    page.locator("path").first.click()
    page.locator(".gap-0 > .relative").click()
    page.get_by_placeholder("Enter game name").fill("fire lightning")
    page.locator(".gameCardImage > .relative").first.click()
    page.locator(".controls").first.click()
    page.locator(".controls > button").first.click()
    page.locator("path").first.click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)