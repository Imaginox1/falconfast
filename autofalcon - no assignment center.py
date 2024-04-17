from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from time import sleep

 
gmailId = input('Enter the gmailid')
 
pwd = getpass('Enter Password:')


try:
    driver = webdriver.Edge(r"C:\edgedriver_win64 (1).zip\msedgedriver.exe")
    sleep(5)
    driver.get(r'https://faithkids.myschoolapp.com/app/?fromHash=login#login')
    sleep(5)
    driver.maximize_window()

    #sleep(20)
    
    #driver.get(r'https://faithkids.myschoolapp.com/app/?fromHash=login#login')
    
    sleep(10)
    
    loginBox = driver.find_element(By.ID, 'Username')
    loginBox.send_keys(gmailId)
 
    nextButton = driver.find_element(By.ID, 'nextBtn')
    nextButton.click()
 
    sleep(10)
 
    nextButton = driver.find_element(By.ID, 'googleButtonLabel')
    nextButton.click()
    
    sleep(10)
    
    loginBox = driver.find_element(By.ID, 'identifierId')
    loginBox.send_keys(gmailId)
 
    sleep(10)
 
    nextButton = driver.find_element(By.ID, 'identifierNext')
    nextButton.click()
    
    sleep(10)
    
    passWordBox = driver.find_element(By.NAME, 'Passwd')
    passWordBox.send_keys(pwd)
 
    nextButton = driver.find_element(By.ID, 'passwordNext')
    nextButton.click()
    
##    sleep(15)
##    
##    nextButton = driver.find_element(By.ID, 'assignment-center-btn')
##    nextButton.click()
 
    print('Login Successful...!!')
    sleep(10000)
    driver.quit()
except:
    print('Login Failed')
    sleep(30)
    driver.quit()
