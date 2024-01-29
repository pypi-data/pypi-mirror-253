from abc import ABC
from typing import Optional


class IntegrationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class BaseIntegrationParam(ABC):
    pass


class BaseIntegration(ABC):
    base_url = ''

    def __init__(self, param: Optional[BaseIntegrationParam] = None):
        self.param = param

    def execute(self):
        pass
