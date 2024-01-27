import time

from playwright.async_api import Error as PlaywrightError, TimeoutError as PlaywrightTimeoutError
from playwright.async_api import async_playwright, Browser, ProxySettings, Page, Playwright
from playwright_stealth import stealth_async
from yarl import URL
from ..base import BasePlaywrightBrowser

from .account import TwitterAccount
from .client import TwitterClient

TWITTER_FUNCAPTCHA_SITEKEY = "0152B4EB-D2DC-460A-89A1-629838B529C9"
TWITTER_FUNCAPTCHA_URL = "https://twitter.com/account/access"


def proxy_url_to_playwright_proxy(proxy: str) -> ProxySettings:
    proxy = URL(proxy)
    return ProxySettings(
        server=f"{proxy.scheme}://{proxy.host}:{proxy.port}",
        password=proxy.password,
        username=proxy.user,
    )


class TwitterUnlocker(BasePlaywrightBrowser):
    # def __init__(self, funcaptcha_solver, **kwargs):
    #     """
    #     :param funcaptcha_solver: Асинхронная функция, решающая фанкапчу. Для ее создания нужно использовать пр
    #     """
    #     self.funcaptcha_solver = funcaptcha_solver
    #     super().__init__(**kwargs)

    async def solve_captcha(self, page: Page, solved_captcha: str) -> bool:
        element = await page.query_selector("#arkose_iframe, input[type='submit'].Button.EdgeButton.EdgeButton--primary")

        if element and element.get_attribute("value") == "Continue to Twitter":
            await element.click()
            print(f'Account successfully unfrozen')

        if element and element.get_attribute('value') == 'Delete':
            await element.click()
            print(f'click delete')

        if element.get_attribute('value') == 'Start':
            await element.click()

            await page.goto('https://twitter.com/account/access')
            await page.wait_for_selector('#arkose_iframe')

        iframe_element = await page.query_selector('#arkose_iframe')
        if not iframe_element:
            if "twitter.com/home" in page.url:
                return True

        iframe = await iframe_element.content_frame()
        script = f'parent.postMessage(JSON.stringify({{eventId:"challenge-complete",payload:{{sessionToken:"{solved_captcha}"}}}}),"*")'
        await iframe.evaluate(script)
        await page.wait_for_load_state(state='networkidle', timeout=10000)


    # TODO должно быть асинхронным контекстным менеджером, который возвращает класс контекста с методом анлокера.
    async def unlock(
            self,
            twitter: TwitterClient,
            *,
            default_timeout: int = 10,
            funcaptcha_solver,
    ):
        # Устанавливаем статус аккаунта, если не установлен прежде
        if twitter.account.status == "UNKNOWN":
            await twitter.establish_status()

        # Если аккаунт не залочен, то ничего не делаем
        if twitter.account.status != "LOCKED":
            return

        # Если залочен, то пытаемся разморозить, решив одну капчи с помощью предоставленного солвера
        proxy = proxy_url_to_playwright_proxy(twitter.session.proxy) if twitter.session.proxy else None
        context = await self._browser.new_context(proxy=proxy)
        cookies = [
            {
                "name": "auth_token",
                "value": twitter.account.auth_token,
                "domain": "twitter.com",
                "path": "/",
            },
        ]
        await context.add_cookies(cookies)
        page = await context.new_page()
        page.set_default_timeout(default_timeout * 1000)
        await stealth_async(page)

        await page.goto(f"https://twitter.com/account/access")
        await page.wait_for_load_state(state='networkidle')

        if "access" not in page.url:
            return

        for _ in range(5):
            await self.solve_captcha(page, solved_funcaptcha)

        # arkose_iframe = await page.query_selector("#arkose_iframe")

        button = await page.wait_for_selector('//*[@id="root"]/div/div[1]/button')
        await button.click()

        ...

        await context.close()

        # Устанавливаем новый статус аккаунта (должен быть GOOD)
        await twitter.establish_status()
