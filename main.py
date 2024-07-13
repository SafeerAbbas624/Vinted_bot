"""
This whole code is written by Safeer Abbas
https://github.com/SafeerAbbas624

"""

# Import all important libraries and packages.


import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pyperclip

# Define the URL for the Vinted sign-in page.
VINTED_SIGN_IN_URL = "https://www.vinted.fr/"

# Define the email address that you want to use to sign in to Vinted.
EMAIL_ADDRESS = "put your email here."

# Define the password that you want to use to sign in to Vinted.
PASSWORD = "Put your password here."

# Create a Selenium browser instance.
driver = uc.Chrome()
driver.maximize_window()

# Open the Vinted sign-in page.
driver.get(VINTED_SIGN_IN_URL)

# Wait for the page to load.
time.sleep(10)

# Click on France country.
driver.find_element(By.XPATH, '/html/body/div[13]/div/div/div/div[3]/div[7]').click()
# wait for page to load.
time.sleep(10)

#  Accept cookies
driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
time.sleep(5)

# click on login
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/div/div/div[3]/div/a[1]/span').click()
time.sleep(2)

# Click on already have account signin button on signin popup
driver.find_element(By.XPATH, '/html/body/div[10]/div/div/div/div[2]/div/span[2]/span/span').click()
time.sleep(2)
# Click on email button
driver.find_element(By.XPATH, '/html/body/div[10]/div/div/div/div[2]/div/span[1]/span/span').click()
time.sleep(2)

# Enter your email address and password.
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(EMAIL_ADDRESS)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(PASSWORD)
time.sleep(3)

# Click the "Sign in" button.
driver.find_element(By.XPATH, '/html/body/div[10]/div/div/div/div[2]/form/div[3]/div/div/button/span').click()
# Wait for the page to load.
# Extra 4 mins to load and for verification code insert.
time.sleep(150)

# List all folder available in Product folder
entries = os.listdir('Products/')

# Click dropdown button to access profile
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/div/div/div[3]/div[2]/div[1]/div/div').click()
time.sleep(3)
# click on profile from dropdown button.
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/div/div/div[3]/div[2]/div[1]/div/div['
                              '2]/div/div/div/div/ul/li[2]/a').click()
# Wait for the page to load
time.sleep(10)

# checking for listings available or not
no_selling = driver.find_element(By.XPATH, '/html/body/main/div/section/div/div[2]/section/div/div/div/div/div['
                                           '3]/div[3]/div[3]/h1/span').text

