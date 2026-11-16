from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
  # آدرس المان‌های صفحه محصولات (Locators)
  PAGE_TITLE = (By.CLASS_NAME, "title")
  ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
  CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
  CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
  CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

  def get_header_title(self):
    return self.get_text(self.PAGE_TITLE)

  def add_backpack_to_cart(self):
    self.click(self.ADD_BACKPACK_BTN)

  def get_cart_count(self):
    return self.get_text(self.CART_BADGE)

  def go_to_cart(self):
    self.click(self.CART_LINK)

  def get_first_cart_item_name(self):
    return self.get_text(self.CART_ITEM_NAME)