class MainPageLocators():
    LOGIN_LINK = ("css selector", "#login_link")

class LoginPageLocators():
    
    LOGIN_FORM = ("css selector" , "#login_form")
    REGISTER_FORM = ("css selector" , "#register_form")
    
    EMAIL_INPUT = ("css celector", "#id_login-username")
    PASS_INPUT = ("css selector", "#id_login-password")
    BATTON_LOG_IN = ("css selector" , "button[value='Log In']")

    EMAIL_REG_INPUT = ("css selector" , "#id_registration-email")
    PASS_REG1 = ("css selector" , "#id_registration-password1")
    PASS_REG2 = ("css selector" , "#id_registration-password2")
    BUTTON_REG = ("css selector" , "button[value='Register']")