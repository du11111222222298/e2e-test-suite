from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_invalid_login_shows_error(driver):
  """تست ورود با اطلاعات اشتباه و بررسی نمایش پیام خطا"""
  login_page = LoginPage(driver)
  login_page.load()
  login_page.login("locked_out_user", "wrong_password")

  error_text = login_page.get_error_text()
  assert (
      "Epic sadface" in error_text
  ), "پیام خطای مناسب برای ورود ناموفق نمایش داده نشد!"


def test_successful_login(driver):
  """تست ورود موفق به حساب کاربری"""
  login_page = LoginPage(driver)
  inventory_page = InventoryPage(driver)

  login_page.load()
  login_page.login("standard_user", "secret_sauce")

  assert (
      inventory_page.get_header_title() == "Products"
  ), "ورود به صفحه محصولات ناموفق بود!"


def test_add_product_to_cart_e2e(driver):
  """تست کامل فرآیند انتخاب محصول و بررسی سبد خرید (E2E)"""
  login_page = LoginPage(driver)
  inventory_page = InventoryPage(driver)

  # ۱. ورود به سایت
  login_page.load()
  login_page.login("standard_user", "secret_sauce")

  # ۲. افزودن کوله پشتی به سبد خرید
  inventory_page.add_backpack_to_cart()
  assert (
      inventory_page.get_cart_count() == "1"
  ), "تعداد محصولات سبد خرید به‌روز نشد!"

  # ۳. ورود به صفحه سبد خرید و بررسی نام محصول
  inventory_page.go_to_cart()
  assert (
      inventory_page.get_first_cart_item_name() == "Sauce Labs Backpack"
  ), "محصول انتخابی در سبد خرید یافت نشد!"