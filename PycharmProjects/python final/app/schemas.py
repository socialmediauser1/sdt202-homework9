from typing import Optional
from pydantic import BaseModel, HttpUrl, constr
from .models import ClothingCategory

class ClothingBase(BaseModel):
    name: constr(min_length=2, max_length=120)
    category: ClothingCategory
    color: Optional[constr(strip_whitespace=True, max_length=50)] = None
    size: Optional[constr(strip_whitespace=True, max_length=40)] = None
    description: Optional[constr(strip_whitespace=True, max_length=600)] = None
    image_url: Optional[HttpUrl] = None

class ClothingCreate(ClothingBase):
    pass

class ClothingUpdate(ClothingBase):
    pass
