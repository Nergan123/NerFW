from pathlib import Path

from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from nerfw.routes.api import api_router

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=6)
app.include_router(api_router)

frontend_dir = Path(__file__).parent / "build"


@app.get("/")
async def read_root():
    return FileResponse(frontend_dir / "index.html")


@app.exception_handler(404)
async def not_found(_, __):
    return FileResponse(frontend_dir / "index.html")


app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="ui")
