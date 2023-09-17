import subprocess
import pytest
import pyautogui as pg
from test.settings import APP_PATH


@pytest.fixture(scope="session")
def app_set_up():
    """ Запуск и отключение приложения для тестирования """
    # Запуск приложения, используя путь в .env
    app = subprocess.Popen([APP_PATH])
    pg.sleep(10)  # Ожидание успешного запуска приложения

    pg.PAUSE = 1  # Настройка паузы между шагами тестирования в 1 секунду

    yield  # Процесс тестирования

    # Отключение приложения после тестирования
    app.terminate()
