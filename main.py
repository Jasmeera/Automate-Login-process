from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
  #set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver

#function untuk ambik no sahaja
def clean_text(text):
  """"Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output
  
def main():
  driver = get_driver()

  #Find and fill username and password
  driver.find_element(by="id",value="id_username").send_keys("automated")
#takda return, it will not return anything
  time.sleep(2) #time gap 2 sec
  driver.find_element(by="id",value="id_password").send_keys("automatedautomated"+ Keys.RETURN)
  time.sleep(2) 

  #Click on Home Link and wait 2 sec
  driver.find_element(by="xpath", value = "/html/body/nav/div/a").click()
  print (driver.current_url) #ni print url yang kita nak masuk
  time.sleep(2) #wait for 2 seconds untuk tunggu halaman selesai loading
  
  #scrape temperature value
  element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)

  
print(main())
