from abc import ABC
from typing import Dict

from attr import define


class AuthMethod(ABC):
    def get_auth_headers(self) -> Dict[str, str]:
        """
        The returned dict must include headers to add to authenticate properly to Cirro
        """
        raise NotImplementedError()


@define
class TokenAuth(AuthMethod):
    token: str

    def get_auth_headers(self) -> Dict[str, str]:
        return {"Authorization": f"Bearer {self.token}"}
