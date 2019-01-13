import webbrowser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import keyword as key
def Youtube_Mode():
    url = "https://www.youtube.com/"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
    # driver = webdriver.Chrome(executable_path=chrome_path)
    # driver.navigate('https://stackoverflow.com/')
    #action = ActionChains(driver)
    # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


    from selenium import webdriver

    driver = webdriver.Chrome(chrome_path)

    driver.close()
    driver.quit()