#1.Click the lab.
#2.Enter the number of clicks
#3.Select whether to automatically click the upgrade button
#4.Wait for 3 seconds
#5.Run the program
#https://particle-clicker.web.cern.ch/


import pyautogui as p

import time as t


def liandianqi():
        a = int(input("Enter the number of clicks: "))
        b = int(input("Enter 1 if you want to auto upgrades other wise enter 0: "))
        t.sleep(3)
        for i in range(0,a):
                p.moveTo(798,448)
                p.click()
        if b == 1:
                p.moveTo(125,269)
                p.click()
                p.moveTo(105,407)
                p.click()
                p.moveTo(124,543)
                p.click()
                p.moveTo(140,674)
                p.click()
                p.moveTo(1362,282)
                p.click()
                p.moveTo(1347,432)
                p.click()
                p.moveTo(1342,580)
                p.click()
                p.moveTo(1354,716)
                p.click()
                p.moveTo(1344,782)
                p.click()
                p.moveTo(1666,306)
                p.click()
                p.moveTo(1666,468)
                p.click()
                p.moveTo(1666,597)
                p.click()
                p.moveTo(1666,723)
                p.click()
                p.moveTo(1666,854)
                p.click()
                p.moveTo(1667,988)
        
        


