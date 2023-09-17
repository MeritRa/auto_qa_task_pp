from faker import Faker
from test.settings import EMAIL, PASS

fake = Faker()


def get_data_for_manual_auth():
    """ Получение тестовых данных для входа в систему с помощью ввода email/password напрямую в приложении """
    return test_data


test_data = [(EMAIL, PASS, "./test/data/pics/home_page.png"),  # Валидные email +  пароль
             (EMAIL, "", "./test/data/pics/empty_field_error.png"),  # Валидный email без пароля
             ("", PASS, "./test/data/pics/empty_field_error.png"),  # Валидный пароль без email'а
             ("", "", "./test/data/pics/empty_field_error.png"),  # Пустые поля
             (f"{fake.lexify(text='????????????????????')}@mail.ru", PASS, "./test/data/pics/wrong_info.png"),
             # Email незарегистрированного пользователя + имеющийся в БД пароль
             (EMAIL, f"{fake.lexify(text='??????????????')}", "./test/data/pics/wrong_info.png"),
             # Email зарегистрированного пользователя + неправильный пароль
             (f"{fake.lexify(text='???????????????????')}", f"{fake.lexify(text='???????')}",
              "./test/data/pics/wrong_email.png"),  # Невалидные email +  пароль
             (PASS, EMAIL, "./test/data/pics/wrong_email.png")]  # Валидные email + пароль, но в неправильных полях
