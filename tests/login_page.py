class LoginPage:

    def __init__(self, page):
        self.page = page
        self.get_user_name_element = self.page.locator("[name='username2']")
        self.get_password_element = self.page.locator("[name='password2']")
        self.get_submit_element = self.page.locator("[id='submit']")

    def sign_in(self, user, password):
        self.get_user_name_element.fill(user)
        self.get_password_element.fill(password)
        self.get_submit_element.click()
