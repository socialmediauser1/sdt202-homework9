from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from .database import Base, engine
from .routers import clothes

load_dotenv()

app = FastAPI(title="Costume Constructor")
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)

app.include_router(clothes.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "home.html", {"request": request, "page_title": "Home"}
    )

@app.get("/health", response_class=JSONResponse)
async def healthcheck():
    return {"status": "ok"}
