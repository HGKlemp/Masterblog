from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route("/api/posts", methods=["GET", "POST"])
def handle_posts():

    if request.method == "GET":
        return jsonify(POSTS)

    if request.method == "POST":
        data = request.get_json()

        missing_fields = []

        if not data or not data.get("title", "").strip():
            missing_fields.append("title")

        if not data or not data.get("content", "").strip():
            missing_fields.append("content")

        if missing_fields:
            return jsonify({
                "error": f"Missing required field(s): {', '.join(missing_fields)}"
            }), 400

        if POSTS:
            new_id = max(post["id"] for post in POSTS) + 1
        else:
            new_id = 1

        new_post = {
            "id": new_id,
            "title": data["title"],
            "content": data["content"]
        }

        POSTS.append(new_post)

        return jsonify(new_post), 201


@app.route("/api/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):

    for post in POSTS:
        if post["id"] == post_id:
            POSTS.remove(post)

            return jsonify({
                "message": (
                    f"Post with id {post_id} "
                    f"has been deleted successfully."
                )
            }), 200

    return jsonify({
        "error": f"Post with id {post_id} was not found."
    }), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)