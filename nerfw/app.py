from pathlib import Path

from fastapi import FastAPI
from sqladmin import Admin
from starlette.middleware.gzip import GZipMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from nerfw.admin import UserAdmin, SaveAdmin
from nerfw.database import engine
from nerfw.routes.api import api_router

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=6)
app.include_router(api_router)

frontend_dir = Path(__file__).parent / "build"


@app.get("/")
async def read_root():
    return FileResponse(frontend_dir / "index.html")


@app.get("/asset-manifest.json")
async def asset_manifest():
    return FileResponse(frontend_dir / "asset-manifest.json")


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(frontend_dir / "favicon.ico")


@app.get("/logo192.png")
async def logo192():
    return FileResponse(frontend_dir / "logo192.png")


@app.get("/logo512.png")
async def logo512():
    return FileResponse(frontend_dir / "logo512.png")


@app.get("/manifest.json")
async def manifest():
    return FileResponse(frontend_dir / "manifest.json")


@app.get("/robots.txt")
async def robots():
    return FileResponse(frontend_dir / "robots.txt")


@app.exception_handler(404)
async def not_found(_, __):
    return FileResponse(frontend_dir / "index.html")


admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(SaveAdmin)
app.mount(
    "/static", StaticFiles(directory=frontend_dir / "static", html=True), name="ui"
)
