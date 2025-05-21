from schema.ingredients_sch import ingre_schemas
from sqlmodel import Session, select
from models.Ingredients import Ingredients

# Leer todos los ingredientes
def get_all_ingredients(db: Session):
    sql_read = select(Ingredients)
    ingredients = db.exec(sql_read).all()
    return ingre_schemas(ingredients)

# Añadir un ingrediente
def add_ingredient(db: Session, id: int, nom: str, id_proveedor: int):
    new_ingredient = Ingredients(id=id, nom=nom, id_proveedor=id_proveedor)
    db.add(new_ingredient)
    db.commit()
    db.refresh(new_ingredient)
    return {"message": "Created ingredient successfully"}

# Eliminar un ingrediente
def delete_ingredient(db: Session, id: int):
    ingredient = db.exec(select(Ingredients).where(Ingredients.id == id)).first()
    if ingredient:
        db.delete(ingredient)
        db.commit()
        return {"message": "Deleted ingredient successfully"}
    return {"message": "Ingredient not found"}

# Actualizar un ingrediente
def update_ingredient(db: Session, id: int, nom: str, id_proveedor: int):
    ingredient = db.exec(select(Ingredients).where(Ingredients.id == id)).first()
    if not ingredient:
        return {"message": "Ingredient not found"}

    ingredient.nom = nom
    ingredient.id_proveedor = id_proveedor

    db.commit()
    db.refresh(ingredient)
    return {"message": "Ingredient updated successfully"}