import datetime
from pathlib import Path  # Corrected path usage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Fixture to initialize the WebDriver for the tests
@pytest.fixture
def Launchbrowser():
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Maximize the window and set implicit wait
    driver.maximize_window()
    driver.implicitly_wait(5)

    # Open the URL
    driver.get("https://allensolly.abfrl.in/")

    # Yield the driver to be used in the tests
    yield driver

    # Cleanup: quit the browser after all tests are done
    driver.quit()

import datetime
from pathlib import Path
import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Get today's date and time for unique reports
    today = datetime.datetime.now().strftime("%Y%m%d%H%M")

    # Define the reports directory (Corrected Windows path handling)
    reports_dir = Path(r"C:\Users\User\PycharmProjects\Seleniumtest\Reports") / today  # Using raw string (r"...")

    # Create the directory if it doesn't exist
    reports_dir.mkdir(parents=True, exist_ok=True)

    # Set the HTML report path dynamically
    config.option.htmlpath = str(reports_dir / "report.html")

# Set the title of the pytest-html report
def pytest_html_report_title(report):
    report.title = "Automation Results"
