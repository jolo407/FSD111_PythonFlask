"""HTTP route definition"""

from flask import request, render_template
from app import app
from app.database import create, read, update, delete, scan 
from datetime import datetime

@app.route("/")
def index():
    serv_time = datetime.now().strftime("%F %H:%M:%S")
    return {
        "ok": True,
        "version": "1.0.0",
        "server_time": serv_time
    }

@app.route("/users")
def get_all_users():
        out = scan()
        out["ok"] = True
        out["message"] = "Success"
        return out

@app.route("/users/<pid>")
def get_one_users(pid):
    out = read(int(pid))
    out["ok"] = True
    out["message"] = "Success"
    return out

@app.route("/users", methods=["POST"])
def create_users():
    users_data = request.json
    new_id = create(
        users_data.get("first_name"),
        users_data.get("last_name"),
        users_data.get("position"),
        users_data.get("department")
    )

    return {"ok": True, "message": "Success", "new_id": new_id}

@app.route("/users/<pid>", methods=["PUT"])
def update_users(pid):
    users_data = request.json
    out = update(int(pid), users_data)
    return {"ok": out, "message": "Updated"}


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

    