# Task — BasePage and LoginPage (Page Object Model basics)
# This is a simplified Page Object Model — the core pattern used in UI automation (Playwright, Selenium). Since
# there's no real browser here, actions are simulated with print. The class structure is identical to real Page Objects.
# Part 1 — BasePage (parent class)
# Create a class BasePage that:
#
# takes url in __init__ and stores it
# has a method open() — prints "Opening {url}"
# has a method click(element) — prints "Clicking on {element}"
# has a method type_text(element, text) — prints "Typing '{text}' into {element}"
class BasePage:
    def __init__(self, url):
        self.url = url

    def open(self):
        print(f"Opening {self.url}")

    def click(self, element):
        print(f"Clicking on {element}")

    def type_text(self, element, text):
        print(f"Typing '{text}' into {element}")


page = BasePage("https://example.com")
page.open()
page.click("login button")
page.type_text("username field", "denis")

# Part 2 — LoginPage (inherits from BasePage)
# Create a class LoginPage that inherits from BasePage and adds one high-level method login(username, password).
# This method uses the inherited methods to perform a full login scenario:
#
# open the page (self.open())
# type the username (self.type_text(...))
# type the password (self.type_text(...))
# click the login button (self.click(...))
class LoginPage(BasePage):
    def login(self, username, password):
        self.open()
        self.type_text("username field", username)
        self.type_text("password field", password)
        self.click("login button")


login_page = LoginPage("https://example.com/login")
login_page.login("denis", "secret123")

# Key idea: LoginPage doesn't rewrite open, type_text, or click — it inherits them from BasePage and combines them into
# one meaningful business scenario login(). This is the essence of Page Object Model.
