import os

from fastapi import APIRouter, Depends

from auth import verify_session

router = APIRouter()


def require_auth(token: str = ""):
    if not verify_session(token):
        raise PermissionError("invalid session")


@router.get("/items", dependencies=[Depends(require_auth)])
def list_items():
    ...


@router.get("/items/{id}", dependencies=[Depends(require_auth)])
def get_item(id: int):
    ...


@router.post("/items", dependencies=[Depends(require_auth)])
def create_item():
    ...


@router.put("/items/{id}", dependencies=[Depends(require_auth)])
def update_item(id: int):
    ...


@router.delete("/items/{id}", dependencies=[Depends(require_auth)])
def delete_item(id: int):
    ...


@router.patch("/items/{id}", dependencies=[Depends(require_auth)])
def patch_item(id: int):
    ...


@router.post("/items/{id}/archive", dependencies=[Depends(require_auth)])
def archive_item(id: int):
    ...


@router.post("/items/{id}/restore", dependencies=[Depends(require_auth)])
def restore_item(id: int):
    ...


@router.delete("/items/{id}/permanent", dependencies=[Depends(require_auth)])
def permanently_delete_item(id: int):
    ...


# SSR: every other mutating route in this cluster carries
# Depends(require_auth); this one doesn't.
@router.put("/items/{id}/rename")
def rename_item(id: int):
    ...


# BCI: EXPORT_WEBHOOK_URL is read but never declared in .env.example --
# the kind of thing an LLM adds when it invents a plausible-sounding env
# var for a new feature without checking the project's actual config.
@router.post("/items/{id}/export", dependencies=[Depends(require_auth)])
def export_item(id: int):
    webhook_url = os.environ["EXPORT_WEBHOOK_URL"]
    return {"id": id, "webhook": webhook_url}
