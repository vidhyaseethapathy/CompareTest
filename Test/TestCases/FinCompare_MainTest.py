import unittest

from selenium import webdriver

from Test.PageObject.Pages.CompanySelection import CompanySelect
from Test.PageObject.Pages.CreditInfo import CreditIn
from Test.PageObject.Pages.HomePage import Home
from Test.PageObject.Pages.Registration import Registration


class MainTest(unittest.TestCase):

    # Function to start the browser
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("Path To/chromedriver.exe")
        print("Chrome browser initiated")
        print("------------------------------")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://app.fincompare.de/wizard")

    # Function to do the registration process
    def test_reg(self):
        driver = self.driver
        homeobj = Home(driver)
        homeobj.click_Kredit()
        crobj = CreditIn(driver)
        crobj.enter_money("1000")
        crobj.enter_usage()
        crobj.enter_runningtime()
        crobj.enter_continue()
        compobj = CompanySelect(driver)
        compobj.getcompanyselection()
        regobj = Registration(driver)
        regobj.setGender()
        regobj.setfName("Vidhya")
        regobj.setSname("Seethapathy")
        regobj.setEmail("vidhyaseethapathy92@gmail.com")
        regobj.setBuis()
        regobj.setRegister()

        direc="TestResult.png"
        self.driver.get_screenshot_as_file(direc)

    # Function to close and quit the browser
    @classmethod
    def tearDownClass(cls):
        print("Quit the browser")
        cls.driver.close()
        cls.driver.quit()
        print('Test successfully completed')
