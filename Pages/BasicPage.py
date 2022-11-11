from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class Page:
    
    def __init__(self, driver):
        self.driver = driver
        self.wd_wait = WebDriverWait(driver, 5)
        
    @staticmethod    
    def get_table_data(table_rows: list[WebElement]) -> list[list]:
        table_data = []
        for row in table_rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            cells = [cell.text for cell in cells]
            table_data.append(cells)
        return table_data 