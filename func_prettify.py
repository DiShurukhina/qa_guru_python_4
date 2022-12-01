"""Сделайте функцию, которая будет печатать читаемое имя переданной ей функции и значений аргументов.
Вызовите ее внутри функций, описанных ниже
Например, вызов следующей функции должен преобразовать имя функции в более читаемый вариант
(заменить символ подчеркивания на пробел, сделать буквы заглавными (или первую букву),
затем вывести значения всех аргументов этой функции:d>>> open_browser(browser_name="Chrome")
"Open Browser Chrome" или "Open Browser [Chrome]" – на ваш выбор.
Подсказка: Имя функции можно получить с помощью func.__name__
def open_browser(browser_name):
    pass
def go_to_companyname_homepage(page_url):
    pass
def find_registration_button_on_login_page(page_url, button_text):
    pass
"""


def prettify(func, *args):
    func_name = func.__name__.replace('_', ' ').title()
    print(func_name, [*args])


def open_browser(browser_name):
    prettify(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    prettify(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    prettify(find_registration_button_on_login_page, page_url, button_text)


url = 'https://github.com/'
button_text = 'Sign in'

open_browser('Chrome')
go_to_companyname_homepage(url)
find_registration_button_on_login_page(url, button_text)
