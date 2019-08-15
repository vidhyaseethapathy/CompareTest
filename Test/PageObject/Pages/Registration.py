from time import sleep

from selenium.webdriver.common.by import By

from Test.PageObject.BasePage.Common import base_class
from Test.PageObject.Locators import Locator


class Registration(object):

    def __init__(self, driver):
        self.driver = driver
        # Defining the locators of Registration
        self.gender = driver.find_element(By.XPATH, Locator.gender)
        self.fName = driver.find_element(By.ID, Locator.fName)
        self.sName = driver.find_element(By.ID, Locator.sName)
        self.emailAdd = driver.find_element(By.ID, Locator.emailAdd)
        self.buisUsage = driver.find_element(By.ID, Locator.buisUsage)
        self.register = driver.find_element(By.XPATH, Locator.register)

    def setGender(self):
        self.gender.click()

    def setfName(self, Name):
        self.fName.clear()
        self.fName.click()
        self.fName.send_keys(Name)

    def setSname(self, secondName):
        self.sName.clear()
        self.sName.click()
        self.sName.send_keys(secondName)

    def setEmail(self, emailID):
        self.emailAdd.clear()
        self.emailAdd.click()
        self.emailAdd.send_keys(emailID)

    def setBuis(self):
        comobj1 = base_class(self.driver)
        self.buisUsage.click()
        buisVal = self.driver.find_elements(By.TAG_NAME, Locator.tagLi)
        for buisSelect in buisVal:
            if buisSelect.text == "Ihr Unternehmen":
                buisSelect.click()
                comobj1.wait_untilvanish(buisSelect)
                break

    def setRegister(self):
        self.sName.click()
        comobj2 = base_class(self.driver)
        comobj2.commonwait_until(Locator.register)
        self.register.click()
        sleep(2)
