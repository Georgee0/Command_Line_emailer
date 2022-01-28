from selenium import webdriver
from selenium.webdriver.common.keys import Keys

email_username = input('What is your username?\n')
email_password = input('What is your password?\n')
email_recipient = input('Who would you like to send an email to?\n')
email_subject = input('What is the subject of the email?\n')
email_body = input('What would you like to say?\n')

# Acceesing website
browser = webdriver.Firefox()
browser.implicitly_wait(40)
browser.get('https://accounts.google.com/signin') 

# Login username
loginElem = browser.find_element_by_id('identifier')
loginElem.send_keys(email_username)

# Login password
passwordElem = browser.find_element_by_class_name('password')
passwordElem.send_keys(email_password)

# Signig in
submitElem = browser.find_element_by_id('passwordNext')
submitElem.click()

# Get current url
browser.get('http//https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')

# Compose mail
composeElem = browser.find_elements_by_class_name('T-I T-I-KE L3')
composeElem.click()

html_elem = browser.find_element_by_tag_name('html')
html_elem.send_keys('c')
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_recipient)
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_subject)
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_body)
html_elem.send_keys(Keys.ENTER)

print('Email was sent successfully.')
