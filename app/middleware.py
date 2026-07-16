from fastapi import FastAPI

app = FastAPI()


class OrphanMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        await self.app(scope, receive, send)


# CCV: registered here, but no file that defines a route ever imports
# 'OrphanMiddleware' -- dead wiring.
app.add_middleware(OrphanMiddleware)
