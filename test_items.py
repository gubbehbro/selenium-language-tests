import time
from selenium.webdriver.common.by import By

def test_add_to_cart_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Пауза 30 секунд для проверки языка, как требует задание
    time.sleep(30)
    
    # Ищем кнопку добавления в корзину
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    
    # Проверяем, что кнопка видна
    assert button.is_displayed(), "Кнопка добавления в корзину не найдена!"