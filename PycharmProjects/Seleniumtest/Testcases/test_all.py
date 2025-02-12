import pytest
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

from GenericUtility.POM.Loginpage import Loginpage
from configtest import *

# Test class using the fixture
@pytest.mark.usefixtures("Launchbrowser")
class Test1:

    def test1_Login(self,Launchbrowser):
        driver=Launchbrowser
        Login=Loginpage(driver)
        Login.performLogin("9876572689")
