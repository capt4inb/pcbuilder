from backend.database import SessionLocal, engine, Base
from backend.models import Component

Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    
    # Check if we already have data
    if db.query(Component).count() > 0:
        print("Database already seeded.")
        return

    components = [
        # CPU
        {"category": "CPU", "brand": "AMD", "model": "Ryzen 5 5600X", "price": 2500000, "socket": "AM4"},
        {"category": "CPU", "brand": "Intel", "model": "Core i5 12400F", "price": 4200000, "socket": "LGA1700"},
        
        # Motherboard
        {"category": "Motherboard", "brand": "ASRock", "model": "B450M-HDV", "price": 1460000, "socket": "AM4", "ram_type": "DDR4"},
        {"category": "Motherboard", "brand": "MSI", "model": "B550M PRO", "price": 2100000, "socket": "AM4", "ram_type": "DDR4"},
        {"category": "Motherboard", "brand": "ASUS", "model": "PRIME B660M-A", "price": 3100000, "socket": "LGA1700", "ram_type": "DDR4"},
        
        # GPU
        {"category": "GPU", "brand": "NVIDIA", "model": "RTX 3060 12GB", "price": 6050000, "wattage": 170},
        {"category": "GPU", "brand": "NVIDIA", "model": "RTX 4060", "price": 7800000, "wattage": 115},
        
        # RAM
        {"category": "RAM", "brand": "Corsair", "model": "16GB DDR4 3200", "price": 1000000, "ram_type": "DDR4"},
        {"category": "RAM", "brand": "G.Skill", "model": "32GB DDR4 3200", "price": 1800000, "ram_type": "DDR4"},
        
        # SSD
        {"category": "SSD", "brand": "Samsung", "model": "512GB NVMe", "price": 1050000},
        {"category": "SSD", "brand": "Crucial", "model": "1TB NVMe", "price": 1900000},
        
        # PSU
        {"category": "PSU", "brand": "Cooler Master", "model": "650W Bronze", "price": 800000, "wattage": 650},
        {"category": "PSU", "brand": "Corsair", "model": "750W Gold", "price": 1400000, "wattage": 750},
        
        # CASE
        {"category": "Case", "brand": "NZXT", "model": "Mid Tower RGB", "price": 570000},
        
        # COOLING
        {"category": "Cooling", "brand": "Deepcool", "model": "Air Cooler", "price": 350000},
    ]

    for comp_data in components:
        component = Component(**comp_data)
        db.add(component)
    
    db.commit()
    db.close()
    print("Database seeded successfully.")

if __name__ == "__main__":
    seed_data()
