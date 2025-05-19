from schema.Proveidor_sch import prove_schemas
from sqlmodel import Session, select
from models.Proveidor import Proveidor

# Leer todos los proveedores
def get_all_proveidors(db: Session):
    sql_read = select(Proveidor)
    proveidors = db.exec(sql_read).all()
    return prove_schemas(proveidors)

# Añadir un proveedor
def add_proveidor(db: Session, cif: str, nom_fiscal: str):
    new_proveidor = Proveidor(cif=cif, nom_fiscal=nom_fiscal)
    db.add(new_proveidor)
    db.commit()
    db.refresh(new_proveidor)
    return {"message": "Created provider successfully"}

# Eliminar un proveedor
def delete_proveidor(db: Session, cif: str):
    proveidor = db.exec(select(Proveidor).where(Proveidor.cif == cif)).first()
    if proveidor:
        db.delete(proveidor)
        db.commit()
        return {"message": "Deleted provider successfully"}
    return {"message": "Provider not found"}

# Actualizar un proveedor
def update_proveidor(db: Session, cif: str, nom_fiscal: str):
    proveidor = db.exec(select(Proveidor).where(Proveidor.cif == cif)).first()
    if not proveidor:
        return {"message": "Provider not found"}

    proveidor.nom_fiscal = nom_fiscal

    db.commit()
    db.refresh(proveidor)
    return {"message": "Provider updated successfully"}
