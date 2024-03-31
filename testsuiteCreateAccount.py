import pytest
from base_test_class import BaseTestCase, BaseCase
import json
from parameterized import parameterized, parameterized_class
BaseCase.main(__name__, __file__)

class TestSuiteCreateAccount(BaseTestCase):
    def _loadConfig(self):
        configFile = open("testsuite2.json", encoding="utf8")
        self.config = json.load(configFile)
        setattr(self, "domain", self.config["domain"])
        setattr(self, "domainAdmin", self.config["domainAdmin"])
        setattr(self, "adminAccount", self.config["adminAccount"])
        setattr(self, "adminPassword", self.config["adminPassword"])
        testcase_dict = {obj["Testcase"]: obj for obj in self.config["testcase"]}
        setattr(self, "testcase_dict", testcase_dict)
        
    
    def setUp(self):
        super().setUp()
        self._loadConfig()

    @parameterized.expand(range(1, 31))
    def test_create_account_and_validate(self, testcase):
        self._createAccount(testcase)
        self._validate(testcase)
        
    @parameterized.expand(range(30, 34))
    def test_create_account_and_validate_success(self, testcase):
        self._createAccount(testcase)
        self._validate(testcase)
        self._deleteAccount()
    
    def _deleteAccount(self):
        self.get(self.domainAdmin)
        self.wait(1)
        self.type("//input[@id='UserName']", self.adminAccount)
        self.type("//input[@id='Password']", self.adminPassword)
        self.click("//button[contains(text(), 'Sign In')]")
        self.wait(1)
        self.click("//a[@href='/admin/account' and @class='nav-link']")
        print(f"//a[@href='#' and @data-user='{self.username}']")
        self.click(f"//a[@href='#' and @data-user='{self.username}']", f"//a[@href='#' and @data-user='{self.username}']")
        # self.wait(10)

    def _createAccount(self, testcase):
        self._prepareParams(testcase)
        self.open(self.domain)
        self.wait(1)
        self.click("//i[@class='fa fa-user']")
        self.wait_for_text("My Account")
        self.hover_and_click("//li[@class='account']","//a[contains(text(), 'Register')]")
        self.wait(1)
        self.type("//input[@id='Email']", self.testcase_dict[testcase]["Username"])
        self.type("//input[@id='Password']", self.testcase_dict[testcase]["Password"])
        self.type("//input[@id='ConfirmPassword']", self.testcase_dict[testcase]["RePassword"])
        self.wait(1)
        self.scroll_to_top()
        self.wait(1)
        self.click("//input[@value='Register' and @type='submit']")
        self.scroll_to_top()

    def _prepareParams(self, testcase):
        self.username = self.testcase_dict[testcase]["Username"]
        self.password = self.testcase_dict[testcase]["Password"]
        self.repassword = self.testcase_dict[testcase]["RePassword"]
        self.set_testcase_visible_elements(self.testcase_dict[testcase]['ExpectResult'])

    def _validate(self,testcase):
        for text in self.testcase_dict[testcase]['ExpectResult']:
            self.wait_for_texts_visible(text)