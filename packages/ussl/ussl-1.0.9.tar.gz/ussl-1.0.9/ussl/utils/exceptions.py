from typing import List


class SOARException(Exception):
    _return_code: int = 1
    _TEMPLATE = 'ОШИБКА: {error}.'

    @property
    def return_code(self):
        return self._return_code

    def __init__(self, error_message: str = None):
        self.error = error_message

    def __str__(self):
        return self._TEMPLATE.format(error=self.error)


class DataError(SOARException):
    _return_code: int = 10
    args: List[str]

    def __init__(self, property_names: List[str] = None) -> None:
        self.args = property_names


class NoInputError(DataError):
    _return_code: int = 11
    _MISSING_INPUTS = 'Отсутствуют обязательные входные аргументы: {names}.'

    def __str__(self):
        return self._MISSING_INPUTS.format(names=', '.join(self.args))


class NoSecretsError(DataError):
    _return_code: int = 12
    _MISSING_SECRETS = 'Отсутствуют секреты: {names}.'

    def __str__(self):
        return self._MISSING_SECRETS.format(names=', '.join(self.args))


class BadInputError(DataError):
    _return_code: int = 13
    _TEMPLATE = 'Ошибка валидации входных данных: {error}.'


class BadSecretsError(DataError):
    _return_code: int = 14
    _TEMPLATE = 'Ошибка валидации секретов: {error}.'


class ProtocolError(SOARException):
    _return_code = 20


class ConnectionFailedError(ProtocolError):
    _return_code = 21
    _TEMPLATE = 'Не удалось подключиться к серверу: {error}.'


class CredentialsError(ProtocolError):
    _return_code: int = 22
    _TEMPLATE = 'Неверные данные для входа: {error}.'


class PermissionsError(ProtocolError):
    _return_code: int = 23
    _TEMPLATE = 'Отсутствуют необходимые права: {error}.'


class ExecutionError(ProtocolError):
    _return_code = 24
    _TEMPLATE = 'Возникла ошибка платформы: {error}.'
