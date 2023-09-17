import pyautogui as pg


class HomeElementsLocators:  # Локаторы элементов на домашней странице профиля
    EXIT_BUTTON = [75, 537]  # Кнопка выхода из профиля
    HOME_PAGE = "./test/data/pics/home_page.png"  # Левое боковое меню


def locate_home_page():
    """ Проверка наличия и возвращение координат найденного меню """
    return pg.locateOnScreen(HomeElementsLocators.HOME_PAGE, 7)


def exit_the_profile():
    """ Выход из профиля и ожидание возвращения на экран авторизации """
    pg.click(HomeElementsLocators.EXIT_BUTTON)
    pg.sleep(7)
