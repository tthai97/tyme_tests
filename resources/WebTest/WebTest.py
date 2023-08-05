import logging

from selenium import webdriver

from POM.HomePage import HomePage
from POM.CategoryPage import CategoryPage
from POM.ProductPage import ProductPage

from common.selenium import Selenium


logging.basicConfig(
    level=logging.INFO,
    format="%(atctime)s - %(levelname)s - %(name)s - %(funcName)s : %(message)s"
)


class WebTest(object):
    def __init__(self) -> None:
        self.driver = None

    def launch_browser(self, url, browser_type):
        logging.info(f"launch browser: {url}")
        if browser_type.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.headless = True
            options.add_argument("window-size=1400,600")
            
            self.driver = webdriver.Chrome(options=options)

        elif browser_type.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            options.headless = True
            options.add_argument("--width=1400")
            options.add_argument("--height=600")

            self.driver = webdriver.Firefox(options=options)

        else:
            raise ValueError(f"Unsupport {browser_type} browser")

        self.driver.get(url)
        self.driver.maximize_window()
    
    def terminate_driver(self):
        if self.driver:
            self.driver.close()
            self.driver.quit()
    
    def browser_title_contain(self, title):
        if not Selenium(self.driver).is_title_contain(title, 5):
            raise ValueError(f"Title '{self.driver.title}' does not contain '{title}'.")

    def move_to_apparel_and_accessories(self):
        HomePage(self).move_to_apparel_and_accessories()
    
    def validate_item_exist_in_subcategories(self, subcategorie_name):
        if not HomePage(self).is_item_exist_in_subcategories(subcategorie_name):
            raise ValueError(f"Not found {subcategorie_name} in subcategories")
        
    def select_subcategorie(self, subcategorie_name):
        HomePage(self).click_item_in_subcategories(subcategorie_name)

    def validate_category_heading_text(self, text):
        if not CategoryPage(self).is_heading_text(text):
            raise ValueError(f"Heading text of Page Category is not {text}")

    def sort_product(self, sort_value):
        CategoryPage(self).sort_item(sort_value)

    def validate_items_sorted_by_price(self, sort_type):
        """
            sort_type: string. The value must be low_to_high or high_to_low
        """
        if not CategoryPage(self).is_items_sorted_by_price(sort_type):
            raise ValueError("Product is not sorted by price as expected")

    def select_product_by_name(self, product_name):
        CategoryPage(self).click_product_by_name(product_name)

    def select_add_to_cart_of_product(self, product_name):
        CategoryPage(self).click_product_by_name(product_name)

    def validate_price_in_page_product(self, price: str):
        if not ProductPage(self).is_product_has_price(price):
            raise ValueError(f"Product price is not matched")

    def validate_product_name_in_page_product(self, name: str):
        if not ProductPage(self).is_product_has_name(name):
            raise ValueError(f"Product name is not matched")

    def validate_product_description_in_page_product(self, text: str):
        if not ProductPage(self).is_product_description_contain(text):
            raise ValueError(f"Product description is not matched")
    