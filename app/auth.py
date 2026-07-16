import fastnonexistentpkg123

from .config import SESSION_SECRET


def verify_session(token: str) -> bool:
    # DHI: 'fastnonexistentpkg123' isn't declared in requirements.txt and
    # doesn't exist on PyPI -- hallucinated.
    # SRF: the import edge points at that same phantom module.
    # PIA: this call targets it too -- "the API cannot exist".
    return fastnonexistentpkg123.verify(token, SESSION_SECRET)
