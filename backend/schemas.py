from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ComponentBase(BaseModel):
    category: str
    brand: str
    model: str
    socket: Optional[str] = None
    ram_type: Optional[str] = None
    wattage: Optional[int] = None
    price: float

class ComponentCreate(ComponentBase):
    pass

class Component(ComponentBase):
    id: int
    updated_at: datetime

    class Config:
        from_attributes = True

class BuildComponentBase(BaseModel):
    component_id: int

class BuildCreate(BaseModel):
    name: str
    total_price: float
    components: List[int] # List of component IDs

class Build(BaseModel):
    id: int
    name: str
    total_price: float
    created_at: datetime

    class Config:
        from_attributes = True
