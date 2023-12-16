
import testcases
import unittest
import data
from selenium import webdriver


class TestYourWebApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://test.in99s.com/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_new(self):
        print(len(data.dish))
        for i in range(0,1001,1):
            testcases.test_create_new_dish(self,i)

    def test_remove(self):
        testcases.test_delete_dish(self)



if __name__ == "__main__":
    unittest.main()
