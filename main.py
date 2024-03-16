from uvicorn import run
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from utils import get_config
from routers import task, assistant

app_cfg = get_config().app
host = app_cfg.host
port = app_cfg.port
path = app_cfg.path
version = app_cfg.version

app = FastAPI(version=version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=task.router)
app.include_router(router=assistant.router)

app.mount(path=f"/{path}", app=StaticFiles(directory="./views", html=True), name="tasks")

if __name__ == "__main__":
    run(app=app, host=host)
