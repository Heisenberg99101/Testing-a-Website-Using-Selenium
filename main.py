import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")

# functions starting with 'test' will be run first.
# First setUp is run, then test_example, then teardown and then again setUp is run, then test_example2, then teardown.
    # def test_example(self):
    #     print("Test")
    #     assert False
    # def test_example_2(self):
    #     assert True
# Ran 2 tests in 9.807s. FAILED (failures=1)

    def test_search_python(self):

        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        #Load the main page. In this case the home page of Python.org
        mainPage = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        assert mainPage.is_title_matches(), ""
        #Sets the text of search textbox to "pycon"
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()