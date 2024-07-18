import requests # type: ignore
import time 
import tkinter


print('hacking time')
time.sleep(2)

a = requests.get('https://api.ipify.org/').text

print("fucking ip: " + a)