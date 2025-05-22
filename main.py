from flask import Flask, request, jsonify
from flask_cors import CORS
from planner.chat import start_chat_session

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  # restrict to your frontend origin

chat_handler = start_chat_session()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = chat_handler.send_message(user_input)
        print("Reply to send:", response.text.strip())  # debug print
        return jsonify({"reply": response.text.strip()})
    except Exception as e:
        print("Error in /chat:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5050)
