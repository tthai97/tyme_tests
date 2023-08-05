import logging

from selenium.webdriver.common.by import By

from common.selenium import Selenium


logger = logging.getLogger(__name__)


class CategoryPage():

    HEADING_TEXT = (By.CSS_SELECTOR, '#maincontainer span.maintext')
    SORT_ITEM_DROPDOWN = (By.ID, 'sort')

    PRODUCT_PRICE_IN_VIEW_LIST = (By.XPATH, '//div[contains(@class, "thumbnails list")]//div[@class="oneprice"]')
    PRODUCT_PRICE_IN_VIEW_GRID = (By.XPATH, '//div[contains(@class, "thumbnails grid")]//div[@class="oneprice"]')

    PRODUCT_CART_BTN_BY_NAME_IN_VIEW_LIST = (By.XPATH, '//div[contains(@class, "thumbnails list")]/div[.//a[@class="prdocutname" and contains(text(), "{}")]]//a[@class="productcart"]')
    PRODUCT_CART_BTN_BY_NAME_IN_VIEW_GRID = (By.XPATH, '//div[contains(@class, "thumbnails grid")]/div[.//a[@class="prdocutname" and text()="{}"]]//a[@class="productcart"]')

    PRODUCT_NAME = (By.XPATH, '//a[@class="prdocutname" and text()="{}"]')

    def __init__(self, web_object):
        self.web_object = web_object
        self.driver = self.web_object.driver

    def sort_item(self, sort_value):
        logger.info(f"Param: [sort_value: {sort_value}]")
        element = Selenium(self.driver).wait_for_element_presenced(*self.SORT_ITEM_DROPDOWN)
        Selenium(self.driver).select_element_by_visible_text(element, sort_value)
        
        logger.info(f"Sorted item by {sort_value}")
    
    def is_heading_text(self, text):
        logger.info(f"Param: [text: {text}]")
        element = Selenium(self.driver).wait_for_element_presenced(*self.HEADING_TEXT)
        heading_text = element.text

        if element.text == text:
            logger.info(f"Heading text {text} is matched")
            return True
        
        logger.info(f"Heading text {heading_text} is not matched with text {text}")
        return False

    def get_all_product_price(self, view_type):
        logger.info(f"Param: [view_type: {view_type}]")
        if view_type == "list":
            locator = self.PRODUCT_PRICE_IN_VIEW_LIST
        else:
            locator = self.PRODUCT_PRICE_IN_VIEW_GRID

        if Selenium(self.driver).is_element_presenced(*locator):
            elements = self.driver.find_elements(*locator)

        logger.info(f"Total elements are: {len(elements)}")
        prices = []
        for element in elements:
            element_price = element.text
            element_price = element_price.replace("$", "")

            price = float(element_price.strip())
            prices.append(price)
        
        logger.info(f"All product's prices are: {prices}")
        return prices
    
    def is_items_sorted_by_price(self, sort_type):
        """
            sort_type: string. The value must be low_to_high or high_to_low
        """
        logger.info(f"Param: [sort_type: {sort_type}]")
        prices = self.get_all_product_price("gird")
        
        if sort_type == "low_to_high":
            prices_sorted = prices[:]
            prices_sorted.sort()
            if prices != prices_sorted:
                logger.info(f"Prices {prices} are not sorted by low to high ({prices_sorted})")
                return False
        elif sort_type == "high_to_low":
            prices_sorted = prices[:]
            prices_sorted.sort(reverse=True)
            if prices != prices_sorted:
                logger.info(f"Prices {prices} are not sorted by high to low ({prices_sorted})")
                return False
        else:
            raise Exception("Unknow sort_type. The value must be low_to_high or high_to_low")

        logger.info(f"Prices {prices} are sorted")
        return True
    
    def click_product_by_name(self, product_name):
        logger.info(f"Param: [product_name: {product_name}]")
        locator = (
            self.PRODUCT_NAME[0],
            self.PRODUCT_NAME[1].format(product_name)
        )

        Selenium(self.driver).wait_for_element_presenced(*locator)
        Selenium(self.driver).click_element(*locator)

        logger.info(f"Clicked product {product_name}")


    def click_add_to_cart_by_product_name(self, product_name):
        logger.info(f"Param: [product_name: {product_name}]")
        locator = (
            self.PRODUCT_CART_BTN_BY_NAME_IN_VIEW_GRID[0],
            self.PRODUCT_CART_BTN_BY_NAME_IN_VIEW_GRID[1].format(product_name)
        )

        Selenium(self.driver).wait_for_element_presenced(*locator)
        Selenium(self.driver).click_element(*locator)

        logger.info(f"Clicked add to Cart of product {product_name}")

    