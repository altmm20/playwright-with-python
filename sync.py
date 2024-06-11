from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.w3schools.com/python/python_strings_methods.asp")
    page.screenshot(path="ss.png")
    browser.close()
