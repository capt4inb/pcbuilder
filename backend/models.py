from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base

class Component(Base):
    __tablename__ = "components"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True) # CPU, GPU, etc.
    brand = Column(String, index=True)
    model = Column(String, index=True)
    socket = Column(String, nullable=True)
    ram_type = Column(String, nullable=True)
    wattage = Column(Integer, nullable=True)
    price = Column(Float)
    image_url = Column(String, nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Build(Base):
    __tablename__ = "builds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    total_price = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    components = relationship("BuildComponent", back_populates="build")

class BuildComponent(Base):
    __tablename__ = "build_components"

    id = Column(Integer, primary_key=True, index=True)
    build_id = Column(Integer, ForeignKey("builds.id"))
    component_id = Column(Integer, ForeignKey("components.id"))

    build = relationship("Build", back_populates="components")
    component = relationship("Component")
