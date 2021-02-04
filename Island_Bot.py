from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from time import sleep
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

print("Starting!")

driver.get("https://chrome.google.com/webstore/detail/chromereloadplus/nbbpjdmdkcmpimmhloehkojhbhjlboog?hl=en")
driver.implicitly_wait(4)
addtochrome = driver.find_element_by_class_name("g-c-x")
addtochrome.click()
time.sleep(5)

driver.implicitly_wait(4)
driver.get("https://shopislandgrown.com/collections/live-breaks")

print("Started!") 
print("██╗░██████╗██╗░░░░░░█████╗░███╗░░██╗██████╗░  ██████╗░░█████╗░████████╗")
print("██║██╔════╝██║░░░░░██╔══██╗████╗░██║██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝")
print("██║╚█████╗░██║░░░░░███████║██╔██╗██║██║░░██║  ██████╦╝██║░░██║░░░██║░░░")
print("██║░╚═══██╗██║░░░░░██╔══██║██║╚████║██║░░██║  ██╔══██╗██║░░██║░░░██║░░░")
print("██║██████╔╝███████╗██║░░██║██║░╚███║██████╔╝  ██████╦╝╚█████╔╝░░░██║░░░")
print("╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░  ╚═════╝░░╚════╝░░░░╚═╝░░░")

driver.implicitly_wait(999999)
target = driver.find_element_by_link_text(config['INFO']['Desired_Pack'])

action = ActionChains(driver)
action.key_down(Keys.CONTROL)
action.key_down(Keys.ALT)
action.send_keys(Keys.F5)
action.key_up(Keys.CONTROL)
action.key_up(Keys.ALT)
action.perform()

target.click()

driver.implicitly_wait(3)

addtocart = driver.find_element_by_name("add")
addtocart.click()
print("Found Desired Packs!")
print("Added to Cart!")

driver.implicitly_wait(1)

dismisscart = driver.find_element_by_class_name("cart-popup__dismiss")
dismisscart.click()

driver.implicitly_wait(1)

viewcart = driver.find_element_by_id("CartCount")
viewcart.click()

driver.implicitly_wait(1)

twitch = driver.find_element_by_id("twitch-name")
twitch.send_keys(config['INFO']['TWITCH_NAME'])
twitch.send_keys(Keys.RETURN)

driver.implicitly_wait(1)

print("Inputting Information")
email = driver.find_element_by_id("checkout_email")
email.send_keys(config['INFO']['Email'])
fname = driver.find_element_by_id("checkout_shipping_address_first_name")
fname.send_keys(config['INFO']['First_Name'])
lname = driver.find_element_by_id("checkout_shipping_address_last_name")
lname.send_keys(config['INFO']['Last_Name'])
address = driver.find_element_by_id("checkout_shipping_address_address1")
address.send_keys(config['INFO']['Address'])
city = driver.find_element_by_id("checkout_shipping_address_city")
city.send_keys(config['INFO']['City'])
country = driver.find_element_by_id("checkout_shipping_address_country")
for option in country.find_elements_by_tag_name('option'):
    if option.text == 'United states':
        option.click()
state = driver.find_element_by_id("checkout_shipping_address_province")
for option in state.find_elements_by_tag_name('option'):
    if option.text == 'Michigan':
        option.click()
zipcode = driver.find_element_by_id("checkout_shipping_address_zip")
zipcode.send_keys(config['INFO']['Zip_Code'])

toshipping = driver.find_element_by_id("continue_button")
toshipping.click()
topayment = driver.find_element_by_id("continue_button")
topayment.click()
continuepayment = driver.find_element_by_id("continue_button")
continuepayment.click()

driver.implicitly_wait(2)

ppguest = driver.find_element_by_id("createAccount")
ppguest.click()

driver.implicitly_wait(1)

print("Inputting Card Info")
cardnumber = driver.find_element_by_id("cardNumber")
cardnumber.send_keys(config['INFO']['Card_Number'])
exp = driver.find_element_by_id("cardExpiry")
exp.send_keys(config['INFO']['Expiration_Date'])
cvv = driver.find_element_by_id("cardCvv")
cvv.send_keys(config['INFO']['Cvv'])
phone = driver.find_element_by_id("phone")
phone.send_keys(config['INFO']['Phone_Number'])
phone.send_keys(Keys.RETURN)
print("Done!")
print("MAKE SURE THE BOT HAS CHECKED OUT!")
print("Thank you and godspeed with your pulls :)")
print("██╗░██████╗██╗░░░░░░█████╗░███╗░░██╗██████╗░  ██████╗░░█████╗░████████╗")
print("██║██╔════╝██║░░░░░██╔══██╗████╗░██║██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝")
print("██║╚█████╗░██║░░░░░███████║██╔██╗██║██║░░██║  ██████╦╝██║░░██║░░░██║░░░")
print("██║░╚═══██╗██║░░░░░██╔══██║██║╚████║██║░░██║  ██╔══██╗██║░░██║░░░██║░░░")
print("██║██████╔╝███████╗██║░░██║██║░╚███║██████╔╝  ██████╦╝╚█████╔╝░░░██║░░░")
print("╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░  ╚═════╝░░╚════╝░░░░╚═╝░░░")
print("Made by DabKingOdis")
driver.close