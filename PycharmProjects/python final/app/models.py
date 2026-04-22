from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import List
from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

class UserRole(str, Enum):
    GUEST = "guest"
    DESIGNER = "designer"
    ADMIN = "admin"

class ClothingCategory(str, Enum):
    TOP = "top"
    BOTTOM = "bottom"
    SHOES = "shoes"
    ACCESSORY = "accessory"
    OUTERWEAR = "outerwear"
    HATS = "hats"

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole), default=UserRole.DESIGNER, nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    outfits: Mapped[List["Outfit"]] = relationship(
        "Outfit", back_populates="user", cascade="all,delete"
    )

class Clothing(Base):
    __tablename__ = "clothes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    category: Mapped[ClothingCategory] = mapped_column(
        SQLEnum(ClothingCategory), nullable=False
    )
    color: Mapped[str | None] = mapped_column(String(50), nullable=True)
    size: Mapped[str | None] = mapped_column(String(40), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    image_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    outfit_items: Mapped[List["OutfitItem"]] = relationship(
        "OutfitItem", back_populates="clothing", cascade="all,delete"
    )

class Outfit(Base):
    __tablename__ = "outfits"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    occasion: Mapped[str | None] = mapped_column(String(120), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    user: Mapped[User] = relationship("User", back_populates="outfits")
    items: Mapped[List["OutfitItem"]] = relationship(
        "OutfitItem", back_populates="outfit", cascade="all,delete"
    )

class OutfitItem(Base):
    __tablename__ = "outfit_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    outfit_id: Mapped[int] = mapped_column(Integer, ForeignKey("outfits.id"), nullable=False)
    clothing_id: Mapped[int] = mapped_column(Integer, ForeignKey("clothes.id"), nullable=False)
    placement: Mapped[str | None] = mapped_column(String(50), nullable=True)

    outfit: Mapped[Outfit] = relationship("Outfit", back_populates="items")
    clothing: Mapped[Clothing] = relationship("Clothing", back_populates="outfit_items")