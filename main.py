from fastapi import FastAPI
from routes.route import router
from routes.middleware import InjectUserIdMiddleware


app = FastAPI()
app.add_middleware(InjectUserIdMiddleware)
app.include_router(router)
