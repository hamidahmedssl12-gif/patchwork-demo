from fastapi import APIRouter, Depends

router = APIRouter()


def require_auth():
    ...


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
