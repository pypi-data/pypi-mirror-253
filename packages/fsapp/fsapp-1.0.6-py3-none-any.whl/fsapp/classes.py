from abc import ABC, abstractmethod
from typing import Tuple, Union


class BaseExecutor(ABC):
    @abstractmethod
    def __call__(self,  data_type: str, value: list) -> Tuple[bool, dict]:
        """
                Основная функция, которая вызывается и
                возвращает результат
                :param data_type: тип данных
                       value: список искомых значений
                :return: возвращаем tuple, где первый элемент - флаг о успешном/неуспешном
                выполнении функции, второй элемент - полученные данные с типом dict, или
                ошибка с типом str
                """
        return True, {"value": {value}}

    def __init__(self):
        pass

