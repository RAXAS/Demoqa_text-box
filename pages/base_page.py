from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, link) -> None:
        self.driver = driver
        self.link = link

    def open(self) -> None:
        self.driver.get(self.link)

    def element_is_visible(self, locator: tuple, timeout=5) -> None:
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator: tuple, timeout=5) -> None:
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

