from playwright.sync_api import expect


class OrderSummaryPage:

    def __init__(self,page):
        self.page = page

    def verifyOrderSummary(self,orderProduct):
        expect(self.page.locator(".tagline")).to_contain_text("Thank you")
        expect(self.page.locator(".col-text.-main")).to_have_text(orderProduct)