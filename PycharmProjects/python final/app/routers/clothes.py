from typing import Dict

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from sqlalchemy.orm import Session

from .. import crud
from ..database import get_session
from ..schemas import ClothingCategory, ClothingCreate


templates = Jinja2Templates(directory="templates")
router = APIRouter(tags=["clothes"])


def _prepare_form_data(form_data) -> Dict[str, str]:
    cleaned: Dict[str, str] = {}
    for key, value in form_data.multi_items():
        if isinstance(value, str):
            cleaned[key] = value.strip() or None
        else:
            cleaned[key] = value
    return cleaned


def _category_options() -> list[tuple[str, str]]:
    return [(choice.value, choice.name.capitalize()) for choice in ClothingCategory]


@router.get("/clothes", response_class=HTMLResponse)
def list_clothes(request: Request, session: Session = Depends(get_session)):
    clothes = crud.list_clothes(session)
    return templates.TemplateResponse(
        "clothes/list.html",
        {"request": request, "clothes": clothes, "page_title": "Catalog"},
    )


@router.get("/clothes/new", response_class=HTMLResponse)
def new_clothing_form(request: Request):
    return templates.TemplateResponse(
        "clothes/form.html",
        {
            "request": request,
            "page_title": "Add Garment",
            "action": "/clothes/new",
            "category_options": _category_options(),
            "form_values": {},
            "errors": {},
        },
    )


@router.post("/clothes/new", response_class=HTMLResponse)
async def create_clothing(request: Request, session: Session = Depends(get_session)):
    form_raw = await request.form()
    cleaned = _prepare_form_data(form_raw)
    try:
        payload = ClothingCreate(**cleaned)
    except ValidationError as exc:
        errors = {error["loc"][0]: error["msg"] for error in exc.errors()}
        return templates.TemplateResponse(
            "clothes/form.html",
            {
                "request": request,
                "page_title": "Add Garment",
                "action": "/clothes/new",
                "category_options": _category_options(),
                "form_values": cleaned,
                "errors": errors,
            },
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )

    item = crud.create_clothing(session, payload)
    return RedirectResponse(
        url=f"/clothes/{item.id}", status_code=status.HTTP_303_SEE_OTHER
    )


@router.get("/clothes/{clothing_id}", response_class=HTMLResponse)
def clothing_detail(
    clothing_id: int, request: Request, session: Session = Depends(get_session)
):
    item = crud.get_clothing(session, clothing_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return templates.TemplateResponse(
        "clothes/detail.html",
        {"request": request, "item": item, "page_title": item.name},
    )


@router.get("/clothes/{clothing_id}/edit", response_class=HTMLResponse)
def edit_clothing_form(
    clothing_id: int, request: Request, session: Session = Depends(get_session)
):
    item = crud.get_clothing(session, clothing_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return templates.TemplateResponse(
        "clothes/form.html",
        {
            "request": request,
            "page_title": f"Edit {item.name}",
            "action": f"/clothes/{item.id}/edit",
            "category_options": _category_options(),
            "form_values": {
                "name": item.name,
                "category": item.category.value if item.category else "",
                "color": item.color or "",
                "size": item.size or "",
                "description": item.description or "",
                "image_url": item.image_url or "",
            },
            "errors": {},
        },
    )


@router.post("/clothes/{clothing_id}/edit", response_class=HTMLResponse)
async def update_clothing(
    clothing_id: int, request: Request, session: Session = Depends(get_session)
):
    item = crud.get_clothing(session, clothing_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    form_raw = await request.form()
    cleaned = _prepare_form_data(form_raw)

    try:
        payload = ClothingCreate(**cleaned)
    except ValidationError as exc:
        errors = {error["loc"][0]: error["msg"] for error in exc.errors()}
        return templates.TemplateResponse(
            "clothes/form.html",
            {
                "request": request,
                "page_title": f"Edit {item.name}",
                "action": f"/clothes/{item.id}/edit",
                "category_options": _category_options(),
                "form_values": cleaned,
                "errors": errors,
            },
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )

    crud.update_clothing(session, item, payload)
    return RedirectResponse(
        url=f"/clothes/{item.id}", status_code=status.HTTP_303_SEE_OTHER
    )


@router.post("/clothes/{clothing_id}/delete", response_class=HTMLResponse)
def delete_clothing(
    clothing_id: int, request: Request, session: Session = Depends(get_session)
):
    item = crud.get_clothing(session, clothing_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    crud.delete_clothing(session, item)
    return RedirectResponse(url="/clothes", status_code=status.HTTP_303_SEE_OTHER)

