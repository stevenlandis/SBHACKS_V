import webbrowser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import keyword as key

def Open_Youtube():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    url = "http://youtube.com/"
    # os.startfile(chrome_path)
    webbrowser.get(chrome_path).open(url)

def Open_Spotify():
    from spotify_local import SpotifyLocal

    with SpotifyLocal() as s:
        pass