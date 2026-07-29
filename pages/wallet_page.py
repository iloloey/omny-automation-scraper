from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class WalletPage(BasePage):
    # Locators mapped from your functional script
    OMNY_CARD_LINK = (By.CSS_SELECTOR, "a[title*='OMNY card •••2971']")
    BALANCE_LABEL = (By.CSS_SELECTOR, "span[class*='BalancePanel-module___balance']")
    DETAILS_LINK = (By.XPATH, "//span[text()='Details']")
    ACCOUNT_SETTINGS_LINK = (By.XPATH, "//span[text()='Account Settings']")
    SIGN_OUT_LINK = (By.XPATH, "//span[text()='Sign Out']")

    def __init__(self, driver):
        """Initializes the wallet dashboard page object."""
        super().__init__(driver)

    def select_card(self):
        """Clicks on the specific OMNY card link."""
        self.click_element(self.OMNY_CARD_LINK)

    def get_balance(self) -> str:
        """Retrieves and returns the textual value of the current card balance."""
        return self.get_element_text(self.BALANCE_LABEL)

    def go_to_details(self):
        """Expands and opens the deep account details panel."""
        self.click_element(self.DETAILS_LINK)

    def logout(self):
        """Navigates the settings dropdown to sign out of the system cleanly."""
        self.click_element(self.ACCOUNT_SETTINGS_LINK)
        self.click_element(self.SIGN_OUT_LINK)
