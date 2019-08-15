

from Test.PageObject.Locators import Locator
from selenium import webdriver
from selenium.webdriver.common.by import By


class Home(object):

    def __init__(self, driver):
        self.driver = driver
    #Defining the locators of HomePage
        self.kredit= driver.find_element(By.XPATH, Locator.kredit)
    def click_Kredit(self):
        self.kredit.click()



