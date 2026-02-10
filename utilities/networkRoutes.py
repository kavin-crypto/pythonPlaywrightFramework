from playwright.sync_api import Page


# ---------- "No Orders" interception ----------

def intercept_no_orders(route):
    """
    Intercepts the 'get-orders-for-customer' API call and forces
    an empty orders response.
    """
    route.fulfill(
        status=200,
        json={"data": [], "message": "No Orders"},
    )


def register_no_orders_route(page: Page):
    """
    Registers the 'no orders' interception on the given page.
    """
    page.route(
        "https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",
        intercept_no_orders,
    )


# ---------- Unauthorized order details interception ----------

def intercept_unauthorized_order_details(route):
    """
    Forces the order details API to always return details for a fixed order
    that should not be visible to the current user.
    """
    route.continue_(
        url=(
            "https://rahulshettyacademy.com/api/ecom/order/"
            "get-orders-details?id=691e2dff5008f6a9092bcet5"
        )
    )


def register_unauthorized_order_details_route(page: Page):
    """
    Registers the unauthorized order details interception on the given page.
    """
    page.route(
        "**/api/ecom/order/get-orders-details?id=*",
        intercept_unauthorized_order_details,
    )
