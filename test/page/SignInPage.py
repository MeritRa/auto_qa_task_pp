import pyautogui as pg
import pygetwindow as gw
from test.settings import TITLE


class AppSighInElementsLocators:  # Локаторы элементов на экране авторизации
    REGISTRATION_BUTTON = [765, 323]  # Кнопка перехода на экран регистрации
    EMAIL_FIELD = [547, 408]  # Поле ввода email
    PASSWORD_FIELD = [562, 505]  # Поле ввода пароля
    HIDE_PASSWORD_BUTTON = [784, 503]  # Кнопка сокрытия пароля
    SIGN_IN_BUTTON = [631, 600]  # Кнопка входа
    SIGN_IN_BY_GOOGLE_BUTTON = [593, 715]  # Кнопка входа через Google
    SIGN_IN_BY_VK_BUTTON = [677, 715]  # Кнопка входа через Вконтакте
    FORGOT_PASSWORD_BUTTON = [604, 767]  # Кнопка "Забыли пароль?"


def focus_on_the_app():
    """ Фокусировка на экране приложения """
    app = gw.getWindowsWithTitle(TITLE)[0]
    app.activate()


def enter_email(email):
    """ Выбор поля email, отчистка и ввод данных """
    pg.moveTo(AppSighInElementsLocators.EMAIL_FIELD)
    pg.click()
    pg.hotkey("ctrl", "a")
    pg.press("backspace")
    pg.typewrite(email)


def enter_password(password):
    """ Выбор поля пароля, отчистка и ввод данных """
    pg.moveTo(AppSighInElementsLocators.PASSWORD_FIELD)
    pg.click()
    pg.hotkey("ctrl", "a")
    pg.press("backspace")
    pg.typewrite(password)


def send_info(result):
    """ Отправка формы авторизации и поиск ожидаемого результата """
    pg.moveTo(AppSighInElementsLocators.SIGN_IN_BUTTON)
    pg.click()
    return pg.locateOnScreen(result, 7)


def switch_to_registation():
    """ Переключение на экран регистрации """
    pg.moveTo(AppSighInElementsLocators.REGISTRATION_BUTTON)
    pg.click()


def google_sigh_up():
    """ Выбор входа через Google """
    pg.moveTo(AppSighInElementsLocators.SIGN_IN_BY_GOOGLE_BUTTON)
    pg.click()


def vk_sigh_up():
    """ Выбор входа через Vkontakte """
    pg.moveTo(AppSighInElementsLocators.SIGN_IN_BY_VK_BUTTON)
    pg.click()


def forgot_password():
    """ Переход на экран восстановления пароля """
    pg.moveTo(AppSighInElementsLocators.FORGOT_PASSWORD_BUTTON)
    pg.click()
