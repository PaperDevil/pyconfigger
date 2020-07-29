"""
TODO:
    - Консольная работа с конфигами (CLI для работы с конфигами)
    - Работа со сторонними сервисами конфигурации
    - Добавление секретных полей в конфиг
    - Оформление Python пакета для PyPi
"""

from field.fields import DefaultConfigField
from config.single_config import SingleConfig


config = SingleConfig('debug.yml')  # Creation
config['hash'] = DefaultConfigField('color', 'ORANGE')
config = SingleConfig('debug.yml')  # Getting

print(config)
