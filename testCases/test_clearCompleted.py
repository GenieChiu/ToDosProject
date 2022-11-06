import pytest
from selenium import webdriver
from pageObjects.TodosPage import TodosPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_ClearCompleted_func:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/TaskData.xlsx"
    logger = LogGen.loggen()

    #Check the "Clear completed" is displayed if more than one item is selected
    @pytest.mark.regression
    def test_07_clearCompleted(self, setup):
        self.logger.info("*************** Test_07_clearCompleted *****************")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)

        self.logger.info("****Started testing item displayed in todos list****")
        self.lp = TodosPage(self.driver)

        # input emty
        self.lp.inputTask("Dug Run")
        self.lp.enterTask()
        time.sleep(3)
        # select the task as completed
        self.lp.selectTask()
        time.sleep(5)


        self.logger.info("****Started more than one item is selected in todos list****")
        # check the "Clear completed" is existed
        actual_text = self.lp.checkClearCompleted()
        print(actual_text)

        # verify the "Clear completed" is existed
        if actual_text == 'Clear completed':
            self.logger.info("******* display clearCompleted func test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* display clearCompleted func test failed **********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_07_clearCompleted.png")
            self.driver.close()
            assert False

   # Check the "Clear completed" is NOT displayed if no item is selected
    @pytest.mark.regression
    def test_08_clearCompleted(self, setup):
        self.logger.info("*************** Test_07_clearCompleted *****************")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)

        self.logger.info("****Started testing item displayed in todos list****")
        self.lp = TodosPage(self.driver)

        # input emty
        self.lp.inputTask("Dug Run")
        self.lp.enterTask()
        time.sleep(3)

        self.logger.info("****No item is selected in todos list****")
        # check there is no "Clear completed" existed
        actual = self.lp.checkNoClearCompleted()

        # verify there is no "Clear completed" existed
        if actual:
            self.logger.info("******* display clearCompleted func test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* display clearCompleted func test failed **********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_08_clearCompleted.png")
            self.driver.close()
            assert False

