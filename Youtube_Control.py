import webbrowser
import keyword as key

def Open_Youtube(arg):
    if arg == 0:
        return

    try:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = "http://youtube.com/"
        # os.startfile(chrome_path)
        webbrowser.get(chrome_path).open(url)
    except Exception as e:
        print(e)

def Open_New_Tab(arg):
    if arg == 0:
        return

    try:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = "https://google.com/"
        # os.startfile(chrome_path)
        webbrowser.get(chrome_path).open(url)
    except Exception as e:
        print(e)

def Open_Spotify():
    from spotify_local import SpotifyLocal

    with SpotifyLocal() as s:
        pass