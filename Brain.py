import os
import shutil
import random
import datetime
from time import ctime,sleep


import urllib.request
import urllib.parse
import re
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import requests
import webbrowser


## Python Scripts Import ##
from Functions.OS_Folder import *
from Functions.Web_Folder import *


### SCRIPT TAKE IN A LIST OF KEYWORDS AND EXECUTE COMPUTING ACTIONS TO ACHIEVE INTENDED RESULT ###


# search - search,search_term,site
# search - search,search_term,site,islocation

def SEARCH(keywords):
    search_term = keywords[0]
    site = keywords[1]
      
    if 'youtube' in site or 'yt' in site:
        # Search and play first yt video found #
        result_status = search_on_YT(search_term)
    else:
        # Search the term on a search engine #
        result_status = search_on_engine(search_term,site)

def SOFTWARE(keywords):
    app_name = keywords[0]
    if app_name == 'steam':
        os.startfile(r"C:\Program Files (x86)\Steam\steam.exe")
    elif app_name == 'python':
        os.startfile(r"C:\Users\Nabil\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10\IDLE (Python 3.10 64-bit)")
    elif app_name == 'spotify':
        os.startfile(r"C:\Users\Nabil\AppData\Roaming\Spotify\Spotify.exe")
    elif app_name == '{folder}':
        os.startfile(r"C:\Users\Nabil\Desktop\Coding")
    else:
        raise Exception


def SETUP(keywords):
    mode = keywords[0]
    if mode == 'default':
        os.startfile(r"C:\Program Files (x86)\Steam\steam.exe")
        os.startfile(r"C:\Users\Nabil\AppData\Roaming\Spotify\Spotify.exe")
        os.startfile(r"C:\Program Files\Rainmeter\Rainmeter.exe")
    # spotify,steam,rainmeter
    elif mode == 'code':
        os.startfile(r"C:\Users\Nabil\Desktop\Coding")
        os.startfile(r"C:\Users\Nabil\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    # open VS,Code Folder,




def OPEN():
    options = ['website','game']
    print('Options: ')
    for i in range(len(options)):
        print(str(i) + '. ' + options[i])
    reply = 'What would you like to open?: '
    item = input(reply)
    if 'website' in item:
        # Opens first website found #
        ### PYTHON SELENIUM SCRIPT LINK ##
        pass
    if 'game' in item:
        options = ['Steam']
        print('Options: ')
        for i in range(len(options)):
            print(str(i+1) + '. ' + options[i])
        reply = 'What software would you like to open?'
        software = input(reply)
        if 'Genshin Impact' in software or 'game' in software:
            print('Opening chosen software now...')
            os.startfile (r"C:\Program Files\Genshin Impact\launcher.exe")

def CREATE():
    options = ['file','folder']
    print('Options: ')
    for i in range(len(options)):
        print(str(i+1) + '. ' + options[i])
    reply = 'What do you want to create?: '
    item = input(reply)
    if 'file' in item:
        reply = 'What is the name of the file?: '
        name = input(reply)
        open(f'{name}.txt','w').close()
        reply = 'What is the file extension? (default:txt): '
        ext = input(reply)
        os.rename(f'{name}.txt',f'{name}.{ext}')
        print('A new file has been created under the same directory')
    if 'folder' in item:
        reply = 'What is the folder name?: '
        name = input(reply)
        curr_dir = os.getcwd()
        #parent_dir = os.path.dirname(curr_dir)
        path = os.path.join(curr_dir,name)
        os.mkdir(path)
        print("A new folder '% s' has been created" % path)

def MOVE():
    options = ['file','folder']
    print('Options: ')
    for i in range(len(options)):
        print(str(i+1) + '. ' + options[i])
    reply = 'What do you want to move?: '
    item = input(reply)
    if 'file' in item:
        reply = 'Name of file?: '
        file_name = input(reply)
        reply = 'Destination folder? (Directory Address C:): '
        dest_folder = input(reply)
        src_folder = os.getcwd()
        shutil.move(src_folder + "\\" + file_name, dest_folder + "\\" + file_name)
    if 'folder' in item:
        reply = 'Source folder? (Directory Address C:): '
        filename = input(reply)
        reply = 'Destination folder? (Directory Address C:): '
        dest_folder = input(reply)
        src_folder = os.getcwd()
        shutil.move(src_folder, dest_folder)

# PREPROCESSING FUNCTIONS FOR MAIN APP #
def get_todays_top_10_news():
    headlines = get_latest_news_sg()
    selected = []
    for i in range(10):
        rand = random.randint(0,len(headlines)-1)
        selected.append(headlines[rand])
    return selected




