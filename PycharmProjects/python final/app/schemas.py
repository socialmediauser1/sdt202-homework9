from typing import Optional
from pydantic import BaseModel, field_validator, constr
from .models import ClothingCategory

class ClothingBase(BaseModel):
    name: constr(min_length=2, max_length=120)
    category: ClothingCategory
    color: Optional[constr(strip_whitespace=True, max_length=50)] = None
    size: Optional[constr(strip_whitespace=True, max_length=40)] = None
    description: Optional[constr(strip_whitespace=True, max_length=600)] = None
    image_url: Optional[str] = None

    @field_validator('image_url')
    @classmethod
    def validate_image_url(cls, v: Optional[str]) -> Optional[str]:
        if not v or not v.strip():
            return None
        v = v.strip()
        if v and not (v.startswith('http://') or v.startswith('https://')):
            raise ValueError('Image URL must start with http:// or https://')
        return v

class ClothingCreate(ClothingBase):
    pass

class ClothingUpdate(ClothingBase):
    pass
