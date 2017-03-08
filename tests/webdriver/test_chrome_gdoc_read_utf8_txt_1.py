from lib.webdriverBaseTest import WebdriverBaseTest


class TestChromeGdocReadUTF8txt1(WebdriverBaseTest):

    def setUp(self):
        self.set_variable(test_target=self.env.TEST_TARGET_ID_1_PAGE_CONTENT_WITH_UTF8_TXT)
        super(TestChromeGdocReadUTF8txt1, self).setUp()

    def test_chrome_gdoc_read_utf8_txt_1(self):
        self.driver.get(self.test_url)
