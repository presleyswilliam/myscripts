from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)
driver.get("https://www.weather.gov")
elemUser = driver.find_element_by_id("inputstring")
elemUser.clear()
elemUser.send_keys("45245")
time.sleep(1)
driver.find_element_by_id("btnSearch").click()
time.sleep(1)

elemTemp = driver.find_element_by_class_name("myforecast-current-lrg")
elemTemp = elemTemp.get_attribute('innerHTML')
elemTemp = elemTemp.split('°')[0]
#print(elemTemp)
currentTime = datetime.datetime.now()
currentTimeString = currentTime.strftime("%d-%b-%Y (%H:%M:%S.%f)")

f = open("weatherData.txt", "a")
f.write(elemTemp + "_" + currentTimeString + ";")
f.write("\r\n")
f.close()

driver.quit()
