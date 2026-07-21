from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app)


SWAGGER_URL = "/api/docs"
API_URL = "/static/masterblog.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Masterblog API"
    }
)

app.register_blueprint(
    swagger_ui_blueprint,
    url_prefix=SWAGGER_URL
)


POSTS = [
    {
        "id": 1,
        "title": "First post",
        "content": "This is the first post."
    },
    {
        "id": 2,
        "title": "Second post",
        "content": "This is the second post."
    },
]


def find_post(post_id):
    """Return the post with the given ID or None if it does not exist."""

    for post in POSTS:
        if post["id"] == post_id:
            return post

    return None


@app.route("/api/posts", methods=["GET", "POST"])
def handle_posts():
    """Return all posts or create a new post."""

    if request.method == "GET":
        sort_field = request.args.get("sort")
        direction = request.args.get("direction")

        if sort_field is None and direction is None:
            return jsonify(POSTS), 200

        if sort_field not in ["title", "content"]:
            return jsonify({
                "error": "Invalid sort field. Use 'title' or 'content'."
            }), 400

        if direction not in ["asc", "desc"]:
            return jsonify({
                "error": "Invalid direction. Use 'asc' or 'desc'."
            }), 400

        reverse_sort = direction == "desc"

        sorted_posts = sorted(
            POSTS,
            key=lambda post: post[sort_field].lower(),
            reverse=reverse_sort
        )

        return jsonify(sorted_posts), 200

    if request.method == "POST":
        data = request.get_json(silent=True)

        missing_fields = []

        if not data or not data.get("title", "").strip():
            missing_fields.append("title")

        if not data or not data.get("content", "").strip():
            missing_fields.append("content")

        if missing_fields:
            return jsonify({
                "error": (
                    f"Missing required field(s): "
                    f"{', '.join(missing_fields)}"
                )
            }), 400

        if POSTS:
            new_id = max(post["id"] for post in POSTS) + 1
        else:
            new_id = 1

        new_post = {
            "id": new_id,
            "title": data["title"].strip(),
            "content": data["content"].strip()
        }

        POSTS.append(new_post)

        return jsonify(new_post), 201


@app.route("/api/posts/search", methods=["GET"])
def search_posts():
    """Search posts by title and/or content."""

    title = request.args.get("title", "").lower()
    content = request.args.get("content", "").lower()

    filtered_posts = []

    for post in POSTS:
        title_matches = title in post["title"].lower()
        content_matches = content in post["content"].lower()

        if title and content:
            if title_matches and content_matches:
                filtered_posts.append(post)

        elif title:
            if title_matches:
                filtered_posts.append(post)

        elif content:
            if content_matches:
                filtered_posts.append(post)

        else:
            filtered_posts.append(post)

    return jsonify(filtered_posts), 200


@app.route("/api/posts/<int:post_id>", methods=["PUT", "DELETE"])
def handle_post(post_id):
    """Update or delete a post with the given ID."""

    post = find_post(post_id)

    if post is None:
        return jsonify({
            "error": f"Post with id {post_id} was not found."
        }), 404

    if request.method == "DELETE":
        POSTS.remove(post)

        return jsonify({
            "message": (
                f"Post with id {post_id} "
                f"has been deleted successfully."
            )
        }), 200

    if request.method == "PUT":
        data = request.get_json(silent=True)

        if not data:
            data = {}

        if "title" in data:
            post["title"] = data["title"]

        if "content" in data:
            post["content"] = data["content"]

        return jsonify(post), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5002,
        debug=True
    )