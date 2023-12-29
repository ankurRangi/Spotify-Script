# Ankur Rangi (IIITD)
# Credits deserved??
from Credentials import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import datetime


# Python Script
path = "Path_to_chromedrive"

driver = webdriver.Chrome(executable_path=path)
driver.get('https://open.spotify.com/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

mute_status = False

def login():
    login_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]")
    login_btn.click()
    wait.until(EC.visibility_of_element_located((By.ID, 'login-username')))
    username = driver.find_element_by_id("login-username")
    # password = driver.find_element_by_id("password")
    # password.send_keys(getPassword())
    # driver.find_element_by_name("submit").click()
    # type_text(getUsername())
    username.send_keys(getUsername())
    tab()
    type_text(getPassword())
    times(tab, 2)
    enter()
    # onetrust-close-btn-handler
    # onetrust-close-btn-container
    # wait.until(EC.visibility_of_element_located((By.ID, 'onetrust-close-btn-handler')))
    # cookie_btn = driver.find_element_by_id("onetrust-close-btn-container")
    # cookie_btn.click()


def times(fun, times):
    for _ in range(times):
        fun()


def type_text(text):
    action = ActionChains(driver)
    action.send_keys(text)
    action.perform()


def press_key(key):
    type_text(key)


def tab():
    press_key(Keys.TAB)


def enter():
    press_key(Keys.ENTER)


def mute():
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class,'volume-bar__icon-button')]")))
    mute_btn = driver.find_element_by_xpath("//button[contains(@class,'volume-bar__icon-button')]")
    mute_btn.click()


def unmute():
    mute()


def songName():
    path = "//*[@id='main']/div/div[2]/div[2]/footer/div/div[1]/div"
    wait.until(EC.visibility_of_element_located((By.XPATH, path)))
    song_name = driver.find_elements_by_id('main')
    return 'learn more' in ''.join(elem.text for elem in song_name).lower()


def nowPlayingAdd():
    sleep(0.2)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='main']/div/div[2]/div[2]/footer/div/div[1]/div")))
    now_playing_text = driver.find_elements_by_id('main')
    return 'learn more' in ''.join(elem.text for elem in now_playing_text).lower()


def CurrentTime():
    print("#####################################")
    print("Started at: " + str(datetime.datetime.now()))


login()
add_count = 0
flag = 0
while True:
    if nowPlayingAdd() == True and mute_status == False:
        mute()
        add_count = add_count + 1
        print("Current number of adds muted: ", add_count)
        add_count = add_count + 1
        mute_status = True
    elif nowPlayingAdd() == False and mute_status == True:
        unmute()
        mute_status = False
    else:
        if flag == 0:
            CurrentTime()
        flag = 1
        continue

