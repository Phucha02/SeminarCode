import time
from base_test_class import BaseTestCase, BaseCase
import json
BaseCase.main(__name__, __file__)

class WebTest(BaseTestCase):
    def _loadConfig(self):
        configFile = open("settings.json", encoding="utf8")
        self.config = json.load(configFile)
        setattr(self, "domain", self.config["domain"])
        setattr(self, "domainAdmin", self.config["domainAdmin"])
        setattr(self, "adminAccount", self.config["adminAccount"])
        setattr(self, "adminPassword", self.config["adminPassword"])
        
    
    def setUp(self):
        super().setUp()
        self._loadConfig()
    
    def test_1_login_function_failed_email_empty(self, testcase = 1):
        self._login_test(testcase)
        self._logout_user()
        
    def test_2_login_function_failed_email_invalid(self, testcase = 2):
        self._login_test(testcase)
        
    def test_3_login_function_failed_password_empty(self, testcase = 3):
        self._login_test(testcase)
        
    def test_4_login_function_failed_password_incorrect(self, testcase = 4):
        self._login_test(testcase)

    def test_5_login_function_failed_account_not_existed(self, testcase = 5):
        self._login_test(testcase)

    def test_6_login_function_failed_password_length_101(self, testcase = 6):
        self._login_test(testcase)
    
    def test_7_login_function_success_combine_valid_password_email_lenght_6(self, testcase = 7):
        self._login_test(testcase)
        self._logout_user()

    def test_8_login_function_success_combine_valid_password_email_lenght_7(self, testcase = 8):
        self._login_test(testcase)
        self._logout_user()

    def test_9_login_function_success_combine_valid_password_email_length_99(self, testcase = 9):
        self._login_test(testcase)

    def test_10_login_function_success_combine_valid_password_email_length_100(self, testcase= 10):
        self._login_test(testcase)

    def _createAccount(self, testcase):
        self._prepareParams(testcase)
        self.open(self.domain)
        self.wait(1)
        self.click("//i[@class='fa fa-user']")
        self.wait_for_text("My Account")
        self.hover_and_click("//li[@class='account']","//a[contains(text(), 'Register')]")
        self.wait(1)
        self.type("//input[@id='Email']", self.username)
        self.type("//input[@id='Password']", self.password)
        self.type("//input[@id='ConfirmPassword']", self.repassword)
        self.click("//input[@value='Register' and @type='submit']")
        # self.wait(5)

    def _deleteAccount(self, testcase):
        self.open(self.domainAdmin)
        self.wait(1)
        self.type("//input[@id='UserName']", self.adminAccount)
        self.type("//input[@id='Password']", self.adminPassword)
        self.click("//button[contains(text(), 'Sign In')]")
        # self.is_element_clickable
        
    def _login_test(self, testcase):
        self._prepareParams(test_case_number= testcase)
        self._login_user()
        self._validate()

    def _prepareParams(self, test_case_number):
        self.test_case_process = "testcase" + str(test_case_number)
        self.test_case_infor = self.config[f"testcase{test_case_number}"]
        self.set_properties_profile(self.test_case_infor['userProfile'])
        self.set_testcase_visible_elements(self.test_case_infor['visible'])    
        self.set_testcase_absent_elements(self.test_case_infor['notVisible'])

    def _logout_user(self):
        self.hover_and_click("//li[@class='account']", "/html/body/div/header/div[1]/div/div/div[2]/div/ul/li[3]/ul/li[2]/a", timeout= 10)

    def _login_user(self):
        self.open(self.domain)
        self.wait(1)
        self.click("//i[@class='fa fa-user']")
        self.wait_for_text("My Account")
        self.hover_and_click("//li[@class='account']","//ul[@class='account_selection']//li//a[contains(@href,'/account/login')]")
        self.wait(1)
        self.type("//input[@id='UserName']", self.username)
        self.wait(1)
        self.type("//input[@id='Password']", self.password)
        self.click("//input[@type='submit']")
        self.scroll_to_top()
    # def test_tinh_nang_chua_login(self):
    #     self.prepareParams(2)
    #     self.open(self.domain)
    #     self.wait(3)
    #     self.wait_for_element_not_visible('//span[contains(text(), '')]')

    