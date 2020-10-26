import matplotlib.pyplot as plt
from datetime import datetime

dateArray = []
tempArray = []

def getData(filePath):
    with open(filePath, "r") as fp:
        for cnt, line in enumerate(fp):
            temp = int(line.split("_")[0])
            tempArray.append(temp)
            date = line.split("_")[1]
            datetime_object = datetime.strptime(date, "%d-%b-%Y (%H:%M:%S.%f); ")
            dateArray.append(datetime_object)
    return tempArray

filePath = "/home/pi/myscripts/weatherData.txt"
getData(filePath)


plt.figure(1)   #plotting temp(F) vs date graph
xArray = range(0, len(tempArray))
plt.plot(dateArray, tempArray)
plt.title("Weather Temps - TESTING SERVICE CHANGE")
plt.xlabel("Date")
plt.ylabel("Temperature (F)")
plt.show()

