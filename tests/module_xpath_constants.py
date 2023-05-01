REGISTER_PAGE = "//h2[text()='Регистрация']" # Страница регистрации с заголовком "Регистрация"
NAME_INPUT = "//label[text()='Имя']/following-sibling::input" # Поле ввода имени
EMAIL_INPUT = "//label[text()='Email']/following-sibling::input" # Поле ввода email
PASSWORD_INPUT = "//label[text()='Пароль']/following-sibling::input" # Поле ввода пароля
REGISTER_BUTTON = "//button[text()='Зарегистрироваться']" # Кнопка "Зарегистрироваться" на странице регистрации
LOGIN_PAGE = "//h2[text()='Вход']" # Страница входа с заголовком "Войти"
LOGIN_BUTTON = "//button[text()='Войти']" # Кнопка "Войти" на странице входа
CABINET_LINK = "//a[@href='/account']" # Ссылка на личный кабинет
CABINET_PAGE = "//a[text()='Профиль']" # Ссылка "Профиль" вличном кабинете
CABINET_PAGE_LOGIN_INFO = "//label[text()='Логин']/following-sibling::input" # Поле Email в личном кабинете кабинете
ERROR_MESSAGE_REGISTER = "//p[starts-with(@class,'input__error')]" # Сообщение об ошибке
MAIN_PAGE = "//section/h1[starts-with(text(),'Соберите')]" # Главная страница с заголовком "Соберите бургер"