import pytest
from selenium import webdriver
from pageObjects.TodosPage import TodosPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_display_func:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/TaskData.xlsx"
    logger = LogGen.loggen()

    # Check the item displayed in todos list while typying the text in the input field and enter it
    @pytest.mark.regression
    def test_01_display(self, setup):
        self.logger.info("*************** Test_01_display *****************")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)

        self.logger.info("****Started testing item displayed in todos list****")
        self.lp = TodosPage(self.driver)

        # data input from the excel sheet
        self.rows = XLUtils.getRowCount(self.path, 'Doglist')
        # set the actual number and expected number
        expect_num = self.rows - 1
        actual_num = 0
        print(expect_num)

        for r in range(2, self.rows+1):
            self.taskname = XLUtils.readData(self.path, 'Doglist', r, 1)

            self.lp.inputTask(self.taskname)
            self.lp.enterTask()
            time.sleep(2)
            actual_num = actual_num + 1
            print(actual_num)

        # verify actual number and expected number are same
        if actual_num == expect_num:
            self.logger.info("******* display func test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* display func  test failed **********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_01_display.png")
            self.driver.close()
            assert False




    # Check the item is NOT displayed in todos list while typying No text in the input field and enter it
    @pytest.mark.regression
    def test_02_display(self, setup):
        self.logger.info("*************** Test_02_display *****************")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)

        self.logger.info("****Started testing item displayed in todos list****")
        self.lp = TodosPage(self.driver)

        # input emty string
        self.lp.inputTask(" ")
        self.lp.enterTask()
        time.sleep(2)

        # check there is no task
        actual = self.lp.checkNoTask()

        # verify there is no task
        if actual:
            self.logger.info("******* display func test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* display func test failed **********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_02_display.png")
            self.driver.close()
            assert False

