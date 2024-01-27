import os.path

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from starlette.staticfiles import StaticFiles

from chef.api import api_router
from chef.models import ensure_tables
from chef.settings import settings, HOME_DIR


app = FastAPI()
app.include_router(api_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def serve():
    options = "\n".join([f"{k.upper()}: '{v}'" for k, v in settings])
    logger.info(f"""

    ███████╗██╗  ██╗███████╗███████╗
    ██╔════╝██║  ██║██╔════╝██╔════╝
    ██║     ███████║█████╗  █████╗  
    ██║     ██╔══██║██╔══╝  ██╔══╝  
    ║██████ ██║  ██║███████╗██║     
    ╚═════════╝  ╚═╝╚══════╝╚═╝

    ...starting with following settings:

{options}
""")

    if not os.path.isdir(settings.images_folder):
        logger.info(f"Creating images folder: {settings.images_folder}")
        os.makedirs(settings.images_folder, exist_ok=True)

    ensure_tables()

    if settings.log_file:
        logger.add(settings.log_file, level=settings.log_level)

    if settings.serve_frontend:
        if not settings.serve_frontend_path or not os.path.isdir(settings.serve_frontend_path):
            logger.error(
                f"Frontend files '{settings.serve_frontend_path}' not found, "
                f"frontend can't be served."
            )
            return
        app.mount("/images", StaticFiles(directory=settings.images_folder))
        app.mount("/", StaticFiles(directory=settings.serve_frontend_path, html=True))

    uvicorn.run(app, host=settings.uvicorn_host, port=settings.uvicorn_port)


if __name__ == '__main__':
    serve()
