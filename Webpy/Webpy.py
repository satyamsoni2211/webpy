import os
import sys
import unittest
from ._config import CONF_DIR
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class Webpy:

    def __init__(self):
        # sys.path.append()
        self.__opts = Options()
        # self.__opts.set_headless()
        self.__path = os.path.join(
            CONF_DIR, 'drivers', 'chromedriver')
        self.__driver = Chrome(self.__path, chrome_options=self.__opts)

    @property
    def driver(self):
        return self.__driver

    def run(self, cls):
        self.__suite = unittest.TestSuite()
        self.__runner = unittest.TextTestRunner(verbosity=2)
        self.__suite.addTests(
            unittest.defaultTestLoader.loadTestsFromTestCase(cls))
        self.__runner.run(self.__suite)

    def __del__(self):
        self.__driver.close()
