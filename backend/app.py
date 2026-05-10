from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from config import Config
from extensions import db, jwt, bcrypt

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

jwt.init_app(app)

bcrypt.init_app(app)

CORS(app)

from models.user_model import User
from models.project_model import Project
from models.task_model import Task

@app.route("/")
def home():
    return {
        "message": "Team Task Manager Backend Running Successfully"
    }


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "member")

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({
            "message": "Email already exists"
        }), 400

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    new_user = User(
        name=name,
        email=email,
        password=hashed_password,
        role=role
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    }), 201
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    is_password_correct = bcrypt.check_password_hash(
        user.password,
        password
    )

    if not is_password_correct:
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "message": "Login successful",
        "token": access_token,
        "user": user.to_dict()
    }), 200
@app.route("/projects", methods=["POST"])
@jwt_required()
def create_project():

    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)

    if user.role != "admin":
        return jsonify({
            "message": "Only admin can create projects"
        }), 403

    data = request.get_json()

    project_name = data.get("project_name")
    description = data.get("description")

    new_project = Project(
        project_name=project_name,
        description=description,
        created_by=current_user_id
    )

    db.session.add(new_project)
    db.session.commit()

    return jsonify({
        "message": "Project created successfully",
        "project": new_project.to_dict()
    }), 201
@app.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():

    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)

    if user.role != "admin":
        return jsonify({
            "message": "Only admin can create tasks"
        }), 403

    data = request.get_json()

    title = data.get("title")
    description = data.get("description")
    assigned_to = data.get("assigned_to")
    project_id = data.get("project_id")

    assigned_user = User.query.get(assigned_to)

    if not assigned_user:
        return jsonify({
            "message": "Assigned user not found"
        }), 404

    project = Project.query.get(project_id)

    if not project:
        return jsonify({
            "message": "Project not found"
        }), 404

    new_task = Task(
        title=title,
        description=description,
        assigned_to=assigned_to,
        project_id=project_id,
        created_by=current_user_id
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({
        "message": "Task created successfully",
        "task": new_task.to_dict()
    }), 201
@app.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():

    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)

    if user.role == "admin":
        tasks = Task.query.all()
    else:
        tasks = Task.query.filter_by(
            assigned_to=current_user_id
        ).all()

    return jsonify({
        "tasks": [task.to_dict() for task in tasks]
    }), 200
@app.route("/tasks/<int:task_id>", methods=["PUT"])
@jwt_required()
def update_task(task_id):

    current_user_id = get_jwt_identity()

    task = Task.query.get(task_id)

    if not task:
        return jsonify({
            "message": "Task not found"
        }), 404

    user = User.query.get(current_user_id)

    if (
        user.role != "admin"
        and task.assigned_to != int(current_user_id)
    ):
        return jsonify({
            "message": "Unauthorized"
        }), 403

    data = request.get_json()

    task.status = data.get("status", task.status)

    db.session.commit()

    return jsonify({
        "message": "Task updated successfully",
        "task": task.to_dict()
    }), 200
if __name__ == "__main__":
    

    with app.app_context():
        db.create_all()

    app.run(debug=True)