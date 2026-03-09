from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.database import get_db
from backend import models, schemas

router = APIRouter(prefix="/api/builds", tags=["builds"])

@router.post("/", response_model=schemas.Build)
def save_build(build_data: schemas.BuildCreate, db: Session = Depends(get_db)):
    db_build = models.Build(name=build_data.name, total_price=build_data.total_price)
    db.add(db_build)
    db.commit()
    db.refresh(db_build)

    for component_id in build_data.components:
        build_comp = models.BuildComponent(build_id=db_build.id, component_id=component_id)
        db.add(build_comp)
    
    db.commit()
    return db_build

@router.get("/", response_model=List[schemas.Build])
def get_builds(db: Session = Depends(get_db)):
    return db.query(models.Build).all()
