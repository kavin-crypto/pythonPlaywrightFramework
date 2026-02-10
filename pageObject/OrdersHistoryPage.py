from playwright.sync_api import expect


class OrdersHistoryPage:

    def __init__(self,page):
        self.page = page

    def selectOrder(self,orderProduct):
        viewButton = self.page.locator("tr").filter(has_text=orderProduct)
        viewButton.get_by_role("button", name="View").click()

    def verifyNoOrderMessage(self):
        print(self.page.locator(".mt-4").text_content())

    def verifyUnauthorizedOrderAccessMessage(self):
        self.page.get_by_role("button", name="View").first.click()
        expect(self.page.locator(".blink_me")).to_have_text(
            "You are not authorize to view this order"
        )