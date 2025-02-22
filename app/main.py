from app.scrapping.scrapper import solve_captcha
from app.constants import (
    URL,
    TRACK_CODE,
    CODE_INPUT_FIELD,
    CAPTCHA_INPUT_FIELD,
    SUBMIT_BUTTON,
)
from playwright.async_api import async_playwright
from app.logger_config import logger


async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL)

        logger.info('Entering the tracking code.')
        await page.fill(CODE_INPUT_FIELD, TRACK_CODE)

        logger.info('Starting CAPTCHA solving process...')
        captcha_text = await solve_captcha(page)

        if not captcha_text:
            logger.error(
                'Error solving CAPTCHA. Terminating scrapping process.'
            )
            return

        logger.info(f'Entering CAPTCHA text: {captcha_text}')
        await page.fill(CAPTCHA_INPUT_FIELD, captcha_text)

        logger.info("Clicking the 'Search' button.")
        await page.click(SUBMIT_BUTTON)

        logger.info('Process successfully completed.')
        await page.wait_for_timeout(5000)
        await browser.close()


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
