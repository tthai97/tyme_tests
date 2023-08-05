*** Settings ***
Library    WebTest/WebTest.py

*** Variables ***
${BROWSER}        Firefox
${TEST_PAGE_URL}  https://automationteststore.com/

*** Keywords ***
Close browser
    terminate_driver

Title Contain "${text}"
    browser_title_contain    ${text}

Open Home Page
    launch_browser    ${TEST_PAGE_URL}    ${BROWSER}
    browser_title_contain    A place to practice your automation skills!

Hover to Apparel and Accessories
    move_to_apparel_and_accessories

Validate "${category}" exist in subcategories
    validate_item_exist_in_subcategories    ${category}

Select "${category}" in subcategories
    select_subcategorie    ${category}

Sort product by "${option}"
    sort_product    ${option}

Product's price are sorted by low to high
    validate_items_sorted_by_price    low_to_high

Product's price are sorted by high to low
    validate_items_sorted_by_price    high_to_low

Select Product "${name}"
    select_product_by_name    ${name}

Add product "${product_name}" to Cart
    select_add_to_cart_of_product    ${product_name}

Product price is "${price}"
    validate_price_in_page_product    ${price}

Product name is "${name}"
    validate_product_name_in_page_product    ${name}

Product description contain "${text}"
    validate_product_description_in_page_product    ${text}

Category heading text is "${text}"
    validate_category_heading_text    ${text}