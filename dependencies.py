from auth import verify_session
from config import DATABASE_URL


def get_current_user(token: str):
    if not verify_session(token):
        raise PermissionError("invalid session")
    return {"db": DATABASE_URL, "token": token}
