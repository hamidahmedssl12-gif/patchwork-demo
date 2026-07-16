# Patchwork demo repo

A tiny FastAPI service used as Patchwork's live example -- Patchwork runs its real detection pipeline against this exact repo so you can see genuine findings, not screenshots.

Every issue below is seeded on purpose, one per real detector Patchwork ships. Nothing here is a mistake -- it's here so the pipeline has something real to catch.

Files are flat at the repo root (not a package) on purpose: patchwork-core's dependency/import analysis only recognizes **top-level `.py` files** as "local modules." Nesting these under a package directory would make every intra-repo import invisible to the import graph (so `related files` would come back empty) or misclassify it as an external, undeclared dependency (a false DHI finding) -- neither is what a real seeded example should do.

| Detector | File | What's wrong |
|---|---|---|
| BCI (config incoherence) | `config.py` | `SESSION_SECRET` is read from the environment but never declared in `.env.example` |
| DHI (dependency hallucination) | `auth.py` | imports `fastnonexistentpkg123`, which isn't in `requirements.txt` and doesn't exist on PyPI |
| SRF (symbol resolution) | `auth.py` | that same import can't resolve to a real dependency |
| PIA (phantom API) | `auth.py` | calls `fastnonexistentpkg123.verify(...)`, a method on a module that doesn't exist |
| CCV (schema variant) | `handlers.py` + `models.py` | reads `.email` off a `User`, which only declares `id` and `name` |
| CCV (middleware variant) | `middleware.py` | `OrphanMiddleware` is registered but no route module ever imports it |
| CFC (control flow) | `handlers.py` | a line after an unconditional `return` in `compute_total` can never execute |
| RCF (resource coherence) | `handlers.py` | opens `templates/welcome.html`, which doesn't exist in this repo |
| RCF (return coherence) | `handlers.py` | `status_label` declares `-> str` but falls off the end for any code other than 200/404 |
| SSR (security structural regression) | `routes.py` | 9 of the 10 routes under `/items` require `Depends(require_auth)`; `PUT /items/{id}/rename` doesn't |

`auth.py` is also a good seed file for "related files": `routes.py` and `dependencies.py` both import it, and it imports `config.py`.

## Running it

```
pip install -r requirements.txt
uvicorn main:app --reload
```

(It'll actually start -- the phantom import in `auth.py` is only ever exercised by the un-called `verify_session`, so it won't crash on boot.)
