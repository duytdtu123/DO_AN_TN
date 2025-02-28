from _typeshed import Incomplete

from authlib.oauth2.rfc7009 import RevocationEndpoint

class JWTRevocationEndpoint(RevocationEndpoint):
    issuer: Incomplete
    def __init__(self, issuer, server: Incomplete | None = None, *args, **kwargs) -> None: ...
    def authenticate_token(self, request, client) -> None: ...
    def get_jwks(self) -> None: ...
