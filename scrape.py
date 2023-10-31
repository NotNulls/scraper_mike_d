from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


options = Options()
options.add_argument('window-size=1600x1000')

driver = webdriver.Firefox(options=options)
driver.get('https://franchisedisclosure.gov.au/Register')

time.sleep(1)


countiune_cookie_button = driver.find_element(By.ID,'btnTOUContiue')
checkbox = driver.find_element(By.ID,'acceptTOU')
checkbox.click()
countiune_cookie_button.click()

search_bar = driver.find_element(By.ID, 'Search_SearchTerm')

search_word = input('Please insert search criteria to look for: ')

search_bar.send_keys(search_word)

search_button = driver.find_element(By.ID, 'btnSearch')
search_button.click()

disclosure_check_box = driver.find_element(By.ID,'Search_HasDisclosureDocument')

disclosure_check_question = input('Please select if you are looking for "Disclosure document available" (Y/N): ')
print (disclosure_check_box)


if disclosure_check_question.lower() == 'y':
    driver.execute_script("arguments[0].scrollIntoView(true);", disclosure_check_box)
    time.sleep(1)
    disclosure_check_box.click()
    time.sleep(3)
elif disclosure_check_question.lower() == 'n':
    pass
else:
    'Please type "Y" or "N"'
    print ('\n')
    disclosure_check_question

all_names = driver.find_element(By.TAG_NAME,'table')

time.sleep(1)
for row in driver.find_elements(By.TAG_NAME,'tr')[1:]:
    time.sleep(0.1)
    comp_name = row.find_element(By.TAG_NAME, 'td').text.split('\n')[0]
    if search_word == comp_name:
        print('check 2')
        link = row.find_element(By.TAG_NAME, 'td')
        driver.execute_script("arguments[0].scrollIntoView(true);", link)
        time.sleep(1)
        link.click()
        time.sleep(1)
        # header = driver.find_elements((By.TAG_NAME, 'dt'))
        # header = [element.text for element in header]
        
        
        # print (header)
        

# driver.close()    

        


