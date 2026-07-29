from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators mapped directly from your script
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[data-qa="SignInButton"]')
    
    def __init__(self, driver):
        """Initializes the login page object."""
        super().__init__(driver)

    def login(self, username: str, password: str):
        """Fills out the credentials and submits the login form."""
        self.enter_text(self.EMAIL_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click_element(self.SIGN_IN_BUTTON)

    def is_logged_in(self) -> bool:
        """Verifies if login was successful by checking the DOM contents."""
        try:
            # Replaces: assert "Wallet" in driver.page_source
            # Looking for the keyword across the page source or inside main view text
            return "Wallet" in self.driver.page_source
        except Exception:
            return False
