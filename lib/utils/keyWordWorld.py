import os
import pdb
from time import sleep

import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options as chrmOption
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as ffOption
from selenium.webdriver.ie.options import Options as ieOption
from selenium.webdriver.edge.options import Options as edgeOption
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

from lib.action import EventsPage
from selenium import webdriver


class Key_Word_World(EventsPage):

    def open_browser(self, path, val):
        """To Launch the browser"""
        if val == "firefox" or val == "fire fox":
            try:
                options = ffOption()
                # options.add_argument("--headless")
                dr = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
            except:
                os.environ["HTTP_PROXY"] = "http://172.24.175.125:9090/"
                os.environ["HTTPS_PROXY"] = "http://172.24.175.125:9090/"
                dr = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
        elif val == "ie":
            ie_options = ieOption()
            ie_options.ignore_protected_mode_settings = True
            dr = webdriver.Ie(options=ie_options, executable_path=path)
        elif val == "edge":
            options = edgeOption()
            # options.add_argument("headless")
            dr = webdriver.Edge(options=options, executable_path=path)
        else:
            # chromedriver_autoinstaller.install()
            # Check if the current version of chromedriver exists
            # and if it doesn't exist, download it automatically,
            # then add chromedriver to path
            try:
                options = chrmOption()
                options.add_argument("--start-maximized")
                # options.add_argument("--headless")  # Runs Chrome in headless mode.
                dr = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
            except:
                os.environ["HTTP_PROXY"] = "http://172.24.175.125:9090/"
                os.environ["HTTPS_PROXY"] = "http://172.24.175.125:9090/"
                dr = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())

        dr.maximize_window()

        self.driver = dr

    def kill_browser(self):
        """To close the browser"""
        self.driver.quit()

    def load_url(self, url):
        """To load the given url"""
        self.driver.get(url)

    def save_snap_shot(self, path):
        """To save the screen shot in the said path"""
        self.driver.save_screenshot(path)

    def enter_text(self, by, ele, value):
        """To enter the given value in the said element"""
        self.send_keys_with_clear(by, ele, value)

    def click_on_element(self, by, ele):
        """To click on the said element"""
        self.click_the_element(by, ele)

    def verify_value_true(self, by, ele, val):
        """To verify whether given data is present in the element"""
        result = self.get_element_text(by, ele)
        assert val in result, "Value/ Data mismatch - required is " + val + " data/ value available is " + result

    def verify_value_false(self, by, ele, val):
        """To verify whether given data is not present in the element"""
        sleep(5)
        result = self.get_element_text(by, ele)
        assert val != result, "Value/ Data matches - required is " + val + " data/ value available is " + result

