from sqlalchemy.orm import Session
from typing import List
from repositories.category_repository import CategoryRepository
from repositories.product_repository import ProductRepository
from schemas.category import CategoryResponse, CategoryCreate
from schemas.product import ProductResponse, ProductListResponse, ProductCreate
from fastapi import HTTPException, status

class ProductService:
    def __init__(self, db: Session):
        self.product_repository = ProductRepository(db)
        self.category_repository = CategoryRepository(db)
        
    def get_all_products(self) -> ProductListResponse:
        products = self.product_repository.get_all
        products_response = [ProductResponse.model_validate(prod) for prod in products]
        return ProductListResponse(products=products_response, total=len(products_response))
    
    def get_category_by_id(self, category_id: int) -> CategoryResponse:
        category = self.repository.get_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="category with this id not found"
            )
        return CategoryResponse.model_validate(category)
    def create_category(self, category_data: CategoryCreate) -> CategoryResponse:
        category = self.repository.create(category_data)
        return CategoryResponse.model_validate(category)