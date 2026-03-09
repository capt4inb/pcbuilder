import json
from .database import SessionLocal, engine, Base
from .models import Component

def import_hacom_data():
    db = SessionLocal()
    
    try:
        with open("backend/data/hacom_components.json", "r", encoding="utf-8") as f:
            components_data = json.load(f)
        
        for comp_data in components_data:
            # Check if component already exists to avoid duplicates
            existing = db.query(Component).filter(
                Component.model == comp_data["model"],
                Component.category == comp_data["category"]
            ).first()
            
            if existing:
                # Update existing price and image
                existing.price = comp_data["price"]
                existing.image_url = comp_data.get("image_url")
                print(f"Updated: {comp_data['model']}")
            else:
                # Create new component
                component = Component(**comp_data)
                db.add(component)
                print(f"Added: {comp_data['model']}")
        
        db.commit()
    except Exception as e:
        print(f"Error importing data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    import_hacom_data()
