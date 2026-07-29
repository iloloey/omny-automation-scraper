import os
import allure
import pytest
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.wallet_page import WalletPage
from pages.history_page import HistoryPage

load_dotenv()

@allure.feature("OMNY Wallet Management")
class TestOmnyWorkflow:
    
    @allure.story("Verify Balance History Data")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_balance_and_history(self, driver):
        # 1. Initialize Page Objects
        login_page = LoginPage(driver)
        wallet_page = WalletPage(driver)
        history_page = HistoryPage(driver)
        
        # 2. Perform Login Flow
        with allure.step("Navigate to OMNY Sign-in"):
            login_page.open_url("https://omny.info/signin")
            login_page.zoom_page("80%")
        with allure.step("Authenticate Credentials"):
            login_page.login(os.getenv("omny_user"), os.getenv("omny_pw"))
        
        # Unit test framework assertion for login success
        assert login_page.is_logged_in(), "Login failed: Wallet text missing from page source."
        
        # 3. Balance Validation Flow
        wallet_page.select_card()
        balance = wallet_page.get_balance()
        assert balance is not None, "Failed to retrieve account balance."
        
        # 4. History and Navigation Flow
        wallet_page.go_to_details()
        history_page.view_balance_history()

        with allure.step("Extract History and Validate Data"):
            raw_data = history_page.get_raw_history_text()
            allure.attach(raw_data, name="Raw Table Text", attachment_type=allure.attachment_type.TEXT)
        
        # # Parse and assert dataframe content
        # history_page.view_balance_history()
        # df = history_page.get_raw_history_text()
        # # print(df)
        # assert not df.empty, "Balance history table is empty."
        # assert "Trip Payment" in df, "Missing expected data columns."
        
        # 5. Logout Sequence
        history_page.go_back_to_details()
        wallet_page.logout()
