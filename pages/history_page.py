from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HistoryPage(BasePage):
    # Locators mapped from your functional script
    VIEW_BALANCE_LINK = (By.XPATH, "//span[text()='View balance history']")
    TABLE_BODY = (By.CSS_SELECTOR, "div[class*='Table-module___tableBody']")
    BACK_TO_DETAILS_BUTTON = (By.CSS_SELECTOR, "a[data-qa='BackLink']")
    BACK_TO_WALLET_BUTTON = (By.XPATH, "//span[contains(@class, 'BackButton-module___text') and text()='Wallet']")

    def __init__(self, driver):
        """Initializes the balance history page object."""
        super().__init__(driver)

    def view_balance_history(self):
        """Clicks the link to navigate to the balance history view."""
        self.click_element(self.VIEW_BALANCE_LINK)

    def get_raw_history_text(self): # -> str:
        """Retrieves the full, unformatted string block from the table container."""
        return self.get_element_text(self.TABLE_BODY)

    def go_back_to_details(self):
        """Clicks the back link to return to the card details pane."""
        self.click_element(self.BACK_TO_DETAILS_BUTTON)

    def go_back_to_wallet(self):
        """Clicks the wallet back button to return to the primary dashboard."""
        self.click_element(self.BACK_TO_WALLET_BUTTON)
