from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

class TodosPage:
    textbox_item_xpath = "//input[@placeholder='What needs to be done?']"
    item_xpath = "//div[@class='view']"
    item_toggle_xpath = "//input[@class='toggle']"
    item_destroy_btn_xpath = "//button[@class='destroy']"
    todo_count_xpath = "//span[@class='todo-count']"
    todo_num_css = "span[class='todo-count'] strong"
    clear_completed_btn_class = "clear-completed"


    def __init__(self, driver):
        self.driver = driver

    def inputTask(self, taskname):
        self.driver.find_element(By.XPATH, self.textbox_item_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_item_xpath).send_keys(taskname)

    def enterTask(self):
        self.driver.find_element(By.XPATH, self.textbox_item_xpath).send_keys(Keys.ENTER)

    def checkNoTask(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(By.XPATH, "//div[@class='view']"))
            not_found = False
        except:
            not_found = True

        return not_found

    def selectTask(self):
        self.driver.find_element(By.XPATH, self.item_toggle_xpath).click()

    def deleteTask(self):
        elem = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.item_destroy_btn_xpath)))
        self.driver.execute_script("arguments[0].click();", elem)


    def clickTask(self):
        try:
          source= WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='view'] label")))
          action = ActionChains(self.driver)
          action.double_click(source).perform()
          found = True
        except:
          found = False

        return found

    def countNum(self):
        try:
           num = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class='todo-count'] strong"))).text
        except:
            num = 0

        return num

    def checkNoClearCompleted(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "clear-completed")))
            not_found = False
        except:
            not_found = True

        return not_found

    def checkClearCompleted(self):
        elem = self.driver.find_element(By.CLASS_NAME, "clear-completed")
        text = elem.get_attribute('innerText')
        return text

