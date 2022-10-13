import pdb
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from lib.action import BasePage


class EventsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def send_keys(self, by, element, value):
        """
        Click on element locator and send the keys
        """
        keys = self.return_element_locator(by, element)
        keys.send_keys(value)

    def click_the_element(self, by, element):
        """
        Click on element locator
        """
        keys = self.return_element_locator(by, element)
        keys.click()

    def clear_the_element(self, by, element):
        """
        Clear the element locator
        """
        keys = self.return_element_locator(by, element)
        keys.clear()

    def element_is_displayed(self, by, element):
        """
        Verify the element is displayed or not
        """
        element = self.return_element_locator(by, element)
        result = element.is_displayed()
        return result

    def get_element_text(self, by, element):
        """
        Verify the element is send the text
        """
        keys = self.return_element_locator(by, element)
        result = keys.text
        return result

    def send_keys_with_clear(self, by, element, value):
        """
        It will send the keys with clear the element
        """
        keys = self.return_element_locator(by, element)
        keys.click()
        keys.clear()
        keys.send_keys(value)

    def click_and_send_keys(self, by, element, value):
        """
        Click on element locator and send the keys
        """
        keys = self.return_element_locator(by, element)
        keys.click()
        sleep(0.5)
        keys.send_keys(value)

    def move_to_find(self, by, element):
        """
        It will scroll to find the given element in the webpage
        """
        keys = self.return_element_locator(by, element)
        actions = ActionChains(self.driver)
        actions.move_to_element(keys).perform()

    def move_to_find_click(self, by, element):
        """
        It will scroll to find the given element in the page
         and click that element
        """
        keys = self.return_element_locator(by, element)
        actions = ActionChains(self.driver)
        actions.move_to_element(keys).perform()
        self.click_the_element(by, element)

    # def cancel_print_window(self):
    #     """
    #     To close the kot print window and kot copy
    #     """
    #     sleep(5)
    #     win_bef = self.driver.window_handles[0]
    #     win_aft = self.driver.window_handles[1]
    #     self.driver.switch_to_window(win_aft)
    #     shadow_root = self.driver.execute_script('return arguments[0].shadowRoot',
    #                                              self.driver.find_element_by_tag_name("print-preview-app"))
    #     root1 = shadow_root.find_element_by_css_selector('print-preview-sidebar')
    #     shadow_root1 = self.driver.execute_script('return arguments[0].shadowRoot', root1)
    #     try:
    #         root2 = shadow_root1.find_element_by_css_selector('print-preview-button-strip')
    #     except:
    #         root2 = shadow_root1.find_element_by_css_selector('print-preview-header')
    #     shadow_root2 = self.driver.execute_script('return arguments[0].shadowRoot', root2)
    #     cancel_button = shadow_root2.find_element_by_css_selector(".cancel-button")
    #     cancel_button.click()
    #     sleep(3)
    #     self.driver.switch_to_window(win_bef)

    def press_escape_key(self):
        """
        To press Escape button in keyboard keys
        """
        sleep(2)
        try:
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        except:
            self.driver.find_element_by_css_selector("html body").send_keys(Keys.ESCAPE)
        sleep(2)

    def press_enter_key(self):
        """
        To press Enter button keyboard keys
        """
        sleep(2)
        try:
            ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        except:
            self.driver.find_element_by_css_selector("html body").send_keys(Keys.ENTER)
        sleep(2)

    def press_home_key(self):
        """
        To press Home button in keyboard keys
        """
        sleep(2)
        self.driver.find_element_by_css_selector("html body").send_keys(Keys.HOME)
        sleep(2)

    def press_end_key(self):
        """
        To press END button keyboard keys
        """
        sleep(2)
        self.driver.find_element_by_css_selector("html body").send_keys(Keys.END)
        sleep(2)

    def press_page_down_key(self):
        """
        To press Page Down button in keyboard keys
        """
        sleep(2)
        self.driver.find_element_by_css_selector("html body").send_keys(Keys.PAGE_DOWN)
        sleep(2)

    def press_arrow_down_key(self):
        """
        To press Arrow Down button keyboard keys
        """
        sleep(2)
        self.driver.find_element_by_css_selector("html body").send_keys(Keys.ARROW_DOWN)
        sleep(2)

    def press_ctrl_shift_home_key(self):
        """
        To press CTRL + Shift + Home button keyboard keys
        """
        sleep(2)
        self.driver.find_element_by_css_selector(
            "html body").send_keys(Keys.CONTROL, Keys.SHIFT, Keys.HOME)
        sleep(2)

    def verify_element_is_available(self, by, element):
        """
        To check element available in DOM
        """
        elemnt = self.find_elements_in_dom(by, element)
        if elemnt:
            return True
        else:
            return False

    def choose_value_from_drop_down(self, by, element, value):
        """
        To choose given value from said drop down
        """
        el = self.return_element_locator(by=by, element=element)
        for option in el.find_elements_by_tag_name('option'):
            if option.text == value:
                option.click()
                break

    def define_sleep(self, time):
        """
        To make wait as user request
        """
        sleep(time)

    def check_element_enabled(self, by, element):
        """
         To return if the element is enabled or not
        """
        keys = self.return_element_locator(by, element)
        result = keys.is_enabled()
        assert result == True, "Element is not enabled"
