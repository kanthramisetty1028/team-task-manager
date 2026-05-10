from extensions import db


class Project(db.Model):

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)

    project_name = db.Column(db.String(150), nullable=False)

    description = db.Column(db.Text, nullable=True)

    created_by = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "project_name": self.project_name,
            "description": self.description,
            "created_by": self.created_by
        }