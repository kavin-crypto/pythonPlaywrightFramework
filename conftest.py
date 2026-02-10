import json
from pathlib import Path

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="browser to use",
    )

@pytest.fixture()
def browser_invoke(playwright, request):

    browser_name = request.config.getoption("browser_name")
    if browser_name =="chrome":
        browser = playwright.chromium.launch(headless=False) # opening a browser engine
    elif browser_name =="firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context() #to create a new temporary browsing session
    page = context.new_page() #opening a tab
    page.goto("https://rahulshettyacademy.com/client")
    yield page
    context.close()
    browser.close()


