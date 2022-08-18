from models import db


class Posts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(50), nullable=True)
    likes = db.Column(db.Integer(), nullable=True)
    created_by = db.Column(db.Integer(), nullable=True)
    created_on = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime(timezone=True),
        server_default=db.func.now(),
        server_onupdate=db.func.now(),
    )

    # Return model as Dictionary

    def GetDict(self):
        return {
            "id": self.id,
            "text": self.text,
            "likes": self.likes,
            "created_by": self.created_by,
            "created_on": str(self.created_on),
            "updated_on": str(self.updated_on),
        }
