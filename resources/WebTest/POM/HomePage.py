import logging

from selenium.webdriver.common.by import By

from common.selenium import Selenium


logger = logging.getLogger(__name__)


class HomePage():
    PAGE_TITLE = "A place to practice your automation skills!"
    PAGE_URL = "https://automationteststore.com/"

    APPAREL_AND_ACCESSSORIES = (By.XPATH, '//section[@id="categorymenu"]//a[contains(text(), "Apparel & accessories")]')
    SUBCATEGORIES_ITEM = (By.XPATH, '//div[@class="subcategories"]//a[contains(text(), "{}")]')
    SUBCATEGORIES_ITEM_IS_SELECTED = (By.XPATH, '//div[@class="subcategories"]//li[@class="current"]//a[contains(text(), "{}")]')

    def __init__(self, web_object):
        self.web_object = web_object
        self.driver = self.web_object.driver

    def move_to_apparel_and_accessories(self):
        logger.info(f"Param: []")
        Selenium(self.driver).hover_to_element_with_offset(*self.APPAREL_AND_ACCESSSORIES, 200, 200)
        Selenium(self.driver).hover_to_element(*self.APPAREL_AND_ACCESSSORIES)

        logger.info("Moved to Apparel & Accessories")
    
    def is_item_exist_in_subcategories(self, subcategorie_name):
        logger.info(f"Param: [subcategorie_name: {subcategorie_name}]")
        locator = (
            self.SUBCATEGORIES_ITEM[0],
            self.SUBCATEGORIES_ITEM[1].format(subcategorie_name)
        )

        if Selenium(self.driver).is_element_presenced(*locator):
            logger.info(f"Found {subcategorie_name} in subcategories")
            return True
        
        logger.info(f"Not found {subcategorie_name} in subcategories")
        return False

    def click_item_in_subcategories(self, subcategorie_name):
        logger.info(f"Param: [subcategorie_name: {subcategorie_name}]")
        locator = (
            self.SUBCATEGORIES_ITEM[0],
            self.SUBCATEGORIES_ITEM[1].format(subcategorie_name)
        )

        Selenium(self.driver).wait_for_element_presenced(*locator)
        Selenium(self.driver).click_element(*locator)
        logger.info(f"Clicked {subcategorie_name} in subcategories")

    def is_item_in_subcategories_is_selected(self, subcategorie_name):
        logger.info(f"Param: [subcategorie_name: {subcategorie_name}]")
        locator = (
            self.SUBCATEGORIES_ITEM_IS_SELECTED[0],
            self.SUBCATEGORIES_ITEM_IS_SELECTED[1].format(subcategorie_name)
        )

        if Selenium(self.driver).wait_for_element_presenced(*locator):
            logger.info(f"Subcategorie {subcategorie_name} is selected")
            return True
        
        logger.info(f"Subcategorie {subcategorie_name} is not selected")
        return False

        

