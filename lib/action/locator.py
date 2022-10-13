import pdb

from selenium.common.exceptions import \
    ElementNotVisibleException as ENVE, \
    ElementNotSelectableException as ENSE, \
    TimeoutException as TE, NoSuchElementException as NSEE, \
    StaleElementReferenceException as SERE, \
    ElementClickInterceptedException as ECIE
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def time_wait(self):
        """
        Wait the time given to click for the next element
        """
        wait = WebDriverWait(self.driver, 20, poll_frequency=3,
                             ignored_exceptions=[ENVE, NSEE,
                                                 ENSE, TE, ECIE])
        return wait

    def return_element_locator(self, by, element):
        """
        Basing on the type of element locator returns it
        """
        if by in "css":
            self.time_wait().until(EC.visibility_of_element_located
                                   ((By.CSS_SELECTOR, element)))
            element = self.driver.find_element(By.CSS_SELECTOR, element)
        elif by in "xpath":
            self.time_wait().until(EC.visibility_of_element_located
                                   ((By.XPATH, element)))
            element = self.driver.find_element(By.XPATH, element)
        elif by in "name":
            self.time_wait().until(EC.visibility_of_element_located
                                   ((By.NAME, element)))
            element = self.driver.find_element(By.NAME, element)
        elif by in "id":
            self.time_wait().until(EC.visibility_of_element_located
                                   ((By.ID, element)))
            element = self.driver.find_element(By.ID, element)
        elif by in "class":
            self.time_wait().until(EC.visibility_of_element_located
                                   ((By.CLASS_NAME, element)))
            element = self.driver.find_element(By.CLASS_NAME, element)
        return element

    def return_clickable_element_locator(self, by, element):
        """
        Basing on the type of element locator returns it
        """
        if by in "css":
            self.time_wait().until(EC.element_to_be_clickable
                                   ((By.CSS_SELECTOR, element)))
            element = self.driver.find_element(By.CSS_SELECTOR, element)
        elif by in "xpath":
            self.time_wait().until(EC.element_to_be_clickable
                                   ((By.XPATH, element)))
            element = self.driver.find_element(By.XPATH, element)
        elif by in "name":
            self.time_wait().until(EC.element_to_be_clickable
                                   ((By.NAME, element)))
            element = self.driver.find_element(By.NAME, element)
        elif by in "id":
            self.time_wait().until(EC.element_to_be_clickable
                                   ((By.ID, element)))
            element = self.driver.find_element(By.ID, element)
        elif by in "class":
            self.time_wait().until(EC.element_to_be_clickable
                                   ((By.CLASS_NAME, element)))
            element = self.driver.find_element(By.CLASS_NAME, element)
        return element

    def explicity_wait(self):
        """
        select existing address for delivery
        """
        wait = WebDriverWait(self.driver, 25, poll_frequency=5,
                             ignored_exceptions=[ENVE, NSEE,
                                                 ENSE, TE, SERE])
        return wait

    def return_found_element(self, by, element):
        """
        To click or tap on an element
        """
        return self.return_element_locator(by, element)

    def find_elements_in_dom(self, by, element):
        """
        To click or tap on an element
        """
        return self.verify_element_in_dom(by, element)

    def verify_element_in_dom(self, by, element):
        """
        Basing on the type of element locator returns it
        """
        if by in "id":
            element = self.driver.find_elements_by_id(element)
        if by in "css":
            element = self.driver.find_elements_by_css_selector(element)
        elif by in "xpath":
            element = self.driver.find_elements_by_xpath(element)
        elif by in "name":
            element = self.driver.find_elements_by_name(element)
        elif by in "tagname":
            element = self.driver.find_elements_by_tag_name(element)

        return element
