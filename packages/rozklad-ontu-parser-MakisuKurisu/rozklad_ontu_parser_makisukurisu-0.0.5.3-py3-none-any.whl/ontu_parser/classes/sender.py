"""Module for sending operations"""
import time
from datetime import datetime
from urllib.parse import urlencode
import requests
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

from .base import BaseClass
from .enums import RequestsEnum


class TTLValue(BaseClass):
    """Describes value with some time to live (like authorization token)"""

    _ttl: int = 3600  # Time To Live (in seconds)
    _value: object = None

    issued_at: datetime = datetime.min

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.issued_at = datetime.now()

    def is_valid(self):
        """
        Checks wether value is still valid
            True if TTLValue was issued less seconds before than Time To Live
        """
        seconds_passed = (datetime.now() - self.issued_at).seconds
        if seconds_passed < self._ttl:
            return True
        return False

    def set_value(self, value):
        """Sets value, and resets issued_at"""
        self.issued_at = datetime.now()
        self._value = value
        return self._value


class Cookies(TTLValue):
    """Describes cookies (Temporary values) for requests"""

    def __init__(self, sender, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sender: Sender = sender

    @property
    def value(self) -> dict[str, str]:
        """Returns value of a cookie (or gets one, if not present)"""
        if self._value and self.is_valid():
            return self._value

        print("Cookies are being updated")
        cookie = self.get_cookie()
        if not cookie:
            raise RuntimeError("Could not get cookies")
        return cookie

    def get_cookie(self):
        """Get's cookie value and notbot (used to verify that request is made by human)"""
        # link = self.sender.link
        notbot = self.sender.notbot.value

        return self.set_value(notbot)


class NotBot(TTLValue):
    """Describes NotBot value for requests"""

    def __init__(self, *args, **kwargs):
        self._browser_kwargs = {}
        super().__init__(*args, **kwargs)

    @classmethod
    def create(cls, **browser_settings):
        """
        Creates NotBot with certain browser_settings
        Refer to webdriver.Firefox arguments and docs for more info
        """
        if isinstance(browser_settings, dict) and "browser_settings" in browser_settings:
            # I'm not sure if this is the right way of multi-passing kwargs :|
            browser_settings = browser_settings.get("browser_settings", {})

        obj = cls()
        obj._browser_kwargs = browser_settings

        return obj

    @property
    def value(self) -> dict:
        """Returns or sets and returns value of {'notbot', 'pow-result'} cookies"""
        if self._value and self.is_valid():
            return self._value

        print("Notbot is being updated")
        notbot = self.get_notbot()
        if not notbot:
            raise RuntimeError("Could not get notbot")
        return notbot

    def __make_request(self, driver: webdriver.Firefox) -> tuple[str | None, str | None]:
        """Returns notbot and pow-result (also PHPSESSID) cookies value"""
        driver.get("https://rozklad.ontu.edu.ua/guest_n.php")
        notbot: str | None = None
        pow_result: str | None = None
        phpsesid: str | None = None
        cookies = driver.get_cookies()
        if cookies:
            for cookie in cookies:
                if cookie["name"] == "notbot":
                    notbot = cookie["value"]
                if cookie["name"] == "pow-result":
                    pow_result = cookie["value"]
                if cookie["name"] == "PHPSESSID":
                    phpsesid = cookie["value"]
        return (notbot, pow_result, phpsesid)

    def get_notbot(self):
        """Gets notbot by making webdriver request (emulates JS)"""
        options = self._browser_kwargs.pop("options", None)
        if not options:
            options = FirefoxOptions()
            options.add_argument("--headless")

        driver = webdriver.Firefox(
            options=options,
            # desired_capabilities=desired_capabilities,
            **self._browser_kwargs,
        )
        i = 0
        while True:
            print("Making request to get cookies")
            notbot, pow_result, phpsesid = self.__make_request(driver=driver)
            if all([notbot, pow_result, phpsesid]):
                break

            print(f"Sleeping for {i ** 2} seconds")
            time.sleep(i**2)
            i += 1

        driver.close()
        return self.set_value({"notbot": notbot, "pow-result": pow_result, "PHPSESSID": phpsesid})


class Sender(BaseClass):
    """Describes sender with link, notbot and cookies to send requests"""

    default_link: str = "https://rozklad.ontu.edu.ua/guest_n.php"
    teachers_link: str = "https://rozklad.ontu.edu.ua/departments_all.php"
    notbot: NotBot = None
    cookies: Cookies = None
    for_teachers: bool = False

    @property
    def link(self):
        """Returns link to send requests to"""
        if self.for_teachers:
            return self.teachers_link
        return self.default_link

    def __init__(self, *args, **kwargs):
        notbot_kwargs = kwargs.get("notbot", {})
        for_teachers = kwargs.get("for_teachers", False)
        self.for_teachers = for_teachers
        self.notbot = NotBot.create(**notbot_kwargs)
        self.cookies = Cookies(self)

    _responses: list[requests.Response] = []

    def send_request(self, method: str, data: (dict | None) = None, query: (dict | None) = None):
        """Sends request with method and some data, if needed"""
        session = requests.Session()
        if method not in RequestsEnum.Methods.CHOICES.value:
            raise ValueError(
                f"arg. `method` should be one of: {RequestsEnum.Methods.CHOICES.value}",
                method,
            )

        link = self.link
        if query:
            link += "?" + urlencode(query)

        try:
            # Just in case, I guess
            for item, key in self.cookies.value.items():
                session.cookies.set(item, key, path="/")
            response: requests.Response = session.request(
                method=method,
                url=link,
                data=data,
                headers={
                    # They are really getting on my nerves at this point TBH
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                },
            )
        except Exception as exception:
            raise ValueError(
                f"could not get response from {link}, got exception: {exception}",
                link,
                exception,
            ) from exception
        if response.status_code != RequestsEnum.code_ok():
            raise ValueError(
                "server returned non OK response",
                response.status_code,
                response,
                response.content,
            )
        # Keep responses for a little while
        self._responses.append(response)
        self._responses = self._responses[-5:]

        return response
