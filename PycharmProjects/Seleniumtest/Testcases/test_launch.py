import pytest
from configtest import *

@pytest.mark.regression
@pytest.mark.parametrize("name,id",[("Ram",123),("Raman",145)])
@pytest.mark.usefixtures("Launchbrowser")
def test_regression_feature(name,id):
    print(name,id)


@pytest.mark.smoke
def test_regression_feature1():
    print("hello1")

