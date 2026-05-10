from extensions import db


class Task(db.Model):

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    description = db.Column(db.Text, nullable=True)

    status = db.Column(
        db.String(50),
        default="Pending"
    )

    assigned_to = db.Column(
        db.Integer,
        nullable=False
    )

    project_id = db.Column(
        db.Integer,
        nullable=False
    )

    created_by = db.Column(
        db.Integer,
        nullable=False
    )

    def to_dict(self):

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "project_id": self.project_id,
            "created_by": self.created_by
        }