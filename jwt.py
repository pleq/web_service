from starlette.applications import Starlette
from starlette_jwt import JWTAuthenticationBackend
from starlette.middleware.authentication import AuthenticationMiddleware

app = Starlette()
app.add_middleware(AuthenticationMiddleware, backend=JWTAuthenticationBackend(secret_key='secret', prefix='JWT'))
