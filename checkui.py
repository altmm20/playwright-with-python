import asyncio
from playwright.async_api import async_playwright, expect
async def selectors():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False,slow_mo=1000)
        page = await browser.new_page()
        #These are use of playwright selectors 
        await page.goto("https://ultimateqa.com/filling-out-forms/")
        await page.fill('input[name="et_pb_contact_name_0"]',"Mahin")
        await page.fill('textarea[name="et_pb_contact_message_0"]', "This is being written with Playwright")
        await page.click('button[name="et_builder_submit_button"]')
        await page.wait_for_timeout(5000)
        await expect(page.get_by_text("Thanks for contacting us")).to_be_visible()
      
async def locators():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False,slow_mo=1000)
        page = await browser.new_page()
        #These are use of playwright selectors 
        await page.goto("https://ultimateqa.com/filling-out-forms/")
        await page.locator('input[name="et_pb_contact_name_1"]').fill("Malhotra")
        await page.locator('textarea[name="et_pb_contact_message_1"]').fill("Lets do the math!")
        math_expression=eval(await page.locator('span.et_pb_contact_captcha_question').text_content())
        await page.locator('input[name="et_pb_contact_captcha_1"]').fill(str(math_expression))
        await page.locator('button:nth-child(2)[name="et_builder_submit_button"]').click()
        await page.wait_for_timeout(5000)
        await expect(page.get_by_text("Thanks for contacting us")).to_be_visible()

    
async def main():
    await asyncio.gather(selectors(), locators())

asyncio.run(main())