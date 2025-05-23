from selenium.webdriver.common.by import By

def test_add_to_basket_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button_add_to_basket = browser.find_element(By.XPATH, "//button[@value='Add to basket']")
    assert button_add_to_basket, "Кнопка добавления в корзину не найдена"
