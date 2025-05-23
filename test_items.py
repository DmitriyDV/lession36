from selenium.webdriver.common.by import By

def test_add_to_basket_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(3)
    button_add_to_basket = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button_add_to_basket, "Кнопка добавления в корзину не найдена"
