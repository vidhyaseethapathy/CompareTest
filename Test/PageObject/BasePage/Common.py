from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class base_class(object):

    def __init__(self, driver):
        self.driver = driver

    # base class for wait function
    def wait_untilvanish(self, tage):

        try:
            WebDriverWait(self.driver, 1).until(ec.invisibility_of_element(tage))
            return True

        except:
            return False

    # Common wait function
    def commonwait_until(self, path):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, path)))
            return True

        except:
            return False

    def commonwait_untilvisible(self, path):
        try:
            WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, path)))
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, path)))
            return True

        except:
            return False
