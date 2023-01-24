from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
import os
from dotenv import load_dotenv

# setting up logging parameters
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(),logging.FileHandler(filename='fb_send_msg.log')]
)

driver = webdriver.Firefox()

def fb_login(login_email,login_pass):

    url = 'https://www.facebook.com/'
    driver.get(url)
    logging.info('Facebook opened in browser. Initiating 15 seconds of wait time.')
    time.sleep(15)
    logging.info('Wait time has elapsed')

    email_input_box = driver.find_element(By.ID,'email')
    email_input_box.click()
    email_input_box.send_keys(login_email)
    time.sleep(1)

    pass_input_box = driver.find_element(By.ID,'pass')
    pass_input_box.click()
    pass_input_box.send_keys(login_pass)
    time.sleep(1)

    login_button = driver.find_element(By.CSS_SELECTOR,'button[name="login"]')
    return login_button.click()

# if you want to write a long message from a txt file
def write_msg_from_txt_file(file_path):
    """function to read the message from a file

    Args:
        file_path (string): the relative path of the txt file from which message will be read

    Returns:
        string: the message as text from the txt file
    """
    with open(file_path,'r') as reader:
        msg_from_txt = reader.read()
    return msg_from_txt

load_dotenv()

# setting up environmental vairables
my_email = os.getenv('email')
my_pass = os.getenv('password')

# log in to to Facebook
fb_login(login_email=my_email,login_pass=my_pass)
time.sleep(5)

# clicking on messenger icon
messenger_icon_xpath = '/html/body/div[1]/div[1]/div[1]/div/div[2]/div[4]/div[1]/div[2]'
messenger_icon_elem = driver.find_element(by=By.XPATH,value=messenger_icon_xpath)
messenger_icon_elem.click()
logging.info('Messenger icon clicked')
time.sleep(1)


# clicking 'See all in Messenger'
messenger_see_all = driver.find_element(By.CSS_SELECTOR,"a[aria-label='See all in Messenger']")
messenger_see_all.click()
logging.info('Messenger page opened')
time.sleep(1)

def send_invitation(name, message):    
    # searching for name in the search bar
    search_name_input_box = driver.find_element(By.CSS_SELECTOR,"input[aria-label='Search Messenger']")
    search_name_input_box.send_keys(name)
    logging.info(f'Written {name} in the message box')
    time.sleep(1)

    # clicking on the first result
    # all the search results have this css class 'xh8yej3'
    chat_search_suggested_list = driver.find_elements(By.CSS_SELECTOR,"li[class = 'xh8yej3']")
    # the first result is 'Search messages for name_to_message', second result is the name_to_message
    chat_search_suggested_list[1].click()
    logging.info(f'Clicked on the name {name}')
    time.sleep(1)

    # writing the message in the message box
    send_msg_box_css_sel = "div[aria-label = 'Message']"
    send_msg_box = driver.find_element(By.CSS_SELECTOR,send_msg_box_css_sel)
    # for some reason, only working when keys are being sent one at a time
    for key in message:
        send_msg_box.send_keys(key)
    logging.info(f'Message written into text box')

    # clicking the send button
    send_button = driver.find_element(By.CSS_SELECTOR,"div[aria-label = 'Press enter to send']") 
    send_button.click()
    logging.info(f'Message has been sent to {name}')

# list to ensure people invited
invited_list = []

# getting list of names and the message content
name_list_file = os.getenv('list_of_names')
message_file = os.getenv('msg_file')

message_from_file = write_msg_from_txt_file(message_file)

with open(file=name_list_file,mode='r',encoding='utf8') as name_reader:  # utf8 helps read names in any language e.g. Bengali, Chinese etc.
    name_file_content = name_reader.read()
    names_list = name_file_content.split('\n')

for name_in_list in names_list:
    send_invitation(name=name_in_list,message=message_from_file)
    invited_list.append(name_in_list)
    logging.info(f'Invitation sent to {name_in_list}')
    time.sleep(5)

with open(file='invited_list.txt',mode='a',encoding='utf8') as list_writer:
    list_writer.write('\n'.join(invited_list))
    logging.info('List of invited people written to file')