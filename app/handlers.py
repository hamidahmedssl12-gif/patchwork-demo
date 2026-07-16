from .models import get_user


def profile_handler():
    u = get_user()
    # CCV: 'email' isn't a field on User -- producer/consumer mismatch.
    return u.email


def render_welcome():
    # RCF: this path doesn't exist anywhere in the repo.
    with open("templates/welcome.html") as f:
        return f.read()


def status_label(code: int) -> str:
    # RCF: declares a str return type but falls off the end for any code
    # other than 200/404 -- a reachable path that never returns.
    if code == 200:
        return "ok"
    if code == 404:
        return "not found"


def compute_total(items: list[int]) -> int:
    return sum(items)
    # CFC: unreachable -- every path above already returns.
    log_computation(items)
