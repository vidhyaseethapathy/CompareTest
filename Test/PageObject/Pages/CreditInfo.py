from selenium.webdriver.common.by import By

from Test.PageObject.BasePage.Common import base_class
from Test.PageObject.Locators import Locator


class CreditIn(object):

    def __init__(self, driver):
        self.driver = driver
        # Defining the locators of CreditInfo
        self.money = driver.find_element(By.ID, Locator.money)
        self.purpose = driver.find_element(By.ID, Locator.purpose)
        self.time = driver.find_element(By.XPATH, Locator.time)
        self.continueButton = driver.find_element(By.XPATH, Locator.continueButton)

    def enter_money(self, moneyval):
        self.money.clear()
        self.money.click()
        self.money.send_keys(moneyval)

    def enter_usage(self):
        comobj1 = base_class(self.driver)
        self.purpose.click()
        purposeval = self.driver.find_elements(By.TAG_NAME, Locator.tagLi)
        for purposeSelect in purposeval:
            if purposeSelect.text == "Betriebsmittel":
                purposeSelect.click()
                comobj1.wait_untilvanish(purposeSelect)
                break

    def enter_runningtime(self):
        comobj1 = base_class(self.driver)
        comobj1.wait_untilvanish(Locator.tagLi)
        self.time.click()
        timeval = self.driver.find_elements(By.TAG_NAME, Locator.tagLi)
        for timeselect in timeval:
            if timeselect.text == "6 Monate":
                timeselect.click()
                comobj1.wait_untilvanish(timeselect)
                break

    def enter_continue(self):
        comobj = base_class(self.driver)
        comobj.wait_untilvanish(Locator.tagLi)
        self.continueButton.click()
