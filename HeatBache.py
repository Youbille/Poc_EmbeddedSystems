# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:34:33 2020

@author: gauth
"""

import time
import os
import board
from busio import I2C
import adafruit_bme680
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()


tempData = np.zeros((5,5))
#create library object 
i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

#change this to match the location's pressure
bme680.sea_level_pressure = 1013.25

for i in range(5):
    for j in range(5):
        tempData[i,j] = bme680.temperature
        time.sleep(5)
        print("moving sensor")
heatMap = sns.heatmap(tempData)
print("The humidity is %s" % bme680.humidity)
print("The pressure is %s" % bme680.pressure)
if os.path.exists("heatMap.png"):
        os.remove("heatMap.png")
plt.savefig("heatMap.png")
