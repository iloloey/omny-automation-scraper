from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        """Initializes the page object with a driver and explicit wait configuration."""
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url: str):
        """Navigates to a specific URL."""
        self.driver.get(url)

    def zoom_page(self, zoom_percentage: str):
        """Sets the browser zoom level via JavaScript execution (e.g., '80%')."""
        self.driver.execute_script(f"document.body.style.zoom='{zoom_percentage}'")

    def wait_for_clickable(self, locator: tuple):
        """Waits for an element to be clickable and returns it."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_visibility(self, locator: tuple):
        """Waits for an element to be visible and returns it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator: tuple):
        """Waits for an element to be clickable and performs a click."""
        self.wait_for_clickable(locator).click()

    def enter_text(self, locator: tuple, text: str):
        """Waits for an input field to be clickable, clears it, and types text."""
        field = self.wait_for_clickable(locator)
        field.clear()
        field.send_keys(text)

    def get_element_text(self, locator: tuple) -> str:
        """Waits for an element to be visible and returns its text content."""
        return self.wait_for_visibility(locator).text
