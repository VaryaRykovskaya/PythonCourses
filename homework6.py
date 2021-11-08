import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Chrome()

    def test_login_logout(self):
        driver = self.driver
        # открытие в Chrome страницы http://www.python.org/psf-landing/
        # на которой есть кнопка Sign In
        driver.get("https://www.python.org/psf-landing/")
        # ждем 5 секунд
        time.sleep(2)
        # поиск ссылки с текстом "Sign In"
        elem = driver.find_element_by_link_text("Sign In")
        # нажатие на ссылку
        elem.click()
        # ждем 5 секунд
        time.sleep(2)
        # поиск текстового поля для ввода логина по XPath
        # (тег input с name='login')
        elem = driver.find_element_by_xpath("//input[@name='login']")
        # ввод логина
        elem.send_keys("Barbara_R")
        # ждем 5 секунд
        time.sleep(2)
        # поиск текстового поля для ввода пароля по XPath
        # (тег input с name='password')
        elem = driver.find_element_by_xpath("//input[@name='password']")
        # ввод логина
        elem.send_keys("chupakabra11")
        # ждем 5 секунд
        time.sleep(2)
        # жмем ввод для отправки формы
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(2)
        # проверка наличия на странице строки "Your account"
        # после входа
        self.assertIn("Your account", driver.page_source)
        # ждем 5 секунд
        time.sleep(2)
        # вывод кода страницы для отладки, потом можно будет убрать
        print(driver.page_source)

        # поиск ссылки с текстом "password change"
        driver.get("https://www.python.org/accounts/password/change/")
        # ждем 2 секунд
        time.sleep(2)
        # поиск текстового поля для ввода пароля по XPath
        # (тег input с name='oldpassword')
        elem = driver.find_element_by_xpath("//input[@name='oldpassword']")
        # ввод password
        elem.send_keys("chupakabra11")
        # ждем 2 секунд
        time.sleep(2)
        # поиск текстового поля для ввода логина по XPath
        # (тег input с name='password1')
        elem = driver.find_element_by_xpath("//input[@name='password1']")
        # ввод password
        elem.send_keys("chupakabra1")
        # ждем 5 секунд
        time.sleep(2)
        # поиск текстового поля для ввода логина по XPath
        # (тег input с name='password2')
        elem = driver.find_element_by_xpath("//input[@name='password2']")
        # ввод password
        elem.send_keys("chupakabra1")
        # ждем 5 секунд
        time.sleep(2)
        # жмем ввод для отправки формы
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(2)


    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
