import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        # открытие в Firefox страницы http://automationpractice.com/index.php
        driver.get("http://automationpractice.com/index.php")
        # ждем 3 секунды
        time.sleep(3)
        # #получение элемента страницы с id search_query_top, т.е поисковая строка)
        elem = driver.find_element_by_id("search_query_top")
        # ждем 3 секунды
        time.sleep(3)
        # набор слова blooseee в найденном элементе,которое не должно найти
        elem.send_keys("bloosee")
        # ждем 3 секунды
        time.sleep(3)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 3 секунды
        time.sleep(3)
        # проверка наличия строки "No results were found."
        # на странице с результатами поиска
        self.assertIn("No results were found for your search", driver.page_source)
        # ждем 3 секунды
        time.sleep(3)
        # получение элемента страницы с id search_query_top
        # на обновленной странице
        elem = driver.find_element_by_id("search_query_top")
        # очищаем строку поиска
        elem.clear()
        #ждем 3 секунды
        time.sleep(3)
        # набор слова blouse в найденном элементе
        elem.send_keys("blouse")
        # ждем 3 секунды
        time.sleep(3)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 3 секунды
        time.sleep(3)
        # проверка отсутствия строки "No results found."
        # на странице с результатами поиска
        self.assertNotIn("No results were found for your search", driver.page_source)
        # ждем 3 секунды
        time.sleep(3)
        # получение элемента страницы через css селектор)
        elems = driver.find_elements_by_css_selector('ul.product_list.grid > li .product-container .product-image-container .product_img_link')
        href_list = []
        for e in elems:
            href_list.append(e.get_attribute("href"))
        driver.get(href_list[0])
        # ждем 3 секунды
        time.sleep(3)
        elem = self.driver.find_element(By.NAME, "Submit")
        elem.click()
        time.sleep(3)
        elem = self.driver.find_element(By.CLASS_NAME, "continue")
        elem.click()
        time.sleep(3)

        elem = driver.find_element_by_id("search_query_top")
        # очищаем строку поиска
        elem.clear()
        # ждем 3 секунды
        time.sleep(3)
        # набор слова dress в найденном элементе
        elem.send_keys("dress")
        # ждем 3 секунды
        time.sleep(3)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 3 секунды
        time.sleep(3)
        # проверка отсутствия строки "No results found."
        # на странице с результатами поиска
        self.assertNotIn("No results were found for your search", driver.page_source)
        # ждем 3 секунды
        time.sleep(3)
        # получение элемента страницы через css селектор)
        elems = driver.find_elements_by_css_selector(
            'ul.product_list.grid > li .product-container .product-image-container .product_img_link')
        href_list = []
        for e in elems:
            href_list.append(e.get_attribute("href"))
        driver.get(href_list[1])
        # ждем 3 секунды
        time.sleep(3)
        elem = self.driver.find_element(By.ID, "wishlist_button")
        elem.click()
        time.sleep(3)
        # Ищем кнопку крестик, которая свернёт окно о том, что нужно зарегистрироваться, чтоб добавить в избранное
        elems = self.driver.find_elements(By.CLASS_NAME, 'fancybox-close')
        # Если кнопка найдена, то кликаем на неё
        if len(elems) != 0:
            elems[0].click()
        time.sleep(3)
        # получение элемента страницы через css селектор)
        elems = driver.find_elements_by_css_selector('.header_user_info .login')
        href_list = []
        for e in elems:
            href_list.append(e.get_attribute("href"))
        driver.get(href_list[0])
        # ждем 3 секунды
        time.sleep(3)

def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
