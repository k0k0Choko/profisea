from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from .BasicPage import Page

class AccountPage(Page):
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//button[@ng-click='customer()']")
    ACCOUNTS_LIST = (By.CSS_SELECTOR, "#userSelect")
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    WITHDRAWL_BUTTON = (By.XPATH, '//button[@ng-click="withdrawl()"]')
    DEPOSIT_BUTTON = (By.XPATH, '//button[@ng-click="deposit()"]')
    TRANSACTIONS_BUTTON = (By.XPATH, '//button[@ng-click="transactions()"]')
    WITHDRAWL_INPUT_FIELD = (By.XPATH, '//form[@ng-submit="withdrawl()"]//input')
    DEPOSIT_INPUT_FILED = (By.XPATH, '//form[@ng-submit="deposit()"]//input')
    MESSAGE = (By.XPATH, '//span[@ng-show="message"]')
    TABLE_ROWS = (By.XPATH, '//tbody/tr')
    LOGOUT_BUTTON = (By.XPATH, '//button[@ng-click="byebye()"]')
    HOME_BUTTON = (By.XPATH, '//button[@ng-click="home()"]')

    def login(self, account_name: str) -> None:
        button = self.wd_wait.until(EC.element_to_be_clickable(AccountPage.CUSTOMER_LOGIN_BUTTON))
        button.click()
        accounts_list = self.wd_wait.until(EC.presence_of_element_located(AccountPage.ACCOUNTS_LIST))
        accounts_list = Select(accounts_list)
        accounts_list.select_by_visible_text(account_name)
        self.driver.find_element(*AccountPage.SUBMIT_BUTTON).click()
        
    def make_withdrawl(self, amount: int) -> str:
        self.wd_wait.until(EC.presence_of_element_located(AccountPage.WITHDRAWL_BUTTON)).click()
        withdrawl_input_field = self.wd_wait.until(EC.presence_of_element_located(AccountPage.WITHDRAWL_INPUT_FIELD))
        withdrawl_input_field.send_keys(str(amount))
        self.driver.find_element(*AccountPage.SUBMIT_BUTTON).click()
        message = self.driver.find_element(*AccountPage.MESSAGE)
        return message.text
    
    def make_deposit(self, amount: int) -> str:
        self.driver.find_element(*AccountPage.DEPOSIT_BUTTON).click()
        deposit_input_field = self.wd_wait.until(EC.presence_of_element_located(AccountPage.DEPOSIT_INPUT_FILED))
        deposit_input_field.send_keys("100")
        self.driver.find_element(*AccountPage.SUBMIT_BUTTON).click()
        message = self.driver.find_element(*AccountPage.MESSAGE)
        return message.text
    
    def get_transactions(self) -> list[list]:
        self.driver.find_element(*AccountPage.TRANSACTIONS_BUTTON).click()
        table = self.wd_wait.until(EC.presence_of_all_elements_located(AccountPage.TABLE_ROWS))
        data = self.get_table_data(table)
        return data
    
    def logout(self) -> None:
        self.wd_wait.until(EC.element_to_be_clickable(AccountPage.LOGOUT_BUTTON)).click()
        self.wd_wait.until(EC.element_to_be_clickable(AccountPage.HOME_BUTTON)).click()