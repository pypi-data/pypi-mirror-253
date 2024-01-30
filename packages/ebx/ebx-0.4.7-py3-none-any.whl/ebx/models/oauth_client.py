"""Class defining a oauth client."""

"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""
from dataclasses import dataclass,asdict
from ebx.constants.api import API_SECRETS_FILE
from ebx.config import ClientConfig

@dataclass
class OAuthClient:
    """Describes a oauth client."""

    name: str
    """The id of the client."""

    description: str
    """The description of the client."""

    client_id: str
    """The Client ID of the client."""

    client_secret: str
    """The Client secret."""

    enabled: bool
    """Whether the client is enabled."""

    def save(self, config:ClientConfig, filename: str=API_SECRETS_FILE):
        """save this dataclass to disk in json format"""
        config.get_persistence_driver().save(filename, asdict(self))
        return self

    @staticmethod
    def load(config:ClientConfig, filename: str=API_SECRETS_FILE):
        """load this dataclass from disk in json format"""
        data = config.get_persistence_driver().load(filename)
        return OAuthClient(**data)
    
    @staticmethod
    def saved_credentials_exists(config:ClientConfig, filename: str=API_SECRETS_FILE):
        """check if the credentials file exists"""
        return config.get_persistence_driver().exists(filename)
        


        