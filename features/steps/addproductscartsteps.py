from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from features.framework import AutomationConstants
import json
import time
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import allure
import os

scenario_counter = 0


# Web elementlerini daha kolay maintanance etmek için bir json dosyasında tutuyoruz ve buradan o json dosyasını okuyoruz
def get_element_xpath(element_key):
    with open("features/elements/elements.json", "r") as file:
        elements = json.load(file)
        return elements.get(element_key, "")


# Ekran görüntüsü için dosya oluşturma
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# Ekran görüntüsünü alıyoruz
def take_screenshot(context, step_name):
    scenario_directory = f"allure-results/screenshots/{scenario_counter}"
    create_directory(scenario_directory)

    screenshot_path = f"{scenario_directory}/{step_name}_{time.strftime('%Y%m%d%H%M%S')}.png"
    context.driver.save_screenshot(screenshot_path)

    allure.attach.file(screenshot_path, name=step_name, attachment_type=AttachmentType.PNG)


# Tarayıcıyı başlatma adımı ve URL'e gitme
@given("Navigate to url '{url}'")
def navigate_to_url(context, url):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    chrome_options = Options()
    chrome_options.add_argument("disable-translate")
    global scenario_counter
    scenario_counter += 1
    try:
        context.driver.get(url)
        print(f"Navigating to URL: {url}")
    except Exception as e:
        print(f"Error while navigating to URL: {url}\nError Details: {str(e)}")


# Ana sayfanın görüntülenip görüntülenmediğini kontrol etme adımı

@then("Verify that home page is visible successfully")
def verify_home_page(context):
    try:
        element_xpath = get_element_xpath("homepage_logo")
        element = context.driver.find_element(By.XPATH, element_xpath)
        element.is_displayed()
        take_screenshot(context, "home page")
    except Exception as e:
        print(f"Verify that home page: {str(e)}")
        raise Exception("failed home page:")


# 'Products' butonuna tıklama adımı
@when("Click 'Products' button")
def click(context):
    try:
        element_xpath = get_element_xpath("products_button")
        element = context.driver.find_element(By.XPATH, element_xpath)
        element.click()
        time.sleep(3)
        print("products :", element)
        take_screenshot(context, "products_button")

    except Exception as e:
        print(f"Error while clicking the element:\nError Details: {str(e)}")
        raise Exception("failed clicking the element: Error")


# İkinci ürün üzerine gelip 'Add to cart' butonuna tıklama adımı
# Eger oncesinde popUp cıkarsa url kontrolu ile popUp oncesi linke yönlendirme yapıyoruz

@then("Hover over first product and click 'Add to cart'")
def hover_first_product(context):
    expected_url = AutomationConstants.productURL
    actual_url = context.driver.current_url
    if actual_url != expected_url:
        context.driver.get(expected_url)
    try:
        first_product_xpath = get_element_xpath("first_product")
        first_product = context.driver.find_element(By.XPATH, first_product_xpath)

        add_to_cart_xpath = get_element_xpath("first_product_add_to_cart")
        add_to_cart_button = context.driver.find_element(By.XPATH, add_to_cart_xpath)
        time.sleep(3)

        ActionChains(context.driver).move_to_element(first_product).click(add_to_cart_button).perform()
        time.sleep(5)
        print("first_product:", first_product)
        print("add_to_cart_button:", add_to_cart_button)
        take_screenshot(context, "Hover over first product and click 'Add to cart'")
    except Exception as e:
        print(f"Error while hovering over the first product:\nError Details: {str(e)}")
        raise Exception("failed hovering over the first product")


# 'Continue Shopping' butonuna tıklama adımı

@then("Click 'Continue Shopping' button")
def click_continue_shopping(context):
    try:
        element_xpath = get_element_xpath("continue_shopping_button")
        element = context.driver.find_element(By.XPATH, element_xpath)
        element.click()
        print("continue element:", element)
        take_screenshot(context, "Click 'Continue Shopping")
    except Exception as e:
        print(f"Error while clicking the 'Continue Shopping' button:\nError Details: {str(e)}")
        raise Exception("failed clicking the 'Continue Shopping' button")


# İkinci ürün üzerine gelip 'Add to cart' butonuna tıklama adımı

@when("Hover over second product and click 'Add to cart'")
def hover_second_product(context):
    try:
        second_product_xpath = get_element_xpath("second_product")
        second_product = context.driver.find_element(By.XPATH, second_product_xpath)

        add_to_cart_xpath = get_element_xpath("second_product_add_to_cart")
        add_to_cart_button2 = context.driver.find_element(By.XPATH, add_to_cart_xpath)
        time.sleep(3)

        ActionChains(context.driver).move_to_element(second_product).click(add_to_cart_button2).perform()
        time.sleep(5)
        print("second product:", second_product)
        print("add_to_cart_button2:", add_to_cart_button2)
        take_screenshot(context, "Hover over second product and click 'Add to cart'")
    except Exception as e:
        print(f"Error while hovering over the first product:\nError Details: {str(e)}")
        raise Exception("failed hovering over the first product")


