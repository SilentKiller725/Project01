from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/register", methods=["POST"])
def register():
    data = request.json  # Get JSON data from the request
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    
    # Example: Just return the received data (normally, you would store it in a database)
    return jsonify({
        "message": "User registered successfully",
        "username": username,
        "email": email
    }), 201  

if __name__ == "__main__":
    app.run(debug=True)
