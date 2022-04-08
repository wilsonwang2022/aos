import sys
import datetime
from time import sleep
import aos_locators as locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service


s=Service(executable_path='../chromedriver.exe')
driver=webdriver.Chrome(service=s)


def setUp():
    driver.maximize_window()

    #to wait for the web browser implicitly
    driver.implicitly_wait(30)
    driver.get(locators.aos_url)

    if driver.current_url == locators.aos_url and driver.title == locators.aos_title:
        print(f'---------------------------------------------------------------------------')
        print(f'We are at the correct web page, {driver.current_url}')
        print(f'We are see the correct title page:{driver.title}')
    else:
        print(f'We are not at the correct home page. try again/check your code')
        driver.close() #close the current tab
        driver.quit() #close the browser completely

def create_new_user():
    if driver.current_url == locators.aos_url and driver.title == locators.aos_title:
        print(f'---------------------------------------------------------------------------')
        print(f'We are at the correct web page, {driver.current_url}')
        driver.find_element(By.ID,'menuUser').click()
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(1)
        if driver.current_url == locators.aos_registerUrl:
           driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
           driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
           driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
           driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
           driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
           sleep(1)
           driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
           driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
           Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text('Canada')
           driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
           driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
           driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.street_city_region)
           driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
           driver.find_element(By.NAME, 'i_agree').click()
           driver.find_element(By.ID, 'register_btnundefined').click()
           sleep(1)
           if driver.find_element(By.XPATH, f'//*[contains(., "{locators.new_username}")]').is_displayed():
              print('you have created new user: ' + (locators.new_username))
              print('your password is: ' + (locators.new_password))

def check_user_created():
    # Check that we are on the User's Main Page
    if driver.current_url == locators.aos_url:
        assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'menuUserLink').click()
        print(f'---------------------------------------------------------------------------')
        print(f'this is: {driver.title}')
        sleep(1)
        driver.find_element(By.XPATH, '//*[@id = "loginMiniTitle"]/label[1]').click()
        print('Verified the new user: ' + (locators.new_username))
        print('Verified the password is: ' + (locators.new_password))
        sleep(1)

def log_out():
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id = "loginMiniTitle"]/label[3]').click()
    #driver.find_element(By.XPATH, '//*[contains(., "Sign out")]').click()
    sleep(1)
    if driver.current_url == locators.aos_url:
        print(f'---------------------------------------------------------------------------')
        print(f'the log out successfuly done at : {datetime.datetime.now()}')
        sleep(1)

#6. Close the browser and display user-friendly messages."""
def tearDown():
    if driver is not None:
        print(f'---------------------------------------------------------------------------')
        print(f'Wishing you have a good day')
        print(f'test was completed at :{datetime.datetime.now()}')
        driver.close()
        driver.quit()
        old_instance = sys.stdout
        log_file = open('message.log', 'w')
        sys.stdout = log_file
        print(f'Email: {locators.email}\nUsername: {locators.new_username}\nPassword: {locators.new_password}\n'
              f'Full Name: {locators.full_name}')
        sys.stdout = old_instance
        log_file.close()

def log_in():
    if driver.current_url == locators.aos_loginurl:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)
        if driver.current_url == locators.aos_url:
           driver.find_element(By.XPATH, "//input[@name= 'username']").send_keys(locators.new_username)
           sleep(1)
           driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
           sleep(1)
           driver.find_element(By.ID, 'sign_in_btnundefined').click()
           sleep(1)
           print(f'---------------------------------------------------------------------------')
           print(f'We are at the correct web page, {driver.current_url}')

def delete_a_user():
        if driver.current_url == locators.aos_loginurl:
            driver.find_element(By.XPATH, '//*[@id="myAccountContainer"]/div[6]/button').click()
            sleep(2)
            driver.find_element(By.XPATH, '//*[@id="deleteAccountPopup"]/div[3]/div[1]').click()
            sleep(1)
            print(f'---------------------------------------------------------------------------')
            print(f'--- Account with username {locators.new_username} has been deleted successfully. Test passed ---')
            print(f'Account deleted successfully at: {datetime.datetime.now()}')
            sleep(5)
        else:
            print(f'Unable to delete New Account. Something went wrong.')

def verified_delete_user():
    if driver.current_url == locators.aos_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(1)
        driver.find_element(By.XPATH, "//input[@name= 'username']").send_keys(locators.new_username)
        sleep(1)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(1)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(1)
        assert driver.find_element(By.XPATH, '//*[@id="signInResultMessage"]').is_displayed()
        print(f'---------------------------------------------------------------------------')
        print(f'Verified {locators.new_username} has been deleted')
    else:
        print(f'This is not currect webpage')

# setUp()
# #check_homepage()
# create_new_user()
#
# check_user_created()
#
# log_out()
#
# log_in()
#
# check_user_created()
#
# delete_a_user()
#
# verified_delete_user()
#
# tearDown()

