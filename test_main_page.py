from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(driver, link)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    main_page.open()                      # открываем страницу
    main_page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    main_page.should_be_login_link()      # выполняем метод проверки— проверяем логин линк
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()







#def test_guest_can_go_to_login_page(driver):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(driver, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()                      # открываем страницу
#    page.should_be_login_link()  
#    page.should_be_login_url()
#    page.should_be_login_form()
#    page.should_be_register_form()
#    #driver.get(link)
#    #login_link = driver.find_element("css selector", "#login_link")
#    #login_link.click()
