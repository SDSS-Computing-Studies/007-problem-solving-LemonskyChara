#1.Click the lab.
#2.Enter the number of clicks
#3.Select whether to automatically click the upgrade button
#4.Wait for 3 seconds
#5.Run the program


import pyautogui as p

import time as t

#1.click the lap
def liandianqi():
        a = int(input("Enter the number of clicks: "))
        t.sleep(2)
        for b in range(0,a):
                p.moveTo(798,448)
                p.click()
#2.reseach
def researchup():
        t.sleep(3)
        p.moveTo(116,253)
        t.sleep(0.5)
        if p.pixelMatchesColor(116,253,(40,96,144)):
                for i in range(0,3):
                        p.click(116,253)
        p.moveTo(107,403)
        t.sleep(0.5)
        if p.pixelMatchesColor(107,403,(40,96,144)):
                for i in range(0,3):
                        p.click(107,403)
        p.moveTo(112,532)
        t.sleep(0.5)
        if p.pixelMatchesColor(112,532,(40,96,144)):
                for i in range(0,3):
                        p.click(112,532)
        p.moveTo(110,686)
        t.sleep(0.5)
        if p.pixelMatchesColor(110,686,(40,96,144)):
                for i in range(0,3):
                        p.click(110,686)
        p.moveTo(113,855)
        t.sleep(0.5)
        if p.pixelMatchesColor(113,855,(40,96,144)):
                for i in range(0,3):
                        p.click(113,855)
        p.moveTo(107,988)
        t.sleep(0.5)
        if p.pixelMatchesColor(107,988,(40,96,144)):
                for i in range(0,3):
                        p.click(107,988)
        #
        p.moveTo(310,407)
        p.mouseDown()
        p.moveTo(310,900)
        p.mouseUp()
        p.moveTo(128,358)
        t.sleep(0.5)
        if p.pixelMatchesColor(128,358,(40,96,144)):
                for i in range(0,3):
                        p.click(128,358)
        p.moveTo(115,509)
        t.sleep(0.5)
        if p.pixelMatchesColor(115,509,(40,96,144)):
                for i in range(0,3):
                        p.click(115,509)
        p.moveTo(118,660)
        t.sleep(0.5)
        if p.pixelMatchesColor(118,660,(40,96,144)):
                for i in range(0,3):
                        p.click(118,660)
        p.moveTo(118,811)
        t.sleep(0.5)
        if p.pixelMatchesColor(118,811,(40,96,144)):
                for i in range(0,3):
                        p.click(118,811)
        p.moveTo(122,984)
        if p.pixelMatchesColor(122,984,(40,96,144)):
                for i in range(0,3):
                        p.click(122,984)
        p.moveTo(310,900)
        p.mouseDown()
        p.moveTo(310,407)
        p.mouseUp()

#3 HR UPGRADE
def HRup():
        t.sleep(2)
        p.moveTo(1348,274)
        t.sleep(0.5)
        if p.pixelMatchesColor(1348,274,(40,96,144)):
                for i in range(0,3):
                        p.click(1348,274)
        p.moveTo(1354,421)
        t.sleep(0.5)
        if p.pixelMatchesColor(1354,421,(40,96,144)):
                for i in range(0,3):
                        p.click(1354,421)
        p.moveTo(1348,572)
        t.sleep(0.5)
        if p.pixelMatchesColor(1348,572,(40,96,144)):
                for i in range(0,3):
                        p.click(1348,572)
        p.moveTo(1348,705)
        t.sleep(0.5)
        if p.pixelMatchesColor(1348,705,(40,96,144)):
                for i in range(0,3):
                        p.click(1348,705)
        p.moveTo(1348,857)
        t.sleep(0.5)
        if p.pixelMatchesColor(1348,857,(40,96,144)):
                for i in range(0,3):
                        p.click(1348,857)
        p.moveTo(1348,1007)
        t.sleep(0.5)
        if p.pixelMatchesColor(1348,1007,(40,96,144)):
                for i in range(0,3):
                        p.click(1348,1007)
        #
        p.moveTo(1593,340)
        p.mouseDown()
        p.moveTo(1589,666)
        p.mouseUp()
        p.moveTo(1348,855)
        t.sleep(0.5)
        if p.pixelMatchesColor(1348,855,(40,96,144)):
                for i in range(0,3):
                        p.click(1348,855)
        p.moveTo(1348,982)
        t.sleep(0.5)
        if p.pixelMatchesColor(1348,982,(40,96,144)):
                for i in range(0,3):
                        p.click(1348,982)
        p.moveTo(1589,666)
        p.mouseDown()
        p.moveTo(1593,340)
        p.mouseUp()        

#4 Upgrades
def Upgrades():
        t.sleep(2)
        p.moveTo(1667,285)
        t.sleep(0.5)
        if p.pixelMatchesColor(1667,285,(40,96,144)):
                for i in range(0,3):
                        p.click(1667,285)
        p.moveTo(1667,472)
        t.sleep(0.5)
        if p.pixelMatchesColor(1667,472,(40,96,144)):
                for i in range(0,3):
                        p.click(1667,472)
        p.moveTo(1667,679)
        t.sleep(0.5)
        if p.pixelMatchesColor(1667,679,(40,96,144)):
                for i in range(0,3):
                        p.click(1667,679)
        p.moveTo(1667,810)
        t.sleep(0.5)
        if p.pixelMatchesColor(1667,810,(40,96,144)):
                for i in range(0,3):
                        p.click(1667,810)
        p.moveTo(1667,940)
        t.sleep(0.5)
        if p.pixelMatchesColor(1667,940,(40,96,144)):
                for i in range(0,3):
                        p.click(1667,940)
        #
        p.moveTo(1910,384)
        p.mouseDown()
        p.moveTo(1908,696)
        p.mouseUp()
        p.moveTo(1667,851)
        t.sleep(0.5)
        if p.pixelMatchesColor(1667,851,(40,96,144)):
                for i in range(0,3):
                        p.click(1667,851)
        p.moveTo(1667,983)
        t.sleep(0.5)
        if p.pixelMatchesColor(1667,983,(40,96,144)):
                for i in range(0,3):
                        p.click(1667,983)
        p.moveTo(1908,696)
        p.mouseDown()
        p.moveTo(1908,384)
        p.mouseUp()            

def main():
        liandianqi()
        researchup()
        HRup()
        Upgrades()
