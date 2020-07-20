"""
TODO:
    - Консольная работа с конфигами (CLI для работы с конфигами)
    - Работа со сторонними сервисами конфигурации
    - Добавление секретных полей в конфиг
    - Оформление Python пакета для PyPi
"""

from pprint import pprint
from src.single_config import SingleConfig


config = SingleConfig('debug.yml')

pprint(config)
