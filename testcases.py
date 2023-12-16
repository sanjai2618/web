
from selenium.webdriver.common.by import By
import time
import data
import random

def test_create_new_dish(self,i):
    self.driver.execute_script("window.scrollBy(0,500)")
    time.sleep(5)
    self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/textarea[1]").send_keys(data.dish[i])
    self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/textarea[1]").send_keys(random.choice(data.description))
    self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys(random.choice(data.availability))
    self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys(random.randint(a=1,b=100))
    self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[5]/div[2]/button[3]/img[1]").click()
    time.sleep(5)


def test_delete_dish(self):
    self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/button[1]/img[1]").click()
    time.sleep(5)
