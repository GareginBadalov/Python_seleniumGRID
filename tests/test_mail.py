import time

from MailPages import MailChecker


def test_mail(browser):
    main_page = MailChecker(browser)
    main_page.go_to_site()
    main_page.auth('garegin.badalov@yandex.ru', 'garik777.')
    text_message = main_page.find_messages('farit valiahmetov')
    main_page.answer('Тестовое задание. Бадалов', text_message)

