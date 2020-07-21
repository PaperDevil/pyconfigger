"""
TODO:
    - Консольная работа с конфигами (CLI для работы с конфигами)
    - Работа со сторонними сервисами конфигурации
    - Добавление секретных полей в конфиг
    - Оформление Python пакета для PyPi
"""

from pprint import pprint
from src.basic_config import BasicConfig


config = BasicConfig('debug.yml', show_config=False)
port = config('port').value
print(port)