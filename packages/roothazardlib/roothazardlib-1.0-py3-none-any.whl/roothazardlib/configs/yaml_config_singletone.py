"""
Provide some common classes for work with configurations
"""

import typing

import yaml
import pydantic

class Singletone(type):
    """
    Singletone metaclass for making singletones
    """

    __instances: dict[type, typing.Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)

        return cls.__instances[cls]


class ConfigModel(pydantic.BaseModel):
    """
    This model should be inherited and the type of config
    should be relaced with the real one. ConfigModel child
    than may be passed in YamlConfig to correctly
    validate yaml file content
    """

    cfg: typing.Type[pydantic.BaseModel]


class ConstModelWrapper(metaclass=Singletone):
    """
    If you make model wrapper based on
    these class it will be const and singletone
    """

    _model: pydantic.BaseModel

    def __getattr__(self, name: str) -> typing.Any:
        return getattr(self.__model, name)

    def __setattr__(self, name: str, value: typing.Any) -> None:
        try:
            self.__getattribute__(name)
            super().__setattr__(name, value)
        except AttributeError as attr_err:
            raise AttributeError("Object is readonly") from attr_err


class YamlConfig(ConstModelWrapper): # pylint: disable=too-few-public-methods
    """
    Universal Yaml config class
    """

    def __init__(self,
        config_file_path: str,
        top_level_model: typing.Type[ConfigModel]
    ) -> None:
        with open(config_file_path, mode="r", encoding="utf-8") as config_file:
            config = yaml.safe_load(config_file)

        self._model = top_level_model(cfg=config)
