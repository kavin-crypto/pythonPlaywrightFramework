import json

from playwright.sync_api import Page

from pageObject.HomePage import HomePage
from pageObject.LoginPage import LoginPage
from pageObject.OrdersHistoryPage import OrdersHistoryPage
from utilities.networkRoutes import register_no_orders_route, register_unauthorized_order_details_route

with open("testdata/userCredentials.json") as f:
    test_data = json.load(f)
    user_credentials = test_data["UserCredentials"]
PRIMARY_USER = user_credentials[1]

def test_intercept(browser_invoke:Page):
    # data
    user = PRIMARY_USER
    page = browser_invoke
    register_no_orders_route(page)

    # page
    loginPage = LoginPage(browser_invoke)
    homePage = HomePage(browser_invoke)
    ordersHistoryPage = OrdersHistoryPage(browser_invoke)

    # test
    loginPage.login(user["userEmailId"], user["Password"])
    homePage.clickOrdersButton()
    ordersHistoryPage.verifyNoOrderMessage()

def test_unAuthApi(browser_invoke:Page):
    # data
    user = PRIMARY_USER
    page = browser_invoke
    register_unauthorized_order_details_route(page)

    # page
    loginPage = LoginPage(browser_invoke)
    homePage = HomePage(browser_invoke)
    ordersHistoryPage = OrdersHistoryPage(browser_invoke)

    # test
    loginPage.login(user["userEmailId"], user["Password"])
    homePage.clickOrdersButton()
    ordersHistoryPage.verifyUnauthorizedOrderAccessMessage()


