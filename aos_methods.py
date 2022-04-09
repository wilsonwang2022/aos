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

#Validate Homepage Text, Links and Top Navigation Menu
def validate_homepage_text():
    if driver.current_url == locators.aos_url:
        sleep(2)
        driver.find_element(By.ID, "speakersTxt").click()
        if driver.current_url == locators.aos_speakers:
            print(f'=================================================================')
            print(f'Validate SPEAKERS is displayed')
            sleep(2)
            driver.find_element(By.XPATH, '//a[contains(., "HOME")]').click()
            sleep(1)
            driver.find_element(By.ID, "tabletsTxt").click()
            if driver.current_url == locators.aos_tablets:
                print(f'------------------------------------------------------------------------')
                print(f'Validate TABLETS is displayed')
                sleep(2)
                driver.find_element(By.XPATH, '//a[contains(., "HOME")]').click()
                sleep(1)
                driver.find_element(By.ID, "laptopsTxt").click()
                if driver.current_url == locators.aos_laptops:
                    print(f'------------------------------------------------------------------------')
                    print(f'Validate LAPTOPS is displayed')
                    sleep(2)
                    driver.find_element(By.XPATH, '//a[contains(., "HOME")]').click()
                    sleep(1)
                    driver.find_element(By.ID, "headphonesTxt").click()
                    if driver.current_url == locators.aos_headphones:
                        print(f'------------------------------------------------------------------------')
                        print(f'Validate HEADPHONES is displayed')
                        sleep(2)
                        driver.find_element(By.XPATH, '//a[contains(., "HOME")]').click()
                        sleep(1)
                        driver.find_element(By.ID, "miceTxt").click()
                        if driver.current_url == locators.aos_mice:
                            print(f'------------------------------------------------------------------------')
                            print(f'Validate MICE is displayed')
                            sleep(2)
                            driver.find_element(By.XPATH, '//a[contains(., "HOME")]').click()
                            sleep(1)
    else:
        print('It is correct homepage, try again')

def validate_links():
    if driver.current_url == locators.aos_url:
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
        if driver.find_element(By.ID, 'special_offer_items').is_displayed():
           print(f'---------------------------------------------------------')
           print('SPECIAL OFFER Link is displayed')
           driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
           if driver.find_element(By.ID, 'popular_items').is_displayed():
               print(f'---------------------------------------------------------')
               print('POPULAR ITEMS Link is displayed')
               driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
               if driver.find_element(By.ID, 'supportCover').is_displayed():
                   print(f'---------------------------------------------------------')
                   print('CONTACT US Link is displayed')
    else:
        print('the links are not displayed, try again')

def validate_main_logo():
    if driver.current_url == locators.aos_url:
        sleep(2)
        driver.find_element(By.XPATH, '//a[@href="#/"]').click()
        if driver.find_element(By.LINK_TEXT, 'OUR PRODUCTS').is_displayed():
            print(f'==========================================================')
            print('Main logo is displayed')
    else:
        print('It is not correct main logo link, try again')

def validate_contact_us_form():
    if driver.current_url == locators.aos_url:
        sleep(3)
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        sleep(1)
        if driver.find_element(By.ID, 'supportCover').is_displayed():
            Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Speakers')
            sleep(1)
            Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text('Bose Soundlink Bluetooth Speaker III')
            sleep(1)
            driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
            sleep(1)
            driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.description1)
            sleep(1)
            driver.find_element(By.ID,'send_btnundefined').click()
            sleep(1)
            print(f'========================================================')
            print('It is already diaplayed Contact Us links')
            if driver.find_element(By.XPATH, '//*[contains(.,"Thank you for contacting Advantage support.")]').is_displayed():
               driver.find_element(By.XPATH, '//a[contains(., "CONTINUE SHOPPING ")]').click()
               print('Thank You and Continue to Shopping!')
    else:
        print('It is not correct to contact us form, try again')

def validate_facebook():
    if driver.current_url == locators.aos_url:
        sleep(3)
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        sleep(1)
        if driver.find_element(By.ID, 'supportCover').is_displayed():
           driver.find_element(By.NAME, 'follow_facebook').click()
           sleep(1)
           print('swtich to facebook homepage')
#          print(driver.title)
           p = driver.window_handles[0]
           c = driver.window_handles[1]
           driver.switch_to.window(c)
           if driver.current_url == 'https://www.facebook.com/MicroFocus/':
              sleep(2)
              print(f'===============================================')
              print('It is Facebook homepage')
              driver.close()
              sleep(1)
              driver.switch_to.window(p)
def validate_twitter():
    if driver.current_url == locators.aos_url:
        sleep(3)
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        sleep(1)
        if driver.find_element(By.ID, 'supportCover').is_displayed():
           driver.find_element(By.NAME, 'follow_twitter').click()
           sleep(1)
           p = driver.window_handles[0]
           c = driver.window_handles[1]
           driver.switch_to.window(c)
           if driver.current_url == 'https://twitter.com/MicroFocus':
              sleep(2)
              print(f'------------------------------------------------')
              print('It is twitter homepage')
              driver.close()
              sleep(1)
              driver.switch_to.window(p)
def validate_linkdin():
    if driver.current_url == locators.aos_url:
        sleep(3)
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        sleep(1)
        if driver.find_element(By.ID, 'supportCover').is_displayed():
           driver.find_element(By.NAME, 'follow_linkedin').click()
           sleep(1)
           p = driver.window_handles[0]
           c = driver.window_handles[1]
           driver.switch_to.window(c)
           if driver.title == 'LinkedIn':
              sleep(2)
              print(f'------------------------------------------------')
              print('It is LinkedIn homepage')
              driver.close()
              driver.switch_to.window(p)
              print('We already checked social media links, well done!')
    else:
        print('It is not correct to social media links, try again')

# setUp()
#
# validate_homepage_text()
# validate_links()
# validate_main_logo()
# validate_contact_us_form()
# validate_facebook()
# validate_twitter()
# validate_linkdin()
#
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