# Starting while loop for not to shut down the browser and remain running till exits by user.
while True:
    # if seller have no profile listings it will upload listings
    if "Dressing du membre" in no_selling:
        # i is to check the length of list of folders
        i = 0
        # click on sell button
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/div/div/div[3]/div[2]/a/span').click()
        # wait for the uploading page to load
        time.sleep(8)
        # upload button
        upload = driver.find_element(By.XPATH, '//*[@id="photos"]/div[2]/div/div/div/div[5]/div/button')

        print(entries)

        # Uplaoding pictures from first folder
        try:
            for file in os.listdir(f'Products/{entries[i]}/'):
                print(entries[i])
                print(file)
                if file.endswith('.jpg'):
                    print(file)
                    upload.send_keys(f'Products/{entries[i]}/{file}')
                    time.sleep(10)
                    print('done')
                    time.sleep(5)
                    # upload = driver.find_element(By.XPATH,
                    #                              '/html/body/main/div/section/div/div[2]/section/div/div/div['
                    #                              '3]/div/div[2]/div/div/div/div[2]/div[2]/div/button/span')
        except IndexError:
            print("all files Completely  upload")

        # Writing and selecting different options on upload page
        try:
            for f in os.listdir(f'Products/{entries[i]}/'):
                print(entries[i])
                print(f)
                # Getting txt file for different options
                if f.endswith('.txt'):
                    print(f)

                    # Opening txt file
                    with open(f'Products/{entries[i]}/{f}', encoding='utf-8', errors='ignore') as rd:
                        print('text file opening and reading')
                        text = rd.read().splitlines()
                        print(text)

                        # Sending keys for title
                        title = driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                              '2]/section/div/div/div[5]/label[1]/div[2]/input')
                        title.send_keys(text[0])
                        time.sleep(3)

                        # Description
                        description = driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                    '2]/section/div/div/div[5]/label[2]/div[2]/textarea').click()
                        des = text[2:15]
                        for txt in text[2:15]:
                            pyperclip.copy(txt)
                            act = ActionChains(driver)
                            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
                            time.sleep(0.2)

                        # Scroll half page
                        driver.execute_script("return document.body.scrollHeight / 2")
                        time.sleep(3)

                        # dropdown for selecting category
                        category = driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                 '2]/section/div/div/div[7]/div/div/input')
                        category.click()
                        time.sleep(3)

                        select_cat = text[-9].split('/')
                        print(select_cat)

                        if 'Divertissement' in select_cat[0]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div[2]/section/div/div/div['
                                                          '7]/div/div/div[1]/div/div/div/ul/li[5]/div').click()
                            time.sleep(3)
                            if 'Jeux vidéo et consoles' in select_cat[1]:
                                driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                              '2]/section/div/div/div[7]/div/div/div[1]/div/div/div['
                                                              '2]/ul/li[1]/div').click()
                                time.sleep(3)
                                if 'Xbox Series X et S' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[1]/div').click()
                                    time.sleep(3)
                                    if 'Jeux' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Consoles' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Accessoires' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                elif 'Xbox One' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[2]/div').click()
                                    time.sleep(3)
                                    if 'Jeux' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Consoles' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Accessoires' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                elif 'Xbox antérieures' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[3]/div').click()
                                    time.sleep(3)
                                    if 'Jeux' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Consoles' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Accessoires' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                elif 'Playstation 5' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[4]/div').click()
                                    time.sleep(3)
                                    if 'Jeux' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Consoles' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Accessoires' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                elif 'Playstation 4' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[5]/div').click()
                                    time.sleep(3)
                                    if 'Jeux' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Consoles' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Accessoires' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                elif 'Playstation antérieures' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[6]/div').click()
                                    time.sleep(3)
                                    if 'Jeux' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Consoles' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Accessoires' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                elif 'Nintendo Switch' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[7]/div').click()
                                    time.sleep(3)
                                    if 'Jeux' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Consoles' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Accessoires' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                elif 'Nintendo Wii & Wii U' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[8]/div').click()
                                    time.sleep(3)
                                    if 'Jeux' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Consoles' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Accessoires' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                elif 'Nintendo 3DS & 2DS' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[9]/div').click()
                                    time.sleep(3)
                                    if 'Jeux' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Consoles' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Accessoires' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                elif 'Nintendo Game Boy' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[10]/div').click()
                                    time.sleep(3)
                                    if 'Jeux' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Consoles' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Accessoires' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                elif 'Nintendo antérieures' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[11]/div').click()
                                    time.sleep(3)
                                    if 'Jeux' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Consoles' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Accessoires' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                elif 'Sega' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[12]/div').click()
                                    time.sleep(3)
                                    if 'Jeux' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Consoles' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Accessoires' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                elif 'Jeux PC' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[13]/div/div[2]').click()
                                    time.sleep(3)
                                elif 'Réalité virtuelle' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[14]/div').click()
                                    time.sleep(3)
                                    if 'Jeux' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Consoles' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Accessoires' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                elif 'Retrogaming' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div/div/div['
                                                                  '1]/div/div/div['
                                                                  '2]/ul/li[15]/div').click()
                                    time.sleep(3)
                                    if 'Steam' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Intellivision' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Atari' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'ColecoVision' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[4]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Commodore' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[5]/div/div[2]').click()
                                        time.sleep(3)
                                    elif '3DO' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div/div/div['
                                                                      '1]/div/div/div[2]/ul/li[6]/div/div[2]').click()
                                        time.sleep(3)
                                        #  /html/body/main/div/section/div/div[2]/section/div/div/div[7]/div/div/div[1]/div/div/div[2]/ul/li[6]/div/div[2]/label/span[1]
                            elif 'Jeux et puzzles' in select_cat[1]:
                                driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                              '2]/section/div/div/div[7]/div/div/div[1]/div/div/div['
                                                              '2]/ul/li[2]/div').click()
                                time.sleep(3)
                                if 'Jeux de plateau' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div[1]/div/div['
                                                                  '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                    time.sleep(3)
                                elif 'Jeux de placement' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div[1]/div/div['
                                                                  '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                    time.sleep(3)
                                elif 'Jeux de cartes' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div[1]/div/div['
                                                                  '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                    time.sleep(3)
                                elif 'Puzzles' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div[1]/div/div['
                                                                  '1]/div/div/div[2]/ul/li[4]/div/div[2]').click()
                                    time.sleep(3)
                                elif 'Casse-têtes' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div[1]/div/div['
                                                                  '1]/div/div/div[2]/ul/li[5]/div/div[2]').click()
                                    time.sleep(3)
                                elif 'Jeux de voyage et de poche' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div[1]/div/div['
                                                                  '1]/div/div/div[2]/ul/li[6]/div/div[2]').click()
                                    time.sleep(3)
                                elif 'Jeux de société et de figurines' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div[1]/div/div['
                                                                  '1]/div/div/div[2]/ul/li[7]/div/div[2]').click()
                                    time.sleep(3)
                                elif "Jeux d'adresse" in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div[1]/div/div['
                                                                  '1]/div/div/div[2]/ul/li[8]/div/div[2]').click()
                                    time.sleep(3)
                                elif 'Jeux au sol' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div[1]/div/div['
                                                                  '1]/div/div/div[2]/ul/li[9]/div/div[2]').click()
                                    time.sleep(3)

                            elif 'Musique et vidéo' in select_cat[1]:
                                driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                              '2]/section/div/div/div[7]/div/div/div[1]/div/div/div['
                                                              '2]/ul/li[3]/div').click()
                                time.sleep(3)
                                if 'Musique' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div[1]/div/div['
                                                                  '1]/div/div/div[2]/ul/li[1]/div').click()
                                    time.sleep(3)
                                    if 'CD' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Cassettes' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Vinyles' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'Formats audio antérieurs' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[4]/div/div[2]').click()
                                        time.sleep(3)
                                elif 'Vidéo' in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div[1]/div/div['
                                                                  '1]/div/div/div[2]/ul/li[2]/div').click()
                                    time.sleep(3)
                                    if 'Blu-ray' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'DVD' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif 'VHS' in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)


                            elif 'Livres' in select_cat[1]:
                                driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                              '2]/section/div/div/div[7]/div/div/div[1]/div/div/div['
                                                              '2]/ul/li[4]/div').click()
                                time.sleep(3)
                                if "Littérature et fiction" in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div[1]/div/div['
                                                                  '1]/div/div/div[2]/ul/li[1]/div').click()
                                    time.sleep(3)
                                    if "Littérature classique" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Bandes dessinées" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Fiction contemporaine" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Policiers et thrillers" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[4]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Humour" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[5]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Poésie et théâtre" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[6]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Romance" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[7]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Science-fiction et fantastique" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[8]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Autre" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[9]/div/div[2]').click()
                                        time.sleep(3)

                                elif "Non-fiction" in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div[1]/div/div['
                                                                  '1]/div/div/div[2]/ul/li[2]/div').click()
                                    time.sleep(3)
                                    if "Arts et divertissement" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Biographies et mémoires" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Économie et affaires" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Informatique et technologie" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[4]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Cuisine" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[5]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Santé et bien-être" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[6]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Histoire" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[7]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Loisirs créatifs, décoration et passions" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[8]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Famille" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[9]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Politique et société" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[10]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Éducation et formation" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[11]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Livres de référence" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[12]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Religion et spiritualité" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[13]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Science et nature" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[14]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Sports" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[15]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Livres scolaires" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[16]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Voyages" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[17]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Autre" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[18]/div/div[2]').click()
                                        time.sleep(3)


                                elif "Enfants et jeunes adultes" in select_cat[2]:
                                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                  '2]/section/div/div/div[7]/div[1]/div/div['
                                                                  '1]/div/div/div[2]/ul/li[3]/div').click()
                                    time.sleep(3)
                                    if "Jeunes adultes" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[1]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Enfants" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[2]/div/div[2]').click()
                                        time.sleep(3)
                                    elif "Bébés" in select_cat[3]:
                                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                                      '2]/section/div/div/div[7]/div[1]/div/div['
                                                                      '1]/div/div/div[2]/ul/li[3]/div/div[2]').click()
                                        time.sleep(3)
                        else:
                            print(f'No Category with {select_cat[0]} found.')

                        # For Marque below code
                        Marque = driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                               '2]/section/div/div/div[7]/div[3]/div/input').click()
                        time.sleep(3)
                        if 'Shein' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[1]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Orchestra' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[2]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif "Tape à l'œil" in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[3]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Kiabi' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[4]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Pokémon' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[5]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Okaïdi' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[6]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'In Extenso' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[7]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Vertbaudet' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[8]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Decathlon' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[9]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Sergent Major' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[10]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Pull & Bear' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[11]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Obaïbi' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[12]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Petit Bateau' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[13]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Zara' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[14]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'H&M' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[15]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Puma' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[16]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Naf Naf' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[17]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Lacoste' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[18]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Tissaia' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[19]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Playmobil' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[20]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'C&A' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[21]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'La Halle' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[22]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Nike' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[23]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Jules' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[24]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Boutique Parisienne' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[25]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Undiz' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[26]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Gémo' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[27]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Kaporal' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[28]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Desigual' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[29]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Nintendo' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[30]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Jennyfer' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[31]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'TAO' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[32]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Creeks' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[33]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Jacadi' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[34]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Disney Baby' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[35]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'adidas' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[36]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Hollister' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[37]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Catimini' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[38]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Jack & Jones' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[39]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Converse' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[40]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Bizzbee' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[41]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'LEGO' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[42]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Verbaudet' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[43]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'POP' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[44]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Pimkie' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[45]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Celio' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[46]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'VTech' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[47]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Camaïeu' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[48]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Primark' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[49]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Tally Weijl' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[50]/div/div[2]/label/span[1]').click()
                            time.sleep(3)
                        elif 'Sans marque' in text[-7]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[3]/div/div['
                                                          '1]/div/div/div/ul/li[51]/div[2]/div[2]/label/span['
                                                          '1]').click()
                            time.sleep(3)
                        else:
                            print(f'No Marque with "{text[-7]}" found.')

                        # For Etat below code
                        if 'Neuf avec étiquette' in text[-5]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[5]/div/div['
                                                          '1]/div/div/div/ul/li[1]/div/div[2]/label').click()
                            time.sleep(3)
                        elif 'Neuf sans étiquette' in text[-5]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[5]/div/div['
                                                          '1]/div/div/div/ul/li[2]/div/div[2]/label').click()
                            time.sleep(3)
                        elif 'Très bon état' in text[-5]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[5]/div/div['
                                                          '1]/div/div/div/ul/li[3]/div/div[2]/label').click()
                            time.sleep(3)
                        elif 'Bon état' in text[-5]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[5]/div/div['
                                                          '1]/div/div/div/ul/li[4]/div/div[2]/label').click()
                            time.sleep(3)
                        elif 'Satisfaisant' in text[-5]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[7]/div[5]/div/div['
                                                          '1]/div/div/div/ul/li[5]/div/div[2]/label').click()
                            time.sleep(3)
                        else:
                            print(f'No Etat with "{text[-5]}" found.')

                        # For Prix below code
                        driver.find_element(By.XPATH, '/html/body/main/div/section/div/div[2]/section/div/div/div['
                                                      '9]/div/div/div/label/div[2]/input').send_keys(text[-3])

                        # Scroll all the way down
                        driver.execute_script("return document.body.scrollHeight")
                        time.sleep(3)

                        # For Format below code
                        if 'Petit' in text[-1]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[10]/div/div[2]/div/div[2]').click()
                            time.sleep(3)
                        elif 'Moyen' in text[-1]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[10]/div/div[3]/div/div[2]').click()
                            time.sleep(3)
                        elif 'Grand' in text[-1]:
                            driver.find_element(By.XPATH, '/html/body/main/div/section/div/div['
                                                          '2]/section/div/div/div[10]/div/div[4]/div/div[2]').click()
                            time.sleep(3)
                        else:
                            print(f'No Format with "{text[-1]}" found.')

                    # Submit button
                    driver.find_element(By.XPATH, '/html/body/main/div/section/div/div[2]/section/div/div/div['
                                                  '14]/div/button[2]').click()
                else:
                    print(f'Data file for {entries[i]} not found!!!!')
                    pass
        except IndexError:
            print('all files scaned')
        if i == len(entries):
            time.sleep(14400)
        else:
            i += 1
    else:
        time.sleep(14400)