# 'View Cart' butonuna tıklama adımı

@then("Click 'View Cart' button")
def click_view_cart(context):
    try:
        time.sleep(2)
        element_xpath = get_element_xpath("view_cart_button")
        element = context.driver.find_element(By.XPATH, element_xpath)
        element.click()
        print("product1_element:", element)
        take_screenshot(context, "Click 'View Cart' button")
    except Exception as e:
        print(f"Error while clicking the 'View Cart' button:\nError Details: {str(e)}")
        raise Exception("failed view cart button")


# Her iki ürünün de sepete eklenip eklenmediğini kontrol etme adımı

@then("Verify both products are added to Cart")
def verify_both_products_added_to_cart(context):
    try:
        product1_element_xpath = get_element_xpath("product_1_element")
        product1_element = context.driver.find_element(By.XPATH, product1_element_xpath)
        product1 = product1_element.is_displayed()
        print("product1_element:", product1_element)

        product2_element_xpath = get_element_xpath("product_2_element")
        product2_element = context.driver.find_element(By.XPATH, product2_element_xpath)
        product2 = product2_element.is_displayed()
        print("product1_element:", product2_element)
        take_screenshot(context, "Verify both products are added to Cart")
        assert (product1 == True) and (product2 == True)
    except Exception as e:
        print(f"Error while verifying both products added to the Cart:\nError Details: {str(e)}")
        raise Exception("failed to verify both products added to the")


@then("I verify their prices, quantity, and total price")
def verifyPricesQuantityTotalPrice(context):
    try:
        prices1_element_xpath = get_element_xpath("verify_product1_prices")
        prices1_element = context.driver.find_element(By.XPATH, prices1_element_xpath)
        prices1 = prices1_element.get_attribute("innerText")
        print("prices1_element=", prices1)

        quantity1_element_xpath = get_element_xpath("verify_product1_quantity")
        quantity1_element = context.driver.find_element(By.XPATH, quantity1_element_xpath)
        quantity1 = quantity1_element.get_attribute("innerText")
        print("quantity1_element:", quantity1)

        totalPrice1_element_xpath = get_element_xpath("verify_product1_total")
        totalPrice1_element = context.driver.find_element(By.XPATH, totalPrice1_element_xpath)
        totalPrice1 = totalPrice1_element.get_attribute("innerText")
        print("totalPrice1_element:", totalPrice1)

        prices2_element_xpath = get_element_xpath("verify_product2_prices")
        prices2_element = context.driver.find_element(By.XPATH, prices2_element_xpath)
        prices2 = prices2_element.get_attribute("innerText")
        print("prices2_element:", prices2)

        quantity2_element_xpath = get_element_xpath("verify_product2_quantity")
        quantity2_element = context.driver.find_element(By.XPATH, quantity2_element_xpath)
        quantity2 = quantity2_element.get_attribute("innerText")
        print("prices2_element:", quantity2)

        totalPrice2_element_xpath = get_element_xpath("verify_product2_total")
        totalPrice2_element = context.driver.find_element(By.XPATH, totalPrice2_element_xpath)
        totalPrice2 = totalPrice2_element.get_attribute("innerText")
        print("totalPrice2_element:", totalPrice2)

        expPrice = AutomationConstants.fieledPrice1
        expQuantity = AutomationConstants.fieldQuantity1
        expTotalPrice = AutomationConstants.fieldTotal1
        expPrice2 = AutomationConstants.fieledPrice2
        expQuantity2 = AutomationConstants.fieldQuantity2
        expTotalPrice2 = AutomationConstants.fieldTotal2
        print("****************************")
        print("expTotalprice2:", expTotalPrice2)

        if prices1 == expPrice and quantity1 == expQuantity and totalPrice1 == expTotalPrice and prices2 == expPrice2 and quantity2 == expQuantity2 and totalPrice2 == expTotalPrice2:
            take_screenshot(context, step_name="verify both products pass")
            print("esit")
            return True
        else:
            take_screenshot(context, step_name="verify both products failed")
            print("esit degil")
            assert False, "failed verifying both products assert"

    except Exception as e:
        print(f"Error while verifying both products added to the Cart:\nError Details: {str(e)}")
        take_screenshot(context, step_name="verify both exception failed")
        raise Exception("failed to verify both products added to the")
