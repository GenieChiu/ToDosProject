import pytest
from selenium import webdriver
from pageObjects.TodosPage import TodosPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_todoCount_func:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/TaskData.xlsx"
    logger = LogGen.loggen()

    # Check the number of todo-count is displayed if more than one item is displayed on the todos list
    def test_05_todoCount(self, setup):
        self.logger.info("*************** Test_05_todoCount *****************")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)

        self.logger.info("****Started testing item displayed in todos list****")
        self.lp = TodosPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Doglist')
        actual_num = 0

        for r in range(2, self.rows+1):
            self.taskname = XLUtils.readData(self.path, 'Doglist', r, 1)

            self.lp.inputTask(self.taskname)
            self.lp.enterTask()
            time.sleep(2)

            # select 1 task as completed
            if r == 2:
              self.lp.selectTask()
              time.sleep(5)

        self.logger.info("****Started counting item ****")
        time.sleep(5)

        # Get the number of item left
        num = self.lp.countNum()

        # verify there is 9 item left
        if num == "9":
            self.logger.info("******* todoCount func test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* todoCount func  test failed **********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_05_todoCount.png")
            self.driver.close()
            assert False

    # Check the number of the item left is NOT displayed if no item is displayed on the todos list
    def test_06_todoCount(self, setup):
        self.logger.info("*************** Test_06_todoCount *****************")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)

        self.logger.info("****Started testing item displayed in todos list****")
        self.lp = TodosPage(self.driver)

        self.logger.info("****Started counting item ****")
        time.sleep(5)
        # Get the number of item left
        num = self.lp.countNum()

        # verify there is no item left
        if num == 0:
            self.logger.info("******* todoCount func test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* todoCount func  test failed **********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_06_todoCount.png")
            self.driver.close()
            assert False
