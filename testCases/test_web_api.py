import json

import pytest
from playwright.sync_api import Playwright, expect

from pageObject.HomePage import HomePage
from pageObject.LoginPage import LoginPage
from pageObject.OrderSummaryPage import OrderSummaryPage
from pageObject.OrdersHistoryPage import OrdersHistoryPage
from utilities.apiBase import ApiBase


with open("testdata/userCredentials.json") as f:
    test_data = json.load(f)
    user_credentials = test_data["UserCredentials"]

# creating the order via API and verifying it placed successfully in Front End

@pytest.mark.parametrize("UserCredentials", user_credentials)
def test_placeOrderViaAPI(playwright:Playwright, UserCredentials, browser_invoke):
    #data
    userEmail = UserCredentials["userEmailId"]
    userPassword = UserCredentials["Password"]
    api = ApiBase()
    orderProduct = str(api.createOrder(playwright,UserCredentials))
    
    #page
    loginPage = LoginPage(browser_invoke)
    homePage = HomePage(browser_invoke)
    ordersHistoryPage = OrdersHistoryPage(browser_invoke)
    orderSummaryPage = OrderSummaryPage(browser_invoke)

    #test
    loginPage.login(userEmail,userPassword)
    homePage.clickOrdersButton()
    ordersHistoryPage.selectOrder(orderProduct)
    orderSummaryPage.verifyOrderSummary(orderProduct)
