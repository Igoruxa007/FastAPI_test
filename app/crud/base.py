from __future__ import annotations


class CRUDBase():
    def __init__(self, model):
        self.model = model

    def get(self, db, id):
        return db.query(self.model).filter(self.model.id == id).first()
