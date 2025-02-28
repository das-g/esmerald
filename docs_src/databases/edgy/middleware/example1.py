from starlette.middleware import Middleware as StarletteMiddleware

from esmerald import Esmerald
from esmerald.conf import settings
from esmerald.config.jwt import JWTConfig
from esmerald.contrib.auth.edgy.middleware import JWTAuthMiddleware
from esmerald.utils.module_loading import import_string

jwt_config = JWTConfig(signing_key=settings.secret_key, auth_header_types=["Bearer", "Token"])

jwt_auth_middleware = StarletteMiddleware(
    JWTAuthMiddleware,
    config=jwt_config,
    user=import_string("myapp.models.User"),
)

app = Esmerald(middleware=[jwt_auth_middleware])
