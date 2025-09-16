from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# In-memory task storage
tasks = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task_text = data.get("task", "").strip()
    if task_text:
        task = {"id": len(tasks) + 1, "task": task_text, "done": False}
        tasks.append(task)
        return jsonify(task), 201
    return jsonify({"error": "Task cannot be empty"}), 400

@app.route("/tasks/<int:task_id>/toggle", methods=["PUT"])
def toggle_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

