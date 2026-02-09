from datetime import datetime, date
from typing import List
from sqlalchemy import DateTime, Float, Integer, String, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), index=True, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"), nullable=False)
    image_url: Mapped[str] = mapped_column(String)
    created_at: Mapped[date] = mapped_column(DateTime, default=datetime.utcnow)
    
    category = relationship("Category", back_populates="products")
    
    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price = '{self.price}')"