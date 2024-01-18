from random import randrange
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


include_capitals=False
include_numbers=False
include_symbols=False

numbers="0123456789"
symbols="!@#$%^&*()-_"
capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string="abcdefghijklmnopqrstuvwxyz"
password=""

lenght=int(input("what lenght? "))
sar=[]

print("include numbers? ")
x=input("")
if x=="yes":
    include_numbers=True

print("include symbols? ")
x=input("")
if x=="yes":
    include_symbols=True

print("include capital letters? ")
x=input("")
if x=="yes":
    include_capitals=True


if include_numbers:
    string=string+numbers

if include_capitals:
    string=string+capital

if include_symbols:
    string=string+symbols


for z in range (3):

    password=""

    for i in range (lenght):
        password=password+string[randrange(len(string))]
    
    
    sar.append(password)
    
url = "https://www.passwordmonster.com/"
driver.get(url)
time.sleep(1)

for i in range (3):
    password=sar[i]
    find=driver.find_element(By.XPATH, '//*[@id="lgd_out_pg_pass"]')
    find.send_keys(password)
    find.clear()
    time.sleep(1)
    find=driver.find_element(By.XPATH, '//*[@id="first_estimate"]/h1')
    output=find.get_attribute("outerHTML")
    output=str(output)
    output=output[4:-5]
    sar.append(output)

for i in range (3):
    print("password", sar[i])
    print ("time to guess: ", sar[i+3], "\n")

