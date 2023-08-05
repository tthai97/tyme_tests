import logging

from selenium.webdriver.common.by import By

from common.selenium import Selenium


logger = logging.getLogger(__name__)


class ProductPage():

    PRODUCT_NAME = (By.CSS_SELECTOR, 'h1[class="productname"] > span')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div[class="productfilneprice"]')
    PRODUCT_DESCRIPTION = (By.ID, 'description')

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'a[class="cart"]')

    def __init__(self, web_object):
        self.web_object = web_object
        self.driver = self.web_object.driver

    def is_product_has_price(self, price: str):
        logger.info(f"Param: [price: {price}]")
        element = Selenium(self.driver).wait_for_element_presenced(*self.PRODUCT_PRICE)
        product_price = element.text.strip()

        if product_price != price:
            logger.info(f"Product price {product_price} is not matched with {price}")
            return False
        
        logger.info(f"Product price {product_price} is matched")
        return True

    def is_product_has_name(self, name: str):
        logger.info(f"Param: [name: {name}]")
        element = Selenium(self.driver).wait_for_element_presenced(*self.PRODUCT_NAME)
        product_name = element.text.strip()

        if product_name != name:
            logger.info(f"Product name {product_name} is not matched with {name}")
            return False
        
        logger.info(f"Product name {product_name} is matched")
        return True
    
    def is_product_description_contain(self, text: str):
        logger.info(f"Param: [text: {text}]")
        element = Selenium(self.driver).wait_for_element_presenced(*self.PRODUCT_DESCRIPTION)
        product_description = element.text.strip()

        logger.info(f"Product description is: {product_description}")
        if text in product_description:
            logger.info(f"Found '{text}' in the description {product_description}")
            return True
        
        logger.info(f"Not found '{text}' in the description {product_description}")
        return False
    
    def click_add_to_cart(self):
        logger.info(f"Param: []")
        Selenium(self.driver).wait_for_element_presenced(*self.ADD_TO_CART_BTN)
        Selenium(self.driver).click_element(*self.ADD_TO_CART_BTN)

        logger.info("Clicked add to Cart")
