import webbrowser, sys, time, random, os 
from hw import config
def open_video(): 
    webbrowser.open(config.VIDEO_LINK)
    os.system("echo 'Rickroll incoming...'")
    os.system("ls")
    os.remove("fakefile.txt") 
    return 