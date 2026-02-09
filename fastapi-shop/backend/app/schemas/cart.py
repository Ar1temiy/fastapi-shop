from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity(must be gt 0)")
    
class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="New quantity must be gt 0")
    
class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product Name")
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., description="Quantity in cart")
    subtotal: float = Field(..., description="Total price for this item (item*quantity)")
    image_url: str|None = Field(None, description="Product image url")
    
class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items cart")
    total:float = Field(..., description="Total cart price")
    items_count: int = Field(..., description="Total number of items in cart")