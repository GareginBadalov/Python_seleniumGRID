import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Remote(command_executor='http://192.168.1.50:4444/wd/hub',
                              desired_capabilities=DesiredCapabilities.CHROME)
    yield driver
    driver.quit()
