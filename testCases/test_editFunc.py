import pytest
from selenium import webdriver
from pageObjects.TodosPage import TodosPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_edit_func:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    # Check the item is editable by double-clicking on the text field
    @pytest.mark.regression
    def test_03_edit(self, setup):
        self.logger.info("*************** Test_03_edit *****************")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)

        self.logger.info("****Started testing item displayed in todos list****")
        self.lp = TodosPage(self.driver)

        # input one task
        self.lp.inputTask("work")
        self.lp.enterTask()
        time.sleep(2)
        # try to edit the item
        act = self.lp.clickTask()

        # verify the item is editable
        if act:
            self.logger.info("******* edit func test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* edit func test failed **********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_03_edit.png")
            self.driver.close()
            assert False


    # Check the item is NOT editable by clicking on the wrong field
    @pytest.mark.regression
    def test_04_edit(self, setup):
        self.logger.info("*************** Test_04_edit *****************")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)

        self.logger.info("****Started testing item displayed in todos list****")
        self.lp = TodosPage(self.driver)

        # input one task
        self.lp.inputTask("work")
        self.lp.enterTask()
        time.sleep(2)
        # delete the item
        self.lp.deleteTask()
        time.sleep(2)
        # try to edit the item
        act = self.lp.clickTask()

        # verify the item is not editable
        if act:
            self.logger.info("******* edit func test failed **********")
            self.driver.close()
            assert False
        else:
            self.logger.error("******* edit func test passed **********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_04_edit.png")
            self.driver.close()
            assert True