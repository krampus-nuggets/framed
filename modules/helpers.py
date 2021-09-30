import os
import time
from modules.banners import print_banner

def check_dir(directory):
    check_p = os.path.exists(directory)

    if check_p:
        return True
    else:
        os.makedirs(directory)
        return False

def video_list(directory):
    all_files = [file for file in os.listdir(directory) if file.endswith(".mp4")]
    return all_files

def invalid_option(recurse_function, print_text):
    print_banner("single", "header-start")
    print(print_text)
    time.sleep(2)
    recurse_function()
