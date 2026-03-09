from fastapi_users.authentication import JWTStrategy

from src.config import settings


def get_jwt_strategy() -> JWTStrategy:
    private_key = settings.auth.private_key_path.read_text()
    public_key = settings.auth.public_key_path.read_text()
    return JWTStrategy(
        secret=private_key,
        lifetime_seconds=3600,
        algorithm="RS256",
        public_key=public_key,
    )
