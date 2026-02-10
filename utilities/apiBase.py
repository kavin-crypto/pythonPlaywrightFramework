from playwright.sync_api import Playwright

orderProduct = {"orders": [{"country": "India","productOrderedId": "68a961719320a140fe1ca57c"}]}

class ApiBase:

    def get_token(self, playwright: Playwright,UserCredentials):

        apiRequest = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = apiRequest.post("api/ecom/auth/login",
                        data= {"userEmail": UserCredentials["userEmailId"],
                               "userPassword": UserCredentials["Password"]})

        assert response.ok
        responseBody =  response.json()
        return responseBody["token"]


    def createOrder(self, playwright:Playwright,UserCredentials):
        token = self.get_token(playwright,UserCredentials)
        apiRequest = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = apiRequest.post(
            "api/ecom/order/create-order",
            data= orderProduct,
            headers = {
                "Authorization": token ,
                "Content-Type": "application/json",
            }
        )
        resp_order = response.json()
        return resp_order["orders"][0]


