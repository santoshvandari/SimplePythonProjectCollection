# Write the Program to automate the monkey type website using selenium and python.
import time
from bs4 import BeautifulSoup 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui
url = "https://monkeytype.com/"
driver_path = '/chromedriver'
options = Options()
options.add_argument('--binary-location={}'.format(driver_path))
driver = webdriver.Chrome(options=options)
driver.get(url) 
time.sleep(2)  # Use sleep to give the page some time to load
elementwords=driver.find_element(By.ID, 'words')
soup = BeautifulSoup(elementwords.get_attribute('innerHTML'), 'html.parser')
words = soup.find_all('div','word')
wordscollection = []
for word in words:
    wordletters = word.find_all('letter')
    wordtext = ""
    for letter in wordletters:
        wordtext += letter.text
    wordscollection.append(wordtext)
text_block = " ".join(word for word in wordscollection)
keep_going = True
while keep_going:
    try:
        for letter in wordscollection:
            pyautogui.write(letter  + " ")
        old_text_block = text_block
        search_string=old_text_block[-10:]
        elementwords=driver.find_element(By.ID, 'words')
        soup = BeautifulSoup(elementwords.get_attribute('innerHTML'), 'html.parser')
        words = soup.find_all('div','word')
        wordscollection = []
        for word in words:
            wordletters = word.find_all('letter')
            wordtext = ""
            for letter in wordletters:
                wordtext += letter.text
            wordscollection.append(wordtext)
        text_block = (" ".join(word for word in wordscollection))
        text_block = text_block[text_block.index(search_string):].replace(search_string, "")
        wordscollection = text_block.split(" ")
    except :
        keep_going = False
input("Press Enter to close the browser...")