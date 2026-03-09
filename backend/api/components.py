from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from backend.database import get_db
from backend import models, schemas

router = APIRouter(prefix="/api/components", tags=["components"])

@router.get("/", response_model=List[schemas.Component])
def get_components(
    category: Optional[str] = None,
    brand: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Component)
    if category:
        query = query.filter(models.Component.category == category)
    if brand:
        query = query.filter(models.Component.brand == brand)
    if search:
        query = query.filter(models.Component.model.contains(search) | models.Component.brand.contains(search))
    return query.all()

@router.get("/categories", response_model=List[str])
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(models.Component.category).distinct().all()
    return [c[0] for c in categories]

@router.post("/update-prices")
def update_prices(updates: List[dict], db: Session = Depends(get_db)):
    # Simple implementation for price updates
    for update in updates:
        component = db.query(models.Component).filter(models.Component.id == update['id']).first()
        if component:
            component.price = update['price']
    db.commit()
    return {"message": "Prices updated successfully"}
