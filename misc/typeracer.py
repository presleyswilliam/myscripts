# CREATED FOR
# MACBOOK PRO LAPTOP


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import time

options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

#driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
driver.get("https://play.typeracer.com/")

trying = True
while (trying):
    try:
        elemEnterRaceParent = driver.find_element_by_id("gwt-uid-1")
        elemEnterRace = elemEnterRaceParent.find_element_by_class_name("prompt-button")
        elemEnterRace.click()
        trying = False
    except Exception as e: 
        time.sleep(0.5)

def race(inputDelay, gwtUid):
    trying = True
    count = 0
    #inputDelay = 0.1
    typeByWordsOrLetters = "Letters" #"Words" #"Letters"
    while (trying):
        try:
            message = ""

            userBox = driver.find_element_by_xpath("//*[@id=\"gwt-uid-" + gwtUid + "\"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div")
            userBoxToType = userBox.find_elements_by_xpath(".//*")
            for i in range(0, len(userBoxToType)):
                toType = userBoxToType[i].get_attribute("innerHTML")
                message += toType

            messageToType = message.split()
            #print(messageToType)
            for i in range(0, len(messageToType)):
                userInput = driver.find_element_by_xpath("//*[@id=\"gwt-uid-" + gwtUid + "\"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input")
                #userInput = driver.find_element_by_class_name("txtInput")
                if (typeByWordsOrLetters == "Words"):
                    toType = messageToType[i]
                    userInput.send_keys(toType)
                    time.sleep(inputDelay)
                else:
                    for n in range(0, len(messageToType[i])):
                        userInput.send_keys(messageToType[i][n])
                        time.sleep(inputDelay)
                if (i < len(messageToType) - 1):
                    userInput.send_keys(" ")
                    time.sleep(inputDelay)
                else:
                    break

            trying = False
            count = 0
            #time.sleep(30)
        except Exception as e:
            #print(e)
            count += 1
            #print("Not Ready Yet")
            time.sleep(0.5)
            # if (count > 30):
            #     break

def raceAgain():
    trying = True
    while (trying):
        try:
            raceAgain = driver.find_element_by_class_name("raceAgainLink")
            raceAgain.click()
            trying = False
        except Exception as e: 
            time.sleep(0.5)

def closePopUp():
    trying = True
    while (trying):
        try:
            closePopUp = driver.find_element_by_link_text("No thanks :(")
            closePopUp.click()
            trying = False
        except Exception as e: 
            time.sleep(0.5)


def end():
    driver.quit()

def main():
    race(0.09, "17")
    time.sleep(2)
    # raceAgain()

    # race(0.09, "28")
    # time.sleep(2)
    # #closePopUp()
    # time.sleep(3)
    # raceAgain()

    # race(0.09, "41")
    # time.sleep(5)
    # raceAgain()

    # race(0.09, "52")
    # time.sleep(10)
    # raceAgain()

    end()

if __name__ == "__main__":
    main()