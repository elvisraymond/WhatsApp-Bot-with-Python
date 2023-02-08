# Importing Libs
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# recipient storage + message to send
timeSleep = 2
ContactName = "Junior Skratos"
MessageToSend = "Hi ! I'm sending this message via my WhatsApp Bot!!"

# initialization + installation of Chrome Manager and launching WhatsAppWeb via selenium
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

# We will wait for user authentication via the QR code
print("PLease scan the QR code and press Enter when it's done")
input()
print("Congrats you're logged in !")

input()
# Go to the WhatsApp search bar and enter the recipient's name
input_path_searchContact = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
input_box_searchContact = driver.find_element(by=By.XPATH, value=input_path_searchContact)
input_box_searchContact.click()

time.sleep(timeSleep) 

# enter the name of the recipient
input_box_searchContact.send_keys(ContactName)
time.sleep(timeSleep)
selected_contact = driver.find_element(by=By.XPATH, value ="//span[@title='"+ContactName+"']")
selected_contact.click()

# type the message and we send it
input_path_messageBox = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
input_messageBox = driver.find_element(by=By.XPATH, value=input_path_messageBox)
time.sleep(timeSleep)

# send the message
input_messageBox.send_keys(MessageToSend + Keys.ENTER)
time.sleep(timeSleep)

# We close the script
print("Message send. press Enter to quit")
input()
print("Logged Out")
driver.quit()
quit()