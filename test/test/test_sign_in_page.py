import pyautogui as pg
import pytest
import allure
from test.page import SignInPage as auth
from test.data import SignInDataHelper as data
from test.page import HomePage as home

pg.FAILSAFE = False


@allure.suite('Planoplan App')
@allure.sub_suite('Sign-In Tests')
@allure.title('Sigh-In in the app')
@pytest.mark.parametrize("email, password, result", data.get_data_for_manual_auth())
def test_sign_in_function_valid(app_set_up, email, password, result):
    """ Тесты на авторизацию через экран приложения - валидный запрос, отсуствие одного или двух полей, невалидные данные
    Количество: 8 """
    auth.enter_email(email)  # Ввод почты
    auth.enter_password(password)  # Ввод пароля
    answer = auth.send_info(result)  # Отправка формы и запрос ожидаемого результата
    assert answer is not None  # Проверка наличия ожидаемого результата
    home_page = home.locate_home_page()  # Проверка успешности авторизации
    if home_page is not None:
        home.exit_the_profile()  # Если авторизация успешна: выход из профиля перед следующей проверкой
