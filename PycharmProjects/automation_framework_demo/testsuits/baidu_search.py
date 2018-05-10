#_*_ coding:utf-8_*_

import time
import unittest

from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.baidu_homepage import HomePage

class BaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_search(self):
        homepage =HomePage(self.driver)
        homepage.type_search('selenium')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_window_img()

        try:
            assert 'selenium' in homepage.get_page_title()
            print("test pass")
        except Exception as e:
            print("test fail",format(e))

    def test_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search('python')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_window_img()

if __name__ =='__main__':
    unittest.main()