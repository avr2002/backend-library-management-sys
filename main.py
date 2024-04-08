from fastapi import FastAPI
from routes.route import router


app = FastAPI(debug=True)

app.include_router(router)
