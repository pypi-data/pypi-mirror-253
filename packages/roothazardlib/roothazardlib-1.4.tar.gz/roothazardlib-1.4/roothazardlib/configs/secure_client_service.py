"""
Frequently used models
"""

import pydantic

class TLSConfigModel(pydantic.BaseModel):
    """
    Any service which use mutual TLS will need this
    """

    client_cert: pydantic.FilePath
    client_key: pydantic.FilePath
    ca: pydantic.FilePath


class ServerConfigModel(pydantic.BaseModel):
    """
    Any service which servers some API will need this
    """

    host: str
    port: pydantic.PositiveInt
