import pytest
from selenium import webdriver

# creating conftest.py file to help reduce duplication, logging, screenshot etc. stay tune
# specified the location where the chrome driver is located
@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    # to supress the error messages/logs
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, executable_path='C:/Users/tzuning.chiu/PycharmProjects/ToDosProject/utilities/chromedriver.exe')
    return driver


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'ToDos list'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Genie'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)