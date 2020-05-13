from selenium import webdriver
import time

name = "name"
email = "youremail@gmail.com"
tel = "1234567890"
address = "123 4th street"
apt_number = "leave blank if N/A"
zip = "12345"
city = "city"
state = "state"
country = "country"

credit_number = "1111 1111 1111 1111"
exp_month = "01"
exp_year = "2222"
cvv = "123"

chromedrive_location = "chromedriver.exe"
driver = webdriver.Chrome(chromedrive_location)
driver.get("https://www.supremenewyork.com/shop/accessories/nq5hkuef2/mt26hz7la")

add_to_cart_button = '//*[@id="add-remove-buttons"]/input'
driver.find_element_by_xpath(add_to_cart_button).click()

time.sleep(2)

checkout_button = '//*[@id="cart"]/a[2]'
driver.find_element_by_xpath(checkout_button).click()

name_xpath = '//*[@id="order_billing_name"]'
driver.find_element_by_xpath(name_xpath).send_keys(name)
email_xpath = '//*[@id="order_email"]'
driver.find_element_by_xpath(email_xpath).send_keys(email)
tel_xpath = '//*[@id="order_tel"]'
driver.find_element_by_xpath(tel_xpath).send_keys(tel)
addr_xpath = '//*[@id="bo"]'
driver.find_element_by_xpath(addr_xpath).send_keys(address)
apt_xpath = '//*[@id="oba3"]'
driver.find_element_by_xpath(apt_xpath).send_keys(apt_number)
zip_xpath = '//*[@id="order_billing_zip"]'
driver.find_element_by_xpath(zip_xpath).send_keys(zip)
city_xpath = '//*[@id="order_billing_city"]'
driver.find_element_by_xpath(city_xpath).send_keys(city)
country_xpath = '//*[@id="order_billing_state"]'
driver.find_element_by_xpath(country_xpath).click()
state_xpath = '//*[@id="order_billing_state"]/option[8]'
driver.find_element_by_xpath(state_xpath).click

# card_month_xpath

print("Web Driver Run")