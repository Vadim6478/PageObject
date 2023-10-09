from selenium.common.exceptions import NoSuchElementException

class BasePage():

    def __init__(self, browser, url, timeout=10): # открываем браузер, с неявым ожидание который возвращаем нам True или False
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what): #метод is_element_present, в котором будем перехватывать исключение. В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор). 
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
