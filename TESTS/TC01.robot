*** Settings ***
Documentation     Test Automation test Store
Resource    ../resources/resource.robot

Variables   ../config/config.py

Test Setup       Open Home Page
Test Teardown    Close browser

*** Keywords ***

*** Test Cases ***
[P] TC01 - Open Home Page of Automation test Store
    Log    2. Hover to Apparel & Accessories and can see Shoes and T-shirts categories
    Hover to Apparel and Accessories
    Validate "Shoes" exist in subcategories
    Validate "T-shirts" exist in subcategories
    Select "T-shirts" in subcategories
    
    Log    3. Can see the Tshirts page
    Title Contain "T-shirts"
    Category heading text is "T-SHIRTS"

    Log    4. Sort by Price Low > High
    Sort product by "Price Low > High"

    Log    5. Verify the product is sorted by Price Low > High
    Product's price are sorted by low to high

    Log    6. Add to Cart an item and check the detail
    Add product "Casual 3/4 Sleeve Baseball T-Shirt" to Cart
    Title Contain "Casual 3/4 Sleeve Baseball T-Shirt"
    Product name is "Casual 3/4 Sleeve Baseball T-Shirt"
    Product price is "$14.00"
    Product description contain "This classic raglan t-shirt is perfect for all occasions. Whether you are working out or hanging out, this shirt is a win for the versatility. Perfect to join your friends to watch and cheer for your favorite team in all sports: basketball, football, football, hockey or baseball."
    Product description contain "The raglan t-shirts are great options for men and women looking for a stylish look in their casual looks. For mild days bet on the 3/4 sleeve model in contrasting color."
    Product description contain "Made in 100% cotton fabric, features slim fit and round neckline."

[P] TC02 - Sort Product By Price High > Low
    Log    2. Hover to Apparel & Accessories and can see Shoes and T-shirts categories
    Hover to Apparel and Accessories
    Validate "Shoes" exist in subcategories
    Validate "T-shirts" exist in subcategories
    Select "T-shirts" in subcategories
    
    Log    3. Can see the Tshirts page
    Title Contain "T-shirts"
    Category heading text is "T-SHIRTS"

    Log    4. Sort by Price High > Low
    Sort product by "Price High > Low"

    Log    5. Verify the product is sorted by Price High > Low
    Product's price are sorted by high to low

[F] TC03 - Not found item in categories
    Log    2. Hover to Apparel & Accessories and can see Shoes and FAIL categories
    Hover to Apparel and Accessories
    Validate "Shoes" exist in subcategories
    Run Keyword And Expect Error    ValueError: Not found FAIL in subcategories        Validate "FAIL" exist in subcategories

[F] TC04 - Sort Product By Price Failed
    Log    2. Hover to Apparel & Accessories and can see Shoes and T-shirts categories
    Hover to Apparel and Accessories
    Validate "Shoes" exist in subcategories
    Validate "T-shirts" exist in subcategories
    Select "T-shirts" in subcategories
    
    Log    3. Can see the Tshirts page
    Title Contain "T-shirts"
    Category heading text is "T-SHIRTS"

    Log    4. Sort by Price High > Low
    Sort product by "Price High > Low"

    Log    5. Verify the product is sorted by Price Low > High
    Run Keyword And Expect Error    ValueError: Product is not sorted by price as expected    Product's price are sorted by low to high

[F] TC05 - Product name is wrong
    Log    2. Hover to Apparel & Accessories and can see Shoes and T-shirts categories
    Hover to Apparel and Accessories
    Validate "Shoes" exist in subcategories
    Validate "T-shirts" exist in subcategories
    Select "T-shirts" in subcategories
    
    Log    3. Can see the Tshirts page
    Title Contain "T-shirts"
    Category heading text is "T-SHIRTS"

    Log    4. Sort by Price Low > High
    Sort product by "Price Low > High"

    Log    5. Verify the product is sorted by Price Low > High
    Product's price are sorted by low to high

    Log    6. Add to Cart an item and check the detail
    Add product "Casual 3/4 Sleeve Baseball T-Shirt" to Cart
    Title Contain "Casual 3/4 Sleeve Baseball T-Shirt"
    Run Keyword And Expect Error    ValueError: Product name is not matched    Product name is "Casual 3/4 Sleeve Baseball T-Shirt FAIL"

[F] TC06 - Product price is wrong
    Log    2. Hover to Apparel & Accessories and can see Shoes and T-shirts categories
    Hover to Apparel and Accessories
    Validate "Shoes" exist in subcategories
    Validate "T-shirts" exist in subcategories
    Select "T-shirts" in subcategories
    
    Log    3. Can see the Tshirts page
    Title Contain "T-shirts"
    Category heading text is "T-SHIRTS"

    Log    4. Sort by Price Low > High
    Sort product by "Price Low > High"

    Log    5. Verify the product is sorted by Price Low > High
    Product's price are sorted by low to high

    Log    6. Add to Cart an item and check the detail
    Add product "Casual 3/4 Sleeve Baseball T-Shirt" to Cart
    Title Contain "Casual 3/4 Sleeve Baseball T-Shirt"
    Product name is "Casual 3/4 Sleeve Baseball T-Shirt"
    Run Keyword And Expect Error    ValueError: Product price is not matched    Product price is "$14.10"

[F] TC07 - Product description is wrong
    Log    2. Hover to Apparel & Accessories and can see Shoes and T-shirts categories
    Hover to Apparel and Accessories
    Validate "Shoes" exist in subcategories
    Validate "T-shirts" exist in subcategories
    Select "T-shirts" in subcategories
    
    Log    3. Can see the Tshirts page
    Title Contain "T-shirts"
    Category heading text is "T-SHIRTS"

    Log    4. Sort by Price Low > High
    Sort product by "Price Low > High"

    Log    5. Verify the product is sorted by Price Low > High
    Product's price are sorted by low to high

    Log    6. Add to Cart an item and check the detail
    Add product "Casual 3/4 Sleeve Baseball T-Shirt" to Cart
    Title Contain "Casual 3/4 Sleeve Baseball T-Shirt"
    Product name is "Casual 3/4 Sleeve Baseball T-Shirt"
    Product price is "$14.00"
    Product description contain "This classic raglan t-shirt is perfect for all occasions. Whether you are working out or hanging out, this shirt is a win for the versatility. Perfect to join your friends to watch and cheer for your favorite team in all sports: basketball, football, football, hockey or baseball."
    Run Keyword And Expect Error    ValueError: Product description is not matched    Product description contain "FAIL The raglan t-shirts are great options for men and women looking for a stylish look in their casual looks. For mild days bet on the 3/4 sleeve model in contrasting color."
