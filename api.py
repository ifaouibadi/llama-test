from bot import verse_bot

from flask import Flask, request, jsonify


# Dummy data to simulate chat threads
chat_threads = {}

app = Flask(__name__)
chat = verse_bot()

response = chat("What is GuardMe")

print('response: ', response)



# @app.route("/chat/<thread_id>", methods=["POST"])
# def send_message(thread_id):
#     # Check if the thread exists, if not, create it
#     if thread_id not in chat_threads:
#         chat_threads[thread_id] = []

#     # Get the JSON data from the request
#     data = request.get_json()

#     # Check if the 'message' property is present in the JSON data
#     if "message" not in data:
#         return jsonify({"error": "Missing message property"}), 400

#     message = data["message"]

#     # Add the message to the chat thread
#     chat_threads[thread_id].append(message)

#     response = chat("What is GuardMe")

#     return jsonify({"message": response}), 201


# if __name__ == "__main__":
#     app.run(debug=False)
