import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

logger = logging.getLogger(__name__)

class Selenium():
    def __init__(self, driver) -> None:
        self.driver = driver
        pass
    
    def is_title_contain(self, title, timeout=5):
        try: 
            WebDriverWait(self.driver, timeout).until(EC.title_contains(title))
            return True
        except TimeoutException as e:
            return False

    def click_element(self, method, locator):
        self.get_element(method, locator).click()
    
    def hover_to_element(self, method, locator):
        element = self.get_element(method, locator)
        ActionChains(self.driver).move_to_element(element).perform()
    
    def hover_to_element_with_offset(self, method, locator, xoffset, yoffset):
        element = self.get_element(method, locator)
        ActionChains(self.driver).move_to_element_with_offset(element, xoffset, yoffset).perform()

    def wait_for_element_presenced(self, method, locator, timeout=5):
        try: 
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((method, locator)))
        except TimeoutException as e:
            raise Exception(f"{(method, locator)} is not exist after {timeout}. Exception: {str(e)}")

    def is_element_presenced(self, method, locator):
        try: 
            WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((method, locator)))
            return True
        except TimeoutException as e:
            logger.info(f"{(method, locator)} is not presented")
            return False
    
    def get_element(self, method, locator):
        try: 
            return self.driver.find_element(method, locator)
        except NoSuchElementException as e:
            raise Exception(f"Failed to get element {(method, locator)}. Exception: {str(e)}")

    def select_element_by_visible_text(self, element, value):
        Select(element).select_by_visible_text(value)