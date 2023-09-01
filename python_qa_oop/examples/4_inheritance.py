class Page:
    NAME = None

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        print("Opened: " + self.NAME)


class Browser:
    pass


class LoginPage(Page):
    NAME = "LoginPage"
    LOGIN_PAGE = "#login"

    def login(self, username, password):
        print(f"Input {username} {password}")
        print("Click " + self.LOGIN_PAGE)


class MainPage(Page):
    NAME = "MainPage"
    PROFILE_LOCATOR = "#profile"

    def open_profile(self):
        print("Click " + self.PROFILE_LOCATOR)


browser = Browser()
main_page = MainPage(browser=browser)
login_page = LoginPage(browser=browser)

main_page.open()
main_page.open_profile()
login_page.open()
login_page.login("admin", "qwerty")
