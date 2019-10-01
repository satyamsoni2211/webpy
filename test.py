from Webpy import Webpy
import unittest
wb = Webpy()
driver = wb.driver


class abc(unittest.TestCase):
    def setUp(self):
        driver.get('http://realpython.com')
        self.elem = driver.find_element_by_name('q')

    def test_abc(self):
        '''
            test to check for the tagname
        '''
        self.assertEqual(self.elem.tag_name, 'input', 'not equal')


if __name__ == '__main__':
    wb.run(abc)
