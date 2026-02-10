class LoginPage:

    def __init__(self,page):
        self.page = page

    def login(self,username,password):
        self.page.locator("#userEmail").fill(username)
        self.page.get_by_placeholder("enter your passsword").fill(password)
        self.page.locator("#login").click()

