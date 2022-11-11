from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from .BasicPage import Page
import time
class ManagerPage(Page):
    ADD_CUSTOMER = (By.XPATH, '//button[@ng-click="addCust()"]')
    MANAGER_LOGIN_BUTTON = (By.XPATH, "//button[@ng-click='manager()']")
    FIRST_NAME_FILED = (By.XPATH, '//input[@ng-model="fName"]')
    LAST_NAME_FILED = (By.XPATH, '//input[@ng-model="lName"]')
    POST_CODE_FILED = (By.XPATH, '//input[@ng-model="postCd"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    TABLE_ROWS = (By.XPATH, '//tbody/tr')

    
    def login(self) -> None:
        self.wd_wait.until(EC.element_to_be_clickable(ManagerPage.MANAGER_LOGIN_BUTTON)).click()
        
    def add_customer(self, first_name: str, last_name: str, post_code: str) -> str:
        self.wd_wait.until(EC.element_to_be_clickable(ManagerPage.ADD_CUSTOMER)).click()
        submit_button = self.wd_wait.until(EC.element_to_be_clickable(ManagerPage.SUBMIT_BUTTON))
        fname_field = self.driver.find_element(*ManagerPage.FIRST_NAME_FILED)
        lname_field = self.driver.find_element(*ManagerPage.LAST_NAME_FILED)
        post_code_field = self.driver.find_element(*ManagerPage.POST_CODE_FILED)
        fname_field.send_keys(first_name)
        lname_field.send_keys(last_name)
        post_code_field.send_keys(post_code)
        submit_button.click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        Alert(self.driver).accept()
        return alert.text
    
    def open_account(self) -> str:
        pass
    
    def get_customers(self) -> list[list]:
        table_rows = self.wd_wait.until(EC.presence_of_all_elements_located(ManagerPage.TABLE_ROWS))
        data = self.get_table_data(table_rows)