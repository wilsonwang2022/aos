import datetime
from faker import Faker
fake = Faker(locale='en_CA')
aos_url = 'https://advantageonlineshopping.com/#/'
aos_loginurl = 'https://advantageonlineshopping.com/#/myAccount'
aos_title = f'\xa0''Advantage Shopping'
aos_registerUrl = 'https://advantageonlineshopping.com/#/register'
#moodle_login_url = 'http://52.39.5.126/login/index.php'
#moodle_users_main_page = 'http://52.39.5.126/admin/user.php'
#moodle_username = 'xiaodongwang'
#moodle_password = 'Wxd2022wxd!'
#moodle_dashboard_url = 'http://52.39.5.126/my/'
new_username = f'{fake.user_name()}{fake.pyint(11,99)}'
new_password = fake.password()[:12]
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
# description = fake.sentence(nb_words=100)
description = f'User added by {new_username} via Python Selenium Automated script on {datetime.datetime.now()}'
pic_desc = fake.user_name()
phonetic_name = fake.user_name()
list_of_interests = [new_username, new_password, full_name, email, city]
web_page_url = fake.url()
icq_number = fake.pyint(111111, 999999)
institution = fake.lexify(text='????????????????????')
department = fake.lexify(text='???????')
phone = fake.phone_number()
mobile_phone = fake.phone_number()
#address = fake.address()
#address = fake.address().replace("\n", "")
address = fake.street_address()
postal_code = fake.postalcode()
province_code = fake.province_abbr()
country_code = fake.current_country_code()
street_city_region = f'{country_code}/{province_code}'