from flask import Flask, jsonify, request, render_template
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="localhost",
    user="root",
    password="riptide",
    database="papertrail"
)

cursor = db.cursor()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/archive", methods=["GET"])
def get_notes():
    cursor.execute("select*from archive")
    notes = cursor.fetchall()
    if not notes:
        return jsonify({"message": "No notes found!"})
    return jsonify(notes)

@app.route("/archive", methods=["POST"])
def add_note():
    data = request.get_json()
    cursor.execute("INSERT INTO archive (title, content) VALUES (%s, %s)", (data["title"], data["content"]))
    db.commit()
    return jsonify({"message": "Note added!"})

@app.route("/archive/<int:note_id>", methods=["GET"])
def get_note(note_id,note_title):
    cursor.execute("SELECT * FROM archive WHERE id = %s or title=%s", (note_id,note_title))
    note = cursor.fetchone()
    return jsonify(note)

@app.route("/archive/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    data = request.get_json()
    note_title = data.get("note_title")  # Extract note_title from JSON
    cursor.execute("DELETE FROM archive WHERE id = %s OR title = %s", (note_id, note_title))
    db.commit()
    return jsonify({"message": "Note deleted!"})

@app.route("/archive/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    data = request.get_json()
    note_title = data.get("note_title")  # Extract note_title from the JSON request
    cursor.execute("UPDATE archive SET title = %s, content = %s WHERE id = %s OR title = %s", 
                   (data["title"], data["content"], note_id, note_title))
    db.commit()
    return jsonify({"message": "Note updated!"})

if __name__ == "__main__":
    app.run(debug=True)

