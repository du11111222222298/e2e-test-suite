from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
  URL = "https://www.saucedemo.com/"

  # آدرس المان‌های صفحه (Locators)
  USERNAME_INPUT = (By.ID, "user-name")
  PASSWORD_INPUT = (By.ID, "password")
  LOGIN_BUTTON = (By.ID, "login-button")
  ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

  def load(self):
    self.open_url(self.URL)

  def login(self, username, password):
    self.enter_text(self.USERNAME_INPUT, username)
    self.enter_text(self.PASSWORD_INPUT, password)
    self.click(self.LOGIN_BUTTON)

  def get_error_text(self):
    return self.get_text(self.ERROR_MESSAGE)