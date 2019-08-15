from selenium.webdriver.common.by import By

from Test.PageObject.Locators import Locator


class CompanySelect(object):

    def __init__(self, driver):
        self.driver = driver
# Defining the locators of CompanySelection
        self.selectCompanyval= driver.find_element(By.ID, Locator.company)
        self.search= driver.find_element(By.XPATH, Locator.search)

    def getcompanyselection(self):
        self.selectCompanyval.clear()
        self.selectCompanyval.click()
        self.selectCompanyval.send_keys("FinCompare GmbH")
        self.search.click()
        company= self.driver.find_element(By.XPATH, Locator.selectCompany)
        company.click()
